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
score = 0
# КЛАСИ _________________________________________________________
class Object(Turtle):
    def __init__(self,color,form,x_start=0,y_start=0):
        super().__init__()
        self.color(color)
        self.shape(form)
        self.penup()
        self.goto(x_start,y_start)
        self.pendown()

    def deth(self):
        global score
        global table
        screen.clear()
        table.clear()
        config()
        score +=1
        lvl()

class Player(Object):
    # Опис
    def __init__(self, color="green", form="circle", x_start=0, y_start=-350):
        super().__init__(color, form, x_start, y_start)
        self.lestening()
    # Рух після натисканеня клавіш
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
    # Детект натискання клавіш
    def lestening(self):
        # Стрілки
        screen.onkeypress(lambda: self.move("Left"), "Left")
        screen.onkeypress(lambda: self.move("Right"), "Right")
        screen.onkeypress(lambda: self.move("Up"), "Up")
        screen.onkeypress(lambda: self.move("Down"), "Down")
        # WSAD
        screen.onkeypress(lambda: self.move("Left"), "A")
        screen.onkeypress(lambda: self.move("Right"), "D")
        screen.onkeypress(lambda: self.move("Up"), "W")
        screen.onkeypress(lambda: self.move("Down"), "S")
        # wasd

        screen.onkeypress(lambda: self.move("Left"), "a")
        screen.onkeypress(lambda: self.move("Right"), "d")
        screen.onkeypress(lambda: self.move("Up"), "w")
        screen.onkeypress(lambda: self.move("Down"), "s")
        screen.listen()

class Point(Object):
    # Опис
    def __init__(self, color="orange", form="square", x_start=0, y_start=350):
        super().__init__(color, form, x_start, y_start)        

    # Реєстрація точки евакуації
    def detect(self):
        if player.xcor() == point.xcor() and player.ycor() == point.ycor():
            for i in range(5):
                print("detected")
        ontimer(self.detect,50)
            
class Barier(Object):
    # Опис
    def __init__(self, color="red", form="circle", x_start=0, y_start=0):
        super().__init__(color, form, x_start, y_start)

    # створення бар'єру 
    def draw_barier(self,x1,y1,x2,y2):
        # створення
        self.begin_fill()
        self.goto(x1,y1)
        self.goto(x2,y1)
        self.goto(x2,y2)
        self.goto(x1,y2)
        self.goto(x1,y1)
        self.end_fill()
        self.hideturtle()
        # оголошення кординат для класу
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    # Реєстрація зони смерті
    def detect(self):
        if int(player.xcor()) in range(self.x1-5,self.x2+7) and int(player.ycor()) in range(self.y2-5,self.y1+7):
            self.deth()
        update()
        ontimer(self.detect,50)

class Enemy(Object):
    def __init__(self, color="red", form="circle", x_start=450, y_start=150):
        super().__init__(color, form, x_start, y_start)
        self.mov_cor = []
    def detect(self):
        if int(player.xcor()) in range(self.xcor()-17,self.xcor()+17) and int(player.ycor()) in range(self.ycor()-17,self.ycor()+17):
            self.deth()
        update()
        ontimer(self.detect,50)


def leble():
    global table
    table = Turtle()
    table.hideturtle()
    table.penup()
    table.goto(-500,350)
    table.write(f"Death:{score}", move=False, align='left', font=('Arial', 24, 'normal')) 

def lvl():
    config()
    leble()

    global enemy
    global barier
    global point
    global player

    enemy= Enemy()
    barier = Barier()
    point = Point()
    player = Player()
    enemy.detect()
    barier.draw_barier(-400,100,400,-100)
    barier.detect()
    point.detect()
    
    update()
lvl()
done()