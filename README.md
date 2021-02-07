# Project 01
This program is based off of FPS aim trainers like KovaaK 2.0 and Aim Lab. Except Aim Trainer is in 2D while the other games are 3D. 
Once you click the start button squares will start to appear and you have 1 second to click on them before they disappear and the 
next square appears in a random place. After you go through 25 squares you will see how much time it took you to complete the game and your accuracy
based on how many squares you clicked.
\n*** This game uses classes to work ***

# Algorithm
This game draws one 25x25 rectangle and then moves the rectangle around on the screen. Instead of undrawing it and drawing a new rectangle. 
Once the rectangle appears the user has 1 second to click on the rectangle if the user doesn't click on the rectangle it moves to a new position.
If the user does click on the rectangle it immediately moves to a new position. If the user clicks the screen the program will verify if it was 
inside the rectangle if it was it will add a point. If the user doesn't click the screen at all the rectangle will keep moving after 1 second passes.
Once it has moved 25 times the program will undraw the rectangle and calculate the user's time and accuracy and display it on the screen.
