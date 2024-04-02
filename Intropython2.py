#while
#while< condicion sea veradera>:
#   cuerpo del ciclo
#condiciones son: expresiones boleanas (or, and) y operaciones de comparacion
#ciclos controlados por un contador enteros

i=0 #increment
k=0

while i<10:
    print ("ciclo")
    #importante controlar el valor del contador
    i=i+1 # es equivalente decir (i+=1)


import random
a=0

while a != 5:
    a=random.randint(1,10) #por evento 
    print(a)

print("se acabo")

a=0
while 1==1:
    a= int(input("ingrese un número")) #por variable
    
    if a==10:
        break

# for: se utiliza para recorrer un "iterable"
# una lista, tupla, diccionario.....
    
# lista: comjunto de variables organizadas en 
#esopacios consecutivos de memoria. A las que
#se les asigna un unico nombre. se diferencian
#por la posicion que ocupan respecto al primer 
#elementos de una lista

miLista= [1, True, "textos", 3.89]
miLista=[]


#en Python todos son objetos. tiene metodos y atributos
print (miLista)
miLista.append(45) #añade un elemento al final de la lista
print(miLista)

print (miLista)
miLista.insert(0, "Hola") #añade un elemento al inicio de la lista
print(miLista)

print (miLista)
miLista.pop(2) #remueve el item en el indice que yo le pida
print(miLista)

print (miLista)
miLista.sort(45) #ordena la lista de manera descendente o ascendente
print(miLista)

print (miLista)
miLista(len(45)) #mide la longuitud de un iterable 
print(miLista)

#Tupla: lista inmutable

miTupla=(2,45,6,8,9,10)

#for: ciclo para recorrer iterables. el cuerpo
#se repite la cantidad de elementos que tenga el
#iterable. en cada ciclo se guarda el valor.
#estructura del FOR en python: 
#for<variable_donde_guardo_el_elemento in iterable:

for x in miLista:
    print(x)
    if x>50:
        print("grande")

#si solo utilizo el iterable para definir la cantidad 
#de repeticiones entonces no es necesaria la variable
        
for _ in miLista:
    print("ciclo")

#si no tengo un iterable puedo usar la funcion 
#range() para generar una secuencia de numeros

for x in range(-10, 10):
    print(x)

#Taller:
#crear un programa en consola que pida un numero al usuario y
#1. imprima los numeros impares entre -nuemeros y numero 
#2. imprima los numeros primos entre 0 y numero 100
#el programa debe garantizar que el usuario ingrese un numero positivo >0
    
#entrega antes de las 4 en el repositorio
    
