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
import socket

#Clase que se encarga de analizar puertos abiertos

class PortScanner():
    def __init__(self):
        pass

    def scan_ports(self, beginPort, endPort):

        sck = socket.socket()
        host = str(socket.gethostbyname(socket.gethostname()))
        #host = host.replace('.', "")
        header=['Puerto','Servicio', 'Estado']
        resultado = []
        resultado.insert(0,header)
        contador=0
        for port in range(beginPort,endPort+1): 
            try:
                sck.connect((host,port))
                resultado.append([str(port),socket.getservbyport(port), "abierto"])
                contador+=1
                sck.close()
         
            except :
                pass#resultado+=  "Port "+str(port)+" cerrado \n"
        resultado.append([str(contador),'','Puertos Abiertos'])
        resultado.append([str(2**16-contador), '','Puertos Cerrados'])
        return resultado



def main(args):
    
    scanner = PortScanner()
    print(scanner.scan_ports(1, 9999))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
