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
import pdb

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
        
        empty_format = '|{:=<' + str(max_length) + '}'
        row_format = '|{:<' + str(max_length) + '}'
        empty_format = empty_format*2 + '|' 
        row_format = row_format*len(arg[0]) + '|'
        text = row_format.format(*arg[0])
        for row in arg[1:]:
            text += '\n' + empty_format.format(*('',''))
            text += '\n' + row_format.format(*row) 
        text += '\n' + empty_format.format(*('',''))
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

def main(args):
    writer = Writer()
    arg = (('0123456789012345','Licencia'),('unrar', 'GPL'),('zip', 'GPL-2'),('vim', 'Charityware'))
    print(writer.write_txt(arg))
    
    #Probar escritura de archivo
    writer.write(arg, 'test.txt')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
