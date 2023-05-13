!pip install fluids
!pip install pint
!pip install mariadb

import pint #manejo unds
ureg = pint.UnitRegistry()
from fluids.units import *

class pipeCalculator:
    def __init__(self,inlet_P,total_caudal,delta_Pmax,height_of_system=1000):
        import numpy as np
        self._work_long=self.takeAll()[0]*ureg.m
        self._accesories=self.takeAll()[1]
        self._in_P=inlet_P*ureg.Pa
        self._total_caudal=total_caudal*((ureg.m**3)/ureg.s)
        self._delta_P=delta_Pmax
        self._second_pipes=self.takeAll()[2]
        self._height_of_system=height_of_system*ureg.m

    def atmospheric_properties(self):
        from fluids.atmosphere import ATMOSPHERE_1976
        atm_props=ATMOSPHERE_1976(Z=float(self._height_of_system.magnitude))
        rhoDensity=atm_props.rho # get rho @ Medellín height
        airMu=atm_props.viscosity(298) # dynamic viscosity @ T ambient *u.K
        return rhoDensity,airMu
    
    def checkdP_fromD(self,seedDia, workLong, kAcces, secondPipeSeedDia, secondPipeSects, inletP,Qtot):#find drop preassure
        import numpy as np #modules
        from fluids.fittings import Hooper2K, contraction_sharp
        from fluids.core import Reynolds
        from fluids.core import K_from_f
        from fluids.core import dP_from_K
        from fluids.friction import friction_factor
        from fluids.friction import nearest_material_roughness, material_roughness
        
        areaFunction=lambda x: (np.pi*x**2)/4 #calculate pipe area
        seedA=areaFunction(seedDia)
        rhoDensity,airMu=self.atmospheric_properties() # get rho @ Medellín high, dynamic viscosity @ T ambient *u.K
        V=Qtot/seedA # compressed air velocity
        Re = Reynolds(V=V, D=seedDia, rho=rhoDensity, mu=airMu)#calculate reynolds u/u
        epsilon=material_roughness( nearest_material_roughness('compressed air', clean=True), D=seedDia, optimism=True ) #*u.m roughness for pipe material
        fd = friction_factor(Re, eD=epsilon/seedDia) # friction factor
        k=0# klosses for friction factor and accesories
        k+=K_from_f(fd=fd, L=workLong, D=seedDia)#add at first the losses from friction factor
        for i in kAcces:#start of losses calculation from accesories
            k+=Hooper2K(Di=seedDia,Re=Re,name=i)#losses for 1 accesory
            #---->check number of accesories for that pipe
        KContractions=secondPipeSects*contraction_sharp(Di1=seedDia,Di2=secondPipeSeedDia,fd=fd,roughness=epsilon) #loss for contractions from one pipe to another of different diameter
        k+=KContractions#final of process adding losses for contractions
        dropP=dP_from_K(k,rho=rhoDensity,V=V)# calculate drop preassure
        dP=(dropP/inletP)*100 # DeltaP=deltaP_max?
        return dP
    
    def takeAll(self):
        import numpy as pd
        try:
            conexion=connection()
            listLongInitial=[]
            listLongFinal=[]
            listAccessories=[]
            for i in conexion._tablas:
                resultSet=conexion.mostrar(i)
                if i==conexion._tablas[0] or i==conexion._tablas[1]:
                    for j in resultSet:
                        listAccesories.append(j[1])
                else:
                    amtSecundarias=0
                    if i=="tuberiasecundaria":
                        amtSecundarias=len(i)
                    for j in resultSet:
                        listLongInitial.append(eval(j[1]))
                        listLongFinal.append(eval(j[2]))
            workLong=0
            for i,j in zip(listLongInitial,listLongFinal):
                difference_coors=j-i
                difference_coors=difference_coors**2
                workLong+=
            return workLong,listAccessories,amtSecundarias
        except Exception as err:
            print(err)
    
    def find_diameter(self):#method to find min diameter
        dP=self._delta_P
        deltaP=10*dP
        seedD=0.1 #*u.m seed diameter
        seedD2=seedD*0.8
        #attributes values
        workL=self._work_long.magnitude
        inP=self._in_P.magnitude
        q_total=self._total_caudal.magnitude
        while True:
            deltaP=self.checkdP_fromD(seedDia=seedD,workLong=workL,kAcces=self._accesories,secondPipeSeedDia=seedD2,secondPipeSects=self._second_pipes,inletP=inP,Qtot=q_total)
            if deltaP<=dP:
                break
            seedD+=seedD*0.05
        seedDResult=round(seedD,3)*ureg.inches
        return seedDResult
        

