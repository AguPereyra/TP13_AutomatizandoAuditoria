#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  auditoriaAutomatica.py
#  
#  Copyright 2018 Unknown <root@pc-piola>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pdb, subprocess, platform, inspect, os
from portScanner import PortScanner

#Clase que se encarga de escribir un archivo con formato de tabla
#para los datos que le pasan
class Writer():
    TEXT = 0
    def __init__(self):
        pass

    #Metodo que escribe archivo de texto plano
    #Parametros:
    #           arg: Tupla con las filas a imprimir
    #
    #Retorna:   cadena formateada
    def write_txt(self, arg):
        #Busqueda de la cadena mas larga de la columna
        max_col = 0
        max_length = 0
        for row in arg:
            max_col = len(arg[0])
            #Eleccion de la columna mas larga
            for i in range(len(arg[0])):
                if max_col < len(row[i]):
                    max_col = len(row[i])
            #Eleccion del maximo largo
            if max_col > max_length:
                max_length = max_col
        
        #Obtener columnas
        col = ['']
        for i in range(len(arg[0])-1):
            col.append('')

        empty_format = '|{:=<' + str(max_length) + '}'
        row_format = '|{:<' + str(max_length) + '}'
        empty_format = empty_format*len(col) + '|' 
        row_format = row_format*len(arg[0]) + '|'
        text = row_format.format(*arg[0])

        for row in arg[1:]:
            text += '\n' + empty_format.format(*col)
            text += '\n' + row_format.format(*row) 
        text += '\n' + empty_format.format(*col)
        return text

    #Metodo que crea un archivo con los datos pasados
    #Parametros:
    #           arg: Tupla con las filas a imprimir en el archivo
    #           name: Path del archivo a crear
    #           kind: Tipo de formato del archivo
    def write(self, arg, name, kind = TEXT):
        #Verificar que todas las tuplas tengan igual largo
        length = len(arg[0])
        for row in arg:
            if length != len(row):
                raise Exception("Tuplas no consistentes")

        #Escribir archivo
        if kind == self.TEXT:
            txt = self.write_txt(arg)
            fl = open(name, 'w')
            fl.write(txt)
            fl.close()


class SoftwareAudit():
    def __init__(self):
        pass
    
    #Clase que retorna el software instalado
    #en la maquina y su version si conoce
    #el SO host
    #Parametros:
    #           platform: El SO de la maquina host, si es Linux, indica
    #                     la distribucion.
    def get_soft_inst(self, platform):
        #Obtencion de software instalado
        #Depende del SO
        #Diccionario de comandos por SO
        dict_os = {'arch':('pacman', '-Q'), 'Windows':('wmic','/', 'output', ':', os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'\soft.txt' , 'product','get', 'name', ',', 'version')}
        process = subprocess.run(dict_os[platform], capture_output=True, text=True)


        #Si es Windows se imprime directamente
        if platform == 'Windows':
            print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
            return
        #Formateo del resultado
        #¡Ojo! Depende de cómo me lo devuelva la consola
        str1 = process.stdout
        header = ['Software', 'Version']
        print(return_list)
        return_list = str1.split('\n')
        length = len(return_list)
        return_list = return_list[:length-1]
        for i in range(length - 1):
            return_list[i] = return_list[i].split()
        return return_list

#Clase que se encarga de realizar la auditoria de la maquina
class AuditCenter():
    def __init__(self):
        pass
    
    #Metodo que audita diferentes conceptos de la maquina
    #anfitrion
    def run(self):
        sftAudit = SoftwareAudit()
        portScan = PortScanner()
        writer = Writer()

        #Obtener OS
        os = platform.system()
        #Si es Linux, obtener distro
        if os == 'Linux':
            os = platform.linux_distribution()[0]

        #Leer puertos
        port_text = portScan.scan_ports(0, 2**16)
        writer.write(port_text, 'puertos.txt')
        print('Puertos leidos')

        #Leer software instalado
        soft_text = sftAudit.get_soft_inst(os)
        #Si es Windows se imprime directamente
        if os != 'Windows':
            writer.write(soft_text, 'soft.txt')
        print('Software instalado revisado')


def main(args):
    audit = AuditCenter()
    audit.run()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
