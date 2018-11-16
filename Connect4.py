# Main program 

import turtle # importing the turtle library



def print_board_circles(height, width, x, y, cursor, radio):
    
    
    cursor.penup()# levanta el cursor
    cursor.setpos (x,y)#mueve el cursor a una posicion absoluta 
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
        #distancia de separacion em horizontal, mas radio*x mas altura.
        #el + es para que crzca hacia arriba 
        cursor.pendown()#baja el lapiz para dibujarlo 
    
    # Escribe los números de las columnas.
    cursor.penup()#No pinta
    cursor.setpos(x-radio*2,y-radio) 
    cursor.pendown()#pinta
    cursor.pencolor("yellow")
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
cursor.pencolor("red") #set the colour of the cursor
cursor.speed(0) #between 1-10

# Board Properties
height = 6 #lineas
width = 7 #columnas

# Coordina donde empezar a dibujar el tablero.
x = -150
y = -150

# Radius of the pieces
radius = 19 #radio de las circumferencias 

# Prints the board in turtle
print_board_circles(height, width, x, y, cursor, radius)


""" MAIN MENU  
Here you will call the Main Menu function
"""

turtle.done() 
try:
    turtle.bye()
except:
    print("Game Over!")