import mariadb

class connection:
    def __init__(self):
        query_tableNames="SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'red_aire';"
        cur=self.query_connection(query_tableNames)
        self._tablas=[i[0] for i in cur]
    #connection db to execute query
    def query_connection(self,query,parameters=""):
        try:
            conn=mariadb.connect(
            host="localhost",
            user="root",
            password="",
            database="red_aire",
            autocommit=True)
            cur=conn.cursor()#cur to get query results
            print(query)
            cur.execute(query,parameters)
            return cur
        except Exception as err:
            print("No fue posible conectarse")
            print(err)
    
    def column_name_getter(self,tabla):
        dict_columnNames={}
        try:
            query_columnNames="select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{}';".format(tabla)
            cur=self.query_connection(query_columnNames)
            list_columnNames_result=[j[0] for j in cur]
            dict_columnNames[tabla]=list_columnNames_result
            print(dict_columnNames)
            return dict_columnNames
        except Exception as err:
            print('No fue posible obtener los nombres de las columnas en la tabla específica')
            print(err)
            
    def map_parameter(self,tabla,op):
        try:
            tableInfo=self.column_name_getter(tabla)
            info=tableInfo[tabla]
            parametersSyntax=""
            if op==1:
                str_parameters="`{}` = %s,"#str to get Update parameters
            else:
                str_parameters="`{}`,"

            for j in range(1,len(info)):
                parametersSyntax+=str_parameters.format(info[j])
            parametersSyntax=parametersSyntax[:-1]#delte last comma to correct syntax
            print(parametersSyntax)#revision_flag
            return parametersSyntax
        except Exception as err:
            print("No fue posible construir la lista de parametros de la tabla específica")
            print(err)
    #begin CRUD
    def agregar(self,tabla,parameters):
        #add data into table with reference to another table if applicable
        try:
            map_parameters=self.map_parameter(tabla,2)
            id_=self.column_name_getter(tabla)
            valueAmt=(len(id_[tabla])-1)*"%s,"
            valueAmt=valueAmt[:-1]
            curQuery="INSERT INTO `{}` ({}) VALUES ({})".format(tabla,map_parameters,valueAmt)
            print(curQuery,parameters)
            self.query_connection(curQuery,parameters)
            self.mostrar(tabla)
        except Exception as err:
            print("No fue posible agregar el dato")
            print("tabla: {}, parametros: {}".format(tabla,parameters))
            print(err)
    
    def mostrar(self,tabla,where=""):
        #every time mostrar(), results on visual must be deleted
        #--->pending
        try:
            if len(where)*len(tabla)>0:#dato especifico para buscar en db existe?
                try:
                    table_cols=self.column_name_getter(tabla)[tabla]
                    curTabla_indexing="SELECT * FROM `{}` WHERE `{}` = {}".format(tabla,table_cols[0],where)#query to get data with specific value
                    cur=self.query_connection(curTabla_indexing)#execute query
                    return cur
                except Exception as err:
                    print('No fue posible obtener el dato específico de la tabla')
                    print(err)
            else:
                curTabla="SELECT * FROM `{}`;".format(tabla)#query to get all data from table
                cur=self.query_connection(curTabla)
                return cur
        except Exception as err:
            print('No fue posible obtener todos los datos de la tabla en específico')
            print(err)
    
    def editar(self,tabla,parameters,where):
        try:
            map_parameters=self.map_parameter(tabla,1)
            id_=self.column_name_getter(tabla)
            id_=id_[tabla][0]
            curQuery="UPDATE `{}` SET {} WHERE `{}` = {}".format(tabla,map_parameters,id_,where)
            print(curQuery,parameters)
            self.query_connection(curQuery,parameters)
        except Exception as err:
            print("No fue posible editar el dato especificado")
            print(err)
    
    def eliminar(self,tabla,where):
        try:
            tableInfo=self.column_name_getter(tabla)[tabla]
            id_=tableInfo[0]
            curQuery="DELETE FROM `{}` WHERE `{}` = {}".format(tabla,id_,where)
            print(curQuery)
            self.query_connection(curQuery)
        except Exception as err:
            print("No fue posible eliminar el dato")
            print(err)
    #final CRUD