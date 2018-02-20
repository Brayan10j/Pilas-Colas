class Pelicula():
    def  __init__ (self,  genero, actor):
        self.Genero=genero
        self.Actor=actor

from Pila import *
def inicio():
    
    pila1=Pila()
    pila2=Pila()
    pila3=Pila()
    pila4=Pila()
    
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
            g=input("Genero de la Pelicula? ")
            while len(pila1.items) != 0:
                pelicula=pila1.desapilar()
                
                if(g==pelicula.Genero):
                   pila3.apilar(pelicula)
                else
                   pila2.apilar(pelicula)
            a=input("Actor de la Pelicula? ")
            while len(pila3.items) != 0:
                pelicula=pila3.desapilar()
                
                if(a==pelicula.Actor):
                    print ("Pelicula encontrada")
                    pila4.apilar(pelicula)
                else 
                  pila2.apilar(pelicula)
                            
                    
                    

            while len(pila2.items)!= 0:
                pelicula=pila2.desapilar()
                pila1.apilar(pelicula)            
                
        elif x==3:
            
            break
        else:
            print ("ingrese una opcion valida")
