## import turtle # importing the turtle library

import turtle

matriz = []

def matriz_crear (matriz):  ## Funcion crear la matriz
    for x in range (6): 
        matriz.append([])
        for y in range (7):
            matriz[x].append(None)
    

def print_matriz(matriz):  ##Funcion imprimir la matriz 
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            print(matriz[x][y], end =" ")
        print()


    
        
matriz_crear(matriz)
print_matriz(matriz)
"""
contador = 0
for x in range(len(matriz)):
    for y in range(len(matriz[x])-3) :
        if matriz[x][y] == 1 and matriz[x][y+1] == 1 and matriz [i][j+2] == 1 and matriz [i][j+3]:
           (or matriz[x][y] == 0 and matriz[x][y+1] == 0 and matriz [i][j+2] == 0 and matriz [i][j+3]:)
           contador += 1
"""
            

def ficha (cursor, radio, x1, y1, color):
    cursor.pencolor(color)
    cursor.penup()
    cursor.setpos(x1,y1)
    cursor.pendown()
    cursor.circle(radio)
    cursor.penup()
   
    
def print_board_circles(height, width, x, y, cursor, radio):
       
    cursor.penup()# levanta el cursor
    cursor.setpos(x,y)#mueve el cursor a una posicion absoluta 
    cursor.pendown()#baja el cursor 
    for i in range (height):#funcion altura 
        for j in range(width):#Ancho 
            cursor.circle(radio)#dibujar un circulo 
            cursor.penup()
            cursor.forward(radio*2)#distancia de separacion entre cimcum
            #en vertical 
            cursor.pendown()
            
        cursor.penup()
        cursor.setpos(x, y+radio*2*(i+1))# aqui supuestamente si substituyo i por x numero lo pinta. 
        #distancia de separacion en horizontal, + radio*x mas altura.
        #el + es para que crzca hacia arriba 
        cursor.pendown()#baja el lapiz para dibujarlo 
    
    # Escribe los números de las columnas.
    cursor.penup()#No pinta
    cursor.setpos(x-radio*2,y-radio) 
    cursor.pendown()#pinta
    cursor.pencolor("grey")
    for i in range (7):
        cursor.penup()
        cursor.forward(radio*2)#la distancia entre los numeros
        cursor.write(i+1, font=("Arial", 20, "normal"))
        #el i+1 indica desde que numero empieza a contar
        
# Creates the window and performs some settings
window = turtle.Screen() #creates a window to draw something
window.bgcolor("white") #sets the background colour
window.title("Connect 4") #sets the window title
window.setup(720,500) #sets he size of the window
window.reset()

cursor = turtle.Turtle() #creates the cursor that allows us to draw
cursor.pensize(2) #set the thickness of the cursor
cursor.pencolor("black") #set the colour of the cursor
cursor.speed(0) #between 1-10

# Board Properties
height = 6 #lineas
width = 7 #columnas

# Coordina donde empezar a dibujar el tablero.
x = -150
y = -150


# Radius of the pieces
radius = 25 #radio de las circumferencias 

# Prints the board in turtle



""" MAIN MENU  
Here you will call the Main Menu function
"""

jugador = 0
ganador = 0
listaX = [0, 0, 0, 0, 0, 0, 0]
################ Menu del juego ###############
menu = tuple(("1. Dos jugadores.", "2. Un solo jugador vs CPU."))

############# Funciones ficha ###############
def posicion_Ficha_ejeX (posicionTablero):# Funcion para eje x, si es 1,2,3,4,5,6,7
    return 50*posicionTablero-200

def posicion_Ficha_ejeY (posicionTablero):# Funcion para eje y, altura de la ficha
    return 50*posicionTablero-150
#############################################

for i in range(len(menu)): #imprime en lista
    print(menu[i])
    
opcion = int(input("Escoge el modo de juego: "))
print_board_circles(height, width, x, y, cursor, radius)


if opcion == 1:
        
    
    menuColor = tuple(("1. Rojo", "2. Azul", "3. Negro", "4. Amarillo", "3. Lila"))
        
    for i in range(len(menuColor)): #imprime en lista
        print(menuColor[i])
        
    colorJ1 = int(input("Jugador 1 escoge el color de tu ficha.")) 
    colorJ2 = int(input("Jugador 2 escoge el color de tu ficha."))
    
    while colorJ1 == colorJ2:
        colorJ2 = int(input("Este color ya lo ha cogido el jugador 1, escoge otro."))        
         
    if colorJ1 == 1:
        colorJ1 = "red"
    elif colorJ1 == 2:
        colorJ1 = "blue"
        
    if colorJ2 == 1:
        colorJ2 = "red"
    elif colorJ2 == 2:
        colorJ2 = "blue"
      
            
    while ganador == 0:
        
        if jugador == 0:
        
            posicion = int(input("Donde quiere poner la ficha: "))

            while listaX[posicion-1] == 6:  #para que no sobrepase las 6 fichas en eje y. 
                posicion = int(input("Fila llena!, ponga su ficha en otra posicion"))

            y1 = posicion_Ficha_ejeY(listaX[posicion-1]) 
            x1 = posicion_Ficha_ejeX(posicion)
            ficha (cursor, radius, x1, y1, colorJ1)
            listaX[posicion-1] += 1 #es igual que listaX[posicion-1]+1
            jugador = 1 #flag para obligar a cambiar jugador 
        else:
            posicion = int(input("Done quiere poner la ficha: "))

            while listaX[posicion-1] == 6:  #para que no sobrepase las 6 fichas en eje y. 
                posicion = int(input("Fila llena!, ponga su ficha en otra posicion"))

            y1 = posicion_Ficha_ejeY(listaX[posicion-1]) 
            x1 = posicion_Ficha_ejeX(posicion)
            ficha (cursor, radius, x1, y1, colorJ2)
            listaX[posicion-1] += 1 #es igual que listaX[posicion-1]+1
            jugador = 0 # lo mismo pero para volver a jugardor "1"

########## Juego ########
#matriz[fila(y1)][posicion-1]= jugador 

turtle.done() 
try:
    turtle.bye()
except:
    print("Game Over!")
