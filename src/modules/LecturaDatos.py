#se importan las liberias necesarias para este modulo
import re
#import pandas as pd


def lectura(archivo):
    '''
    Lee los datos de los generadores.
    Recibe como entrada un string que es el nombre del archivo
    Devuelve listas de los datos en el siguiente orden
    bus
    governor
    CON
    porcentaje
    idg
    comentario
    '''
    datos_generadores=list()
    regiones=list()
    generadores_restar=list()
    lineas=list()
    with open(archivo,'r') as conteo:
        n=0
        cortes=list()
        for line in conteo:
            lineas.append(line)
            n+=1
            if line.startswith('99999'):
                cortes.append(n)
        print(cortes)


    j=1

    for linea in lineas:
        
        if j==1:
            reserva_fijar=linea
        if j==2:
            parametros=linea  
        if (j<cortes[0] and j>2):
            temporal=linea.strip()
            generador=re.split('\s+',temporal,5) 
            datos_generadores.append(generador)   
        if (j>cortes[0]and j<cortes[1]):
            temporal=linea.strip()
            region=re.split('\s+',temporal,2)
            regiones.append(region)
        if (j>cortes[1]):
            temporal=linea.strip()
            a_restar=re.split('\s+',temporal,3)
            generadores_restar.append(a_restar)
        j+=1



    temp1=re.split('\s',reserva_fijar)
    temp2=(re.split('\s',parametros))
    recorta=temp2[1]
    reserva=temp2[3]
    maquinas=temp2[5]
    print(recorta, reserva,maquinas)


    #print(datos_generadores)
    #print(regiones)
    #print(generadores_restar)
    #se desglozan los datos de los generadores

    i=0
    bus=list()
    governor=list()
    CON=list()
    porcentaje=list()
    idg=list()
    comentario=list()

    for generador in datos_generadores:
        bus.append(int(generador[0]))
        governor.append(generador[1])
        CON.append(int(generador[2]))
        porcentaje.append(float(generador[3]))
        idg.append(generador[4])
        comentario.append(generador[5])


    #se crea el dataframe para tener una mejor optimización
    #df_datos=pd.DataFrame({'BUS':bus,'GOVERNOR':governor,'CON':CON,'PORCENTAJE':porcentaje,'IDG':idg,'COMENTARIO':comentario})
    #df_datos.head(5)
    #df_datos.info()

    #se borran las listas para no tener un uso de memoria insuficiente
    #del(bus,governor,CON,porcentaje,idg,comentario)
    return(bus,governor,CON,porcentaje,idg,comentario)
