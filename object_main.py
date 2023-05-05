!pip install fluids
!pip install pint

class pipeCalculator:
    def __init__(self,work_long,accesories,inlet_P,total_caudal,delta_Pmax,height_of_system):
        self._work_long=work_long
        self._accesories=accesories
        self._in_P=inlet_P
        self._total_caudal=total_caudal
        self._delta_P=delta_Pmax
        self._height_of_system=height_of_system

    def atmospheric_properties(self):
        from fluids.atmosphere import ATMOSPHERE_1976
        atm_props=ATMOSPHERE_1976(self._height_of_system)
        rhoDensity=atm_props.rho # get rho @ Medellín height
        airMu=atm_props.viscosity(298) # dynamic viscosity @ T ambient *u.K
        return rhoDensity,airMu

    def checkdP_fromD(self,seedDia, atmObj, workLong, kAcces, secondPipeD, secondPipeSects, inletP,Qtot):#find drop preassure
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
            k+=Hooper2K(Di=seedDia,Re=Re,name=i[0])*i[1] # seedD.to_tuple()[0]
        KContractions=secondPipeSects*contraction_sharp(Di1=seedDia,Di2=secondPipeD,fd=fd,roughness=epsilon) #loss for contractions from one pipe to another of different diameter
        k+=KContractions#final of process adding losses for contractions
        dropP=dP_from_K(k,rho=rhoDensity,V=V)# calculate drop preassure
        dP=dropP/(inletP*10E5) # DeltaP=deltaP_max?
        return dP
    
    def find_diameter(self):#method to find min diameter
        deltaP=10*self._delta_P
        seedD=0.001 #*u.m seed diameter
        while deltaP>self._delta_P:
            seedD+=seedD*0.5
            deltaP=checkdP_fromD(seedDia=seedD,...)