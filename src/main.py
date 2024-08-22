import os
import sys

#import LecturaDatos as LD
#import VerificacionDatos as VD
#import CalculoReserva as CR
#import PruebaExcel as PD
 
sys_path_PSSE=r'E:\PSS\PSSPY34'
sys.path.append(sys_path_PSSE)

 
os_path_PSSE=r'E:\PSS\PSSBIN'
os.environ['PATH'] += ';' + os_path_PSSE
os.environ['PATH'] += ';' + sys_path_PSSE
 
#importacion de librerias necesarias
import redirect
import datetime
import re
import tkinter
import pssexplore34
import psspy

#importacion de librerias propias
import modules.lectura as lectura 
import modules.informe as informe

_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()

psspy.psseinit(1000)

CASE='savnw.sav'

psspy.case(CASE)

psspy.cong(0)
psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
psspy.fact()
psspy.tysl(0)

# Open snap.
psspy.rstr(r"""savnw""")
psspy.dynamicsmode(0)

# 1 - Crear el archivo de salida
ruta='E:/PF_IE'
informe.crear(ruta)

# 2 - Lectura de los parametros
parametros=lectura.parametros()

# 3 - Lectura de datos del archivo "reserva.dat"
bus,governor,CON,porcentaje,idg,comentario,tipo=lectura.generadores()

# 4 - Verificacion de los datos
"""nombre=list()
cmpval=list()
v=list()
v1=list()
indice_ini=list()
rval=list()
for i in range(0,len(bus)):
   nombre_temp, cmpval_temp,v_temp,v1_temp, indice_ini_temp,rval_temp=VD.verificacionDatos(bus[i],idg[i],CON[i])
   nombre.append(nombre_temp)
   cmpval.append(cmpval_temp)
   v.append(v_temp)
   v1.append(v1_temp)
   indice_ini.append(indice_ini_temp)
   rval.append(rval_temp)"""

# 5 - Determinación de los margenes de reserva

#creación de listas para verificar datos y almacenar los restantes



#---------------
#calculo de límites de los governors en este caso de TGOV1 y HYGOV
"""   P=list()
   Q=list()
for pq in cmpval:
   P.append(pq.real)
   Q.append(pq.imag)

total=0
for i,gov in enumerate(governor):
   print(gov,i)
   if gov=='TGOV1':
      reserva,pot=CR.TGOV1(rval[i],v[i],P[i])
      print('la reserva es ', reserva)
      
   if gov=='HYGOV':
      reserva,pot=CR.HYGOV(indice_ini[i],rval[i],v[i],P[i])
      print('el limite es ',reserva)
   total+=reserva
print('la reserva total es ',total)"""

"""
Revisar esto porque no puede ser la potencia generada mayor que la maxima y debe estar considerado en los errores->
RESERVATOTAL=RESERVATOTAL+((pmaxi(ngen)-P(ngen))*Aux01)


RESERVATOTAL2=RESERVATOTAL2+(pmaxi(Igen)-P(Igen))

Se deteermina la nueva reserva en base al dato del archivo 
reserva_nueva=reserva_optima*gen_SADI/100
(GENSADI=(PA-TOTALRESTA) en la generacion del sadi se resta los generadores que no aportan a la generacion pgeuru=pgeuru+pge y
que generacion de que regiones se restan TOTALRESTA=TOTALRESTA+PA)

RESERVANUEVA=((RESERVAOPTIMA/100.)*(GENSADI)) se calcula la nueva reserva una vez calculada la generacion del SADI 

DIFNUE(IGEN)= RESERVANUEVA*DIFEGEN(IGEN)/RESERVATOTAL2 aca se calcula la nueva reserva para el generador en cuestion 

PMAXINUE(IGEN)=P(IGEN)+DIFNUE(IGEN) se calcula nueva potencia maxima del generador para poder cambiar los limites

PMAXINUE2(IGEN)=P(IGEN)*(1.+PORCE(IGEN)/100.)

RESERVANUEVAX=(PMAXINUE(IGEN)-P(IGEN))+RESERVANUEVAX

totadif=totadif+DIFNUE(IGEN)

totamax=totamax+pmaxiNUE(IGEN)-P(IGEN)
"""
#Se registran los generadores que tienen PMAX<PGEN (1721)
#ERRROR EN GENERADOR, ibus, id, nombre

#Se registran en pmax_pgen.prn "DETALLES DE RESERVA DE GENERADORES" (1732)
#IBUS NOMBRE ID POT_MAX POT_GEN MAX_GEN RESERVA% PORCENTAJE DATO RESOPT 

#DIFPOT=pmax-p es la reserva que queda

#Registrar generadores con reserva por debajo de la optima (1799)

#Registrar generadores con reserva mayoor a la maxima (1831)

"""Saca informe con
el titulo del escenario
reserva hidro, termica y total
revisar el tema de la reserva util
(1850)
"""

#Extrae generacion del sistema (1880)

"""Se registra los generadores que salen
gensale, ibus, nombre, PQ, id
generacion restar
"""

#Se analizan las aeras

#Se registra Genreacion Activa Reactiva (1996)
#iarea, nombrearea

#---------
#prueba para el cambio de CON
#primero miro el CON

"""for i,gov in enumerate(governor):
      if gov=='HYGOV':
         ierr,rval20=psspy.dsrval('CON',(indice_ini[i]+11))
         ierr,rval22=psspy.dsrval('CON',(indice_ini[i]+9))
         print('los valores de CON de HYGOV  son ',rval20,', ',rval22)
         psspy.change_con(indice_ini[i]+11, 0.5)
         psspy.change_con(indice_ini[i]+9,2)
         ierr,rval20=psspy.dsrval('CON',(indice_ini[i]+11))
         ierr,rval22=psspy.dsrval('CON',(indice_ini[i]+9))
         print('los nuevos valores CON de HYGOV  son ,',rval20,', ',rval22)

#verifico que me cambio los limites

total=0
for i,gov in enumerate(governor):
   print(gov,i)
   if gov=='TGOV1':
      reserva,pot=CR.TGOV1(rval[i],v[i],P[i])
      print('la reserva es ', reserva)
      
   if gov=='HYGOV':
      reserva,pot=CR.HYGOV(indice_ini[i],rval[i],v[i],P[i])
      print('el limite es ',reserva)
   total+=reserva
print('la reserva total es ',total)"""