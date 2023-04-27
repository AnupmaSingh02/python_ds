# Python program for creating a digital clock using Turtle  
import time  
import datetime as dte  
import turtle  
  
# Creating a turtle for displaying time  
tt1 = turtle.Turtle()  
# Creating a turtle for creating a rectangle box  
tt2 = turtle.Turtle()  
# Creating the screen  
screen = turtle.Screen()  
# Setting the background color for the screen  
screen.bgcolor("pink")  
  
# Obtaining the current hour, minute and second from the system of the user  
secs = dte.datetime.now().second  
mins = dte.datetime.now().minute  
hrs = dte.datetime.now().hour  
tt2.pensize(3)  
tt2.color('white')  
tt2.penup()  
  
# Setting the position of the turtle  
tt2.goto(-15, -15)  
tt2.pendown()  
  
# Creating the rectangle( box)  
for j in range(2):  
   tt2.forward(200)  
   tt2.left(90)  
   tt2.forward(70)  
   tt2.left(90)  
     
# Hiding the turtle  
tt2.hideturtle()  
  
while True:  
   tt1.hideturtle()  
   tt1.clear()  
   # Displaying the generated time  
   tt1.write(str(hrs).zfill(2)  
            + ":"+str(mins).zfill(2)+":"  
            + str(secs).zfill(2),  
            font=("Callibri Narrow", 37, "bold"))  
   time.sleep(1)  
   secs += 1  
   if secs == 60:  
       secs = 0  
       mins += 1  
   if mins == 60:  
       mins = 0  
       hrs += 1  
   if hrs == 13:  
       hrs = 1  