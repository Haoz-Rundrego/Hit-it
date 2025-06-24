from turtle import*
from random import*
from time import*

# конфіг
def config():
    global screen
    screen = Screen() # об'єкт екрану
    screen.tracer(0) #виключення авто оновлень
    screen.listen() #прослуховування клавіш і мишки
    screen.bgcolor("#69FFE6") #фон колір
    screen.setup(width=1200, height=800, startx=0, starty=0) #задає розмір екрану
    screen.cv._rootwindow.resizable(False, False) 
config()

# додаткові ресурси
class Runnum():
    def rnum(self,x,y):
        return randint(x,y)   
run = Runnum()

# КЛАСИ _________________________________________________________
class Object(Turtle):
    def __init__(self,color,form,x_start=0,y_start=0):
        super().__init__()
        self.color(color)
        self.shape(form)
        self.penup()
        self.goto(x_start,y_start)
        self.pendown()

    def move(self, direct):
        lab = 5
        if direct == "Left":
            self.setx(self.xcor()-lab) 
        elif direct == "Right":
            self.setx(self.xcor()+lab)
        elif direct == "Up":
            self.sety(self.ycor()+lab)
        elif direct == "Down":
            self.sety(self.ycor()-lab) 
        update()

    def lestening(self):
        screen.onkeypress(lambda: box.move("Left"), "Left")
        screen.onkeypress(lambda: box.move("Right"), "Right")
        screen.onkeypress(lambda: box.move("Up"), "Up")
        screen.onkeypress(lambda: box.move("Down"), "Down")


box = Object("green","circle")
box.lestening()



done()