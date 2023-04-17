from turtle import *
colors = ['purple' , 'red']


pencolor('colors[0]')
penup()
goto(-200,150)
pendown()
for i in range(4):
    fd(50)
    lt(90)

pencolor('colors[1]')
penup()
goto(200,150)
pendown()
for i in range(4):
    fd(50)
    lt(90)

pencolor('colors[2]')
penup()
goto(200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(90)

pencolor('colors[3]')
penup()
goto(-200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(90)

mainloop()  
