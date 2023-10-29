import turtle 
import os
import math # math module for more advanced calculations
import random # random module
import winsound # import program to import wav files 

wn = turtle.Screen() # call in turtle screen
wn.bgcolor("black") # set background to black
wn.title("Space Invaders") # window title
wn.bgpic("space_invaders_background.gif") # set window background
# window setup

turtle.register_shape("invader.gif") # import gif file for alien
turtle.register_shape("player.gif") # import gif file for spaceship

border_pen = turtle.Turtle() # call in turtle to build border
border_pen.speed(0) # set speed of border to 0 
border_pen.color("white") # set border color
border_pen.penup()
border_pen.setposition(-300,-300) # set position of border
border_pen.pendown()
border_pen.pensize(3)

for k in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
# border setup

score = 0 # set score to 0
score_pen = turtle.Turtle() # call in turtle to make a score counter
score_pen.speed() # set score speed to 0 
score_pen.color("white") # set score display to white
score_pen.penup()
score_pen.setposition(-290,280) # set position for score
scorestring = "Score: %s" %score # set string to display the score
score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()

spaceship = turtle.Turtle()
spaceship.color("blue") # set color for spaceship
spaceship.shape("player.gif") # set shape of spaceship
spaceship.penup()
spaceship.speed(0) 
spaceship.setposition(0,-250) # set position of spaceship
spaceship.setheading(90)


ship_speed = 15 # set speed of spaceship
# spaceship setup

num_of_aliens = 7 # choose number of aliens
aliens = [] # create empty list of aliens
for j in range(num_of_aliens): 
    aliens.append(turtle.Turtle())

for alien in aliens:    
    alien.color("red") # set alien color
    alien.shape("invader.gif") # set shape of alien
    alien.penup()
    alien.speed(0)
    g = random.randint(-200,200)
    h = random.randint(100,250)
    alien.setposition(g,h)

alienspeed = 2
# alien setup

laser_ar = turtle.Turtle()
laser_ar.color("green") # set color of laser
laser_ar.shape("triangle") # set shape of laser
laser_ar.penup()
laser_ar.speed(0)
laser_ar.setheading(90)
laser_ar.shapesize(0.5,0.5)
laser_ar.hideturtle()
laserar_speed = 16 # set speed of laser
# laser weapon setup 
laserstate = "ready"
# create state for laser weapon

def move_left():
    x = spaceship.xcor()
    x-= ship_speed
    if x < -280:
        x = -280
    spaceship.setx(x)
# function for left movement with border check

def move_right():
    x = spaceship.xcor()
    x+= ship_speed
    if x > 280:
        x = 280
    spaceship.setx(x)
# function for right movement with border check

def shoot_laser():
    global laserstate
    if laserstate == ("ready"): 
       # ready state means weapon is ready to fire
      laserstate == ("fire") 
      # fire state means the weapon has let off a shot and the laser has not touched the border yet to shoot again
      m = spaceship.xcor()
      n = spaceship.ycor()
      laser_ar.setposition(m , n)
      laser_ar.showturtle()
      winsound.PlaySound("space_laser.wav", winsound.SND_ASYNC)
# function to let spaceship shoot laser

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
# function for collision between alien and laser

turtle.listen()
turtle.onkey(move_left, "Left") # control for left movement
turtle.onkey(move_right, "Right") # control for right movement
turtle.onkey(shoot_laser, "space") # control for shooting
# keyboard bindings

while True:
    
    for alien in aliens:
      x = alien.xcor()
      x+= alienspeed
      alien.setx(x)
      # movement of alien
      if alien.xcor() > 280:
        for a in aliens: # move all enemies down 
          y = alien.ycor()
          y-= 40
          a.sety(y)
        # allows alien to jump down to close the distance with player/ change direction
        alienspeed *= -1
        
      if alien.xcor() < -280:
        for a in aliens: # move all enemies down 
          y = alien.ycor()
          y-= 40
          a.sety(y)
        # allows alien to jump down to close the distance with player/ change direction
        alienspeed *= -1
        
      # defines laser state and when laser hits border, weapon is reloaded to shoot again
      if isCollision(laser_ar, alien):
      # reset laser
        laser_ar.hideturtle()
        laserstate = ("ready")
        laser_ar.setposition(0, -400)
        # reset alien
        g = random.randint(-200 , 200)
        h = random.randint(100 , 250)
        alien.setposition(g , h)
        winsound.PlaySound("Torpedo+Explosion.wav", winsound.SND_ASYNC)
      # collision check between laser and alien
        score += 10
        scorestring = "Score %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align = "left", font = ("Arial", 14, "normal"))


      if isCollision(spaceship, alien):
        spaceship.hideturtle()
        alien.hideturtle()
        print("Game Over") # prints Game Over
        winsound.PlaySound("Torpedo+Explosion.wav", winsound.SND_ASYNC)
        break # ends game
        turtle.bye()
        # collision check between ship and alien 

    y = laser_ar.ycor()
    y += laserar_speed
    laser_ar.sety(y)
    if laser_ar.ycor() > 275:
        laser_ar.hideturtle()
        laserstate = ("ready")
    # defines laser state and when laser hits border, weapon is reloaded to shoot again 
# function for moving the alien with border check


turtle.mainloop() # allows window to stay open unless close button is pressed
# calls in mainloop()



