
from graphics import *
import random
import time

class Menu1:
    def __init__(self, win):
        self.game_name = Text(Point(500, 200), "Aim Trainer")
        self.game_name.setSize(15)
        self.game_name.setFill('green')
        self.game_name.draw(win)
    
        self.instructions_1 = Text(Point(500, 225), "This game aims to train your aim")
        self.instructions_1.setSize(15)
        self.instructions_1.setFill('green')
        self.instructions_1.draw(win)
    
        self.instructions_2 = Text(Point(500, 250), "Click the squares as fast and accurate as you can")
        self.instructions_2.setSize(15)
        self.instructions_2.setFill('green')
        self.instructions_2.draw(win)
    
        self.good_luck = Text(Point(500, 275), "Good Luck!")
        self.good_luck.setSize(15)
        self.good_luck.setFill('green')
        self.good_luck.draw(win)

        self.start_button = Rectangle(Point(350, 300), Point(650, 350))
        self.start_button.setOutline("green")
        self.start_button.setFill("green")
        self.start_button.draw(win)
    
        self.instructions_start = Text(Point(500, 325), "Click Here To Start")
        self.instructions_start.setSize(15)
        self.instructions_start.draw(win)

    def start(self, win):
        #Infinite loop waiting for user to click start button
        while True:
            start = win.getMouse()
            start_x = start.getX()
            start_y = start.getY()
        
            if 350 <= start_x <= 650 and 300 <= start_y <= 350:
                self.game_name.undraw()
                self.instructions_1.undraw()
                self.instructions_2.undraw()
                self.good_luck.undraw()
                self.start_button.undraw()
                self.instructions_start.undraw()
                break

    def endscreen(self, win, time, accuracy):
        score = Text(Point(500, 400), 'Your time is {0} seconds!\nYour accuracy is {1}%'.format(time, accuracy))
        score.setFill('green')
        score.setSize(15)
        score.draw(win)


class Game:
    def __init__(self):
        #Variable to count the amount of squares clicked
        self.points = 0
        #Starts timer
        self.start_time = time.time()
    
        #Draws first target
        self.target = Rectangle(Point(50, 50), Point(75,75))
        self.target.setOutline("green")
        self.target.setFill("green")

    def gameplay(self, win):
        center_X = 0
        center_Y = 0
        self.target.draw(win)
        #Moves the square and checks if it was clicked
        for i in range(1, 26):
            dx = random.randint(50, 950)
            dy = random.randint(50, 750)
       
            self.target.move(dx, dy) if i == 1 else self.target.move(dx - center_X, dy - center_Y)
        
            #Sets the time the square will appear
            timed_square = time.time() + 1
            
            #Makes the square disappear after 1 seconds
            while time.time() < timed_square:
                click = win.checkMouse()
                center_X = self.target.getCenter().getX()
                center_Y = self.target.getCenter().getY()
            
                if click != None:
                    click_x = click.getX()
                    click_y = click.getY()
                
        
                    if center_X - 12.5 <= click_x <= center_X + 12.5 and center_Y - 12.5 <= click_y <= center_Y + 12.5:
                        self.points += 1
                        break
                    else:
                        break
        
        
    def endgame(self):
        #Deletes the square when the game is over
        self.target.undraw()
        #End timer
        end_time = time.time()
        #Calculates the time it took the user to finish the game
        final_time = round(end_time - self.start_time, 2)
        #Calculates the player's accuracy
        accuracy = (self.points / 25) * 100
    
        return final_time, accuracy


def main():
    win = GraphWin("Aim Trainer",1000,800)
    win.setBackground("Black")

    m = Menu1(win)
    m.start(win)
    aimtrain = Game()
    aimtrain.gameplay(win)
    time, accuracy = aimtrain.endgame()
    m.endscreen(win, time, accuracy)
    win.getMouse()
    win.close()
    
main()




