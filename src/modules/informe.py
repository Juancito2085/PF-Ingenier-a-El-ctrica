import openpyxl
import os

def crear (ruta):
    # Creamos el excel en la ruta especificada por el parametro
    wb = openpyxl.Workbook()
    # Eliminamos la hoja por defecto
    wb.remove(wb.active)
    # Creamos las hojas del excel
    wb.create_sheet('reserva_total.prn')
    wb.create_sheet('Pmax_Pgen.prn')
    wb.create_sheet('Mayor_maxima.prn')
    wb.create_sheet('Reserva.rep')
    wb.create_sheet('Reserva.err')
    # Creamos los enacabezados de las hojas
    wb['reserva_total.prn'].append(['Escenario','Reserva Hidro','Reserva Termica','Reserva Total'])
    wb['Pmax_Pgen.prn'].append(['IBUS','NOMBRE','ID','POT_MAX','POT_GEN','MAX_GEN','RESERVA%','PORCENTAJE','DATO','RESOPT'])
    wb['Mayor_maxima.prn'].append(['IBUS','NOMBRE','ID','POT_MAX','POT_GEN','MAX_GEN','RESERVA%','PORCENTAJE','DATO','RESOPT'])
    wb['Reserva.rep'].append(['Escenario','Reserva Hidro','Reserva Termica','Reserva Total'])
    wb['Reserva.err'].append(['Escenario','Reserva Hidro','Reserva Termica','Reserva Total'])
    # Guardamos el excel con el nombre Reserva_salida.xlsx
    ruta_completa= ruta+'/Reserva_salida1.xlsx'
    wb.save(ruta_completa)
    # Mensaje que avisa que el archivo se ha creado en la ruta especificada
    print('Archivo creado en la ruta: ',ruta_completa)
    return
