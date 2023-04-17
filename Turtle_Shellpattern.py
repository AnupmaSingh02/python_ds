from turtle import *
pencolor('black')
pensize(3)
fillcolor('pink')
bgcolor('gray')
speed('fast')
for i in range(10 , 0 , -1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
mainloop()    