import turtle 

  
sc = turtle.Screen() 
olive = turtle.Turtle() 
olive.speed(0)



def pixel(x, y, color):
  olive.penup()
  olive.color('black')
  if (x == 0 or y == 0):
    print("0 is not a valid argument for this function. ")
    return False 
  
  x_cord = (x-1) * 20
  y_cord = (y-1) *20
  
    
  if x < 0:
    x_cord = (x) * 20
  if y < 0:
    y_cord = (y) * 20
    
  if (x == 1):  
    x_cord = 0
  if (y == 1):  
    y_cord = 0    
    
  print(x, y)  
  olive.goto(x_cord, y_cord)
  
  olive.pendown()
  olive.fillcolor(color)
  olive.begin_fill()
  
  for i in range(4):
    olive.forward(20)
    olive.right(90)
  olive.end_fill()
  
  olive.penup()
  olive.goto(x_cord, y_cord)

def draw_grid():
  olive.goto(0,0)  
  olive.penup()
  olive.right(90)
  olive.forward(200)
  olive.left(90)
  olive.pendown()
  
  olive.forward(200)
  olive.right(180)
  olive.forward(400)
  
  for i in range(10):
    olive.penup()
    olive.right(90)
    olive.forward(20)
    olive.right(90)
    olive.pendown()
    olive.forward(400)
    
    olive.penup()
    olive.left(90)
    olive.forward(20)
    olive.left(90)
    olive.pendown()
    olive.forward(400)
  
  olive.penup()
  olive.left(90)
  olive.pendown()
  olive.forward(400)   



  
  for i in range(10):
    olive.penup()
    olive.left(90)
    olive.forward(20)
    olive.left(90)
    olive.pendown()
    olive.forward(400)
    olive.right(90)
    olive.penup()
    olive.forward(20)
    olive.right(90)
    olive.pendown()
    olive.forward(400)
    olive.penup()
  
  olive.penup()
  olive.left(90)
  olive.forward(20)
  olive.left(90)
  olive.pendown()
  olive.forward(400)
  
def draw_axis():
  olive.penup()
  olive.goto(0,0)
  olive.color("red")
  olive.pendown()
  
  for i in range(4):
    olive.forward(200)
    olive.right(180)
    olive.forward(200)
    olive.right(90)

  
def draw_grid_test(): 
  for i in range(8):
    j = -1
  #  pixel(j,i+1, 'green')
    for j in range(8): 
      pixel(j+1,i, 'green')
      




