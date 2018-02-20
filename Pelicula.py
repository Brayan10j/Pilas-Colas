class Pelicula():
    def  __init__ (self,  genero, actor):
        self.Genero=genero
        self.Actor=actor

from Pila import *
def inicio():
    
    pila1=Pila()
    pila2=Pila()
    
    print("Bienvenido")
    while True:
        print ("1-Agregar Pelicula")
        print ("2-Buscar Pelicula")
        
        print ("3-Salir")
        x=input("Digite una opcion: ")
        x=int(x)
        if x==1:
            
            genero=input("Genero de la Pelicula? ")
            
            actor=input("Actor de la Pelicula? ")
            pelicula=Pelicula(genero,actor)            

            pila1.apilar(pelicula)
        elif x==2:
            p=input("Genero de la Pelicula? ")
            while len(pila1.items) != 0:
                pelicula=pila1.desapilar()
                pila2.apilar(pelicula)
                if(p==pelicula.Genero):
                    print (pelicula.Genero)

            while len(pila2.items)!= 0:
                pelicula=pila2.desapilar()
                pila1.apilar(pelicula)            
                
        elif x==3:
            print (len(pila1.items))
        elif x==4:
            break
        else:
            print ("ingrese una opcion valida")
