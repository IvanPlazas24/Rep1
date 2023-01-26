# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:48:35 2021

@author: WINDOWS
"""
#Programa principal
carta_mano={"numero": 9,
            "palo": "trebol"}
opcion_1={"numero": 2,
            "palo": "picas"}
opcion_2={"numero": 3,
            "palo": "diamantes"}
def cambio_de_cartas(carta_mano: dict, opcion_1: dict, opcion_2: dict)->int:
    resultado=None
    if carta_mano["palo"]==opcion_1["palo"] or carta_mano["numero"]==opcion_1["numero"]:
       resultado=1
    elif carta_mano["palo"]==opcion_2["palo"] or carta_mano["numero"]==opcion_2["numero"]:
       resultado=2
    else:
        resultado=0
    return resultado