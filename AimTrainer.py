#!/usr/bin/env python
# coding: utf-8

# In[4]:


from graphics import *
import random
import time

win = GraphWin("Aim Trainer",1000,800)
win.setBackground("Black")

#Start Menu
def menu():
    game_name = Text(Point(500, 200), "Aim Trainer")
    game_name.setSize(15)
    game_name.setFill('green')
    game_name.draw(win)
    
    instructions_1 = Text(Point(500, 225), "This game aims to train your aim")
    instructions_1.setSize(15)
    instructions_1.setFill('green')
    instructions_1.draw(win)
    
    instructions_2 = Text(Point(500, 250), "Click the squares as fast and accurate as you can")
    instructions_2.setSize(15)
    instructions_2.setFill('green')
    instructions_2.draw(win)
    
    good_luck = Text(Point(500, 275), "Good Luck!")
    good_luck.setSize(15)
    good_luck.setFill('green')
    good_luck.draw(win)
    
    start_button = Rectangle(Point(350, 300), Point(650, 350))
    start_button.setOutline("green")
    start_button.setFill("green")
    start_button.draw(win)
    
    instructions_start = Text(Point(500, 325), "Click Here To Start")
    instructions_start.setSize(15)
    instructions_start.draw(win)
    
    #Infinite loop waiting for user to click start button
    while True:
        start = win.getMouse()
        start_x = start.getX()
        start_y = start.getY()
        
        if 350 <= start_x <= 650 and 300 <= start_y <= 350:
            game_name.undraw()
            instructions_1.undraw()
            instructions_2.undraw()
            good_luck.undraw()
            start_button.undraw()
            instructions_start.undraw()
            break

            
#Function responsible for the gameplay
def Game():
    #Variable to count the amount of squares clicked
    points = 0
    #Starts timer
    start_time = time.time()
    
    #Draws first target
    target = Rectangle(Point(50, 50), Point(75,75))
    target.setOutline("green")
    target.setFill("green")
    target.draw(win)
    
    #Moves the square and checks if it was clicked
    for i in range(1, 26):
        dx = random.randint(50, 950)
        dy = random.randint(50, 750)
       
        target.move(dx, dy) if i == 1 else target.move(dx - center_X, dy - center_Y)
        
        #Sets the time the square will appear
        timed_square = time.time() + 1
            
        #Makes the square disappear after 1 seconds
        while time.time() < timed_square:
            click = win.checkMouse()
            center_X = target.getCenter().getX()
            center_Y = target.getCenter().getY()
            
            if click != None:
                click_x = click.getX()
                click_y = click.getY()
                
        
                if center_X - 12.5 <= click_x <= center_X + 12.5 and center_Y - 12.5 <= click_y <= center_Y + 12.5:
                    points += 1
                    break
                else:
                    break
    
    #Deletes the square when the game is over
    target.undraw()
    #End timer
    end_time = time.time()
    #Calculates the time it took the user to finish the game
    final_time = round(end_time - start_time, 2)
    #Calculates the player's accuracy
    accuracy = (points / 25) * 100
    
    return final_time, accuracy
    
#Function that displays the end screen
def End_Screen(time, accuracy):
    score = Text(Point(500, 400), 'Your time is {0} seconds!\nYour accuracy is {1}%'.format(time, accuracy))
    score.setFill('green')
    score.setSize(15)
    score.draw(win)
    
    
def main():
    menu()
    time, accuracy = Game()
    End_Screen(time, accuracy)
    win.getMouse()
    win.close()
    
main()


# In[ ]:




