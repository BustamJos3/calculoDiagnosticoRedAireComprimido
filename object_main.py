!pip install fluids
!pip install pint
!pip install mariadb

import pint
ureg = pint.UnitRegistry()
from fluids.units import *

class pipeCalculator:
    def __init__(self,coors,accesories,inlet_P,total_caudal,delta_Pmax,secondPipes,height_of_system):
        import numpy as np
        workLong=np.sqrt(np.sum((coors[1]-coors[0])**2))
        self._work_long=workLong*ureg.m
        self._accesories=accesories
        self._in_P=inlet_P*ureg.Pa
        self._total_caudal=total_caudal*((ureg.m**3)/ureg.s)
        self._delta_P=delta_Pmax
        self._second_pipes=secondPipes
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
        return seedDResult #default in inches
        
import mariadb

class connection:
    def __init__(self):
        query_tableNames="SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='red_aire';"
        cur=self.query_connection(query_tableNames)
        self._tablas=[i for i in cur]
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
            cur.execute(query,parameters)
            return cur
        except Exception as err:
            print("No fue posible conectarse")
            print(err)
    
    def mostrar(self,tabla,id_tabla="",where=""):
        #every time mostrar(), results on visual must be deleted
        #--->pending
        try:
            if len(where)*len(tabla)*len(id_tabla)>0:#dato especifico para buscar en db existe?
                try:
                    curTabla_indexing='SELECT * FROM `'+tabla+'` WHERE `'+id_tabla+'` = '+where#query to get data with specific value
                    cur=self.query_connection(curTabla_indexing)#execute query
                    for i in cur:#print results of specific
                        print(i)
                except Exception as err:
                    print('No fue posible obtener el dato específico de la tabla')
            else:
                curTabla='SELECT * FROM `'+tabla+'`;'#query to get all data from table
                cur=self.query_connection(curTabla)
                for i in cur:#print results
                    print(i)
        except Exception as err:
            print('No fue posible obtener todos los datos de la tabla en específico')
            print(err)
    def agregar(self,tabla,parameters):
        #add data into table with reference to another table if applicable
        try:
            if len(parameters)==4:
                curQuery="INSERT INTO "+tabla+" (`coor_inicial`, `coor_final`, `material`, `deltaP_max`) VALUES (%s,%s,%s,%s)"
                self.query_connection(curQuery,parameters)
            elif len(parameters)==5:
                curQuery="INSERT INTO "+tabla+"(`coor_inicial`, `coor_final`, `material`, `deltaP_max`, `fk_Primaria`) VALUES (%s,%s,%s,%s,%s)"
                self.query_connection(curQuery,parameters)
            elif len(parameters)==2:
                curQuery="INSERT INTO "+tabla+"(`tipo`, `fk_Primaria`) VALUES (%s,%s)"
                self.query_connection(curQuery,parameters)
            elif len(parameters)==2:
                curQuery="INSERT INTO "+tabla+"(`tipo`, `fk_Secundaria`) VALUES (%s,%s)"
                self.query_connection(curQuery,parameters)
            print(curQuery)
            self.mostrar(tabla)
        except Exception as err:
            print("No fue posible agregar el dato")
            print("tabla: {}, parametros: {}".format(tabla,parameters))
            print(err)
    
    #add update method
    
    def eliminar(self,tabla,id_="",where=""):
        try:
            if len(tabla)*len(id_)*len(where)>0:
                curQuery="DELETE FROM "+tabla+" WHERE "+id_+"="+where
                self.query_connection(curQuery)
        except Exception as err:
            print("No fue posible eliminar el dato")
            print(err)