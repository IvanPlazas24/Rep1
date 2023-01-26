# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:45:15 2021

@author: WINDOWS
"""
#Punto 1
def mayor(a: float, b: float)->float:
    "Retorna el mayor numero entre a y b"
    mayor=0
    if a>mayor and a>b:
       mayor=a 
    elif b>mayor and b>a:
       mayor=b        
    else:
       mayor 
    return mayor
#Punto 2
def mayor3(a: float,b: float,c: float)->float:
    "Retorna el mayor numero entre a, b y c"
    mayor=0
    if a>mayor and a>b and a>c:
       mayor=a
    elif b>mayor and b>a and b>c:
        mayor=b
    else:
        mayor=c
    return mayor
#Punto 3
def bisiesto(anio: int)->bool:
    "Retorna True si anio es un año bisiesto y False de lo contrario"
    respuesta=True
    if anio%4!=0:
       respuesta=False
    elif anio%100!=0:
       respuesta=True
    elif anio%400!=0:
       respuesta=False
    else:
       respuesta=True
    return respuesta 
#Punto 4
def clasificar(a1: float,a2: float,a3: float)->str:
    "Retorna un Equilatero, si el triangulo es equilatero, Isoceles si es isoceles y Escaleno si es escaleno"
    Respuesta=""
    if a1==a2==a3:
       Respuesta="Equilatero"
    elif a1==a2 or a1==a3 or a2==a3:
        Respuesta="Isoceles"
    else:
       Respuesta="Escaleno"
    return Respuesta   
#Punto 5
def solucionar(a: float,b: float,c: float)->str:
    respuesta=""
    primer_paso=((b**2)-(4*(a)*(c)))
    if a==0:
       respuesta="La ecuacion no tiene solucion"
    elif primer_paso<0:
        respuesta="La ecuacion no tiene solucion"
    else:
         
         solucion1=(-(b)+(primer_paso**(1/2)))/(2*a)
         solucion2=(-(b)-(primer_paso**(1/2)))/(2*a)
         respuesta="Las soluciones de la ecuacion cuadratica son x1 = "+str(round(solucion1,2))+" y x2 = "+str(round(solucion2,2))+"."
    return respuesta    
    
        
        