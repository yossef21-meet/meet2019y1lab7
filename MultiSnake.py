
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1500
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 100


#Initialize lists
pos_list = []
pos_list_1=[]
stamp_list = []
stamp_list_1=[]
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake_1=turtle.clone()
snake = turtle.clone()
snake.shape("square")
snake.color("green")
snake_1.shape("square")
snake_1.color("red")
turtle.bgcolor('black')
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    snake_pos_1=snake_1.pos()
    #Append the position tuple to pos_list
    pos_list.append(snake_pos)
    pos_list_1.append(snake_pos_1)
    
    #snake.stamp() returns a stamp ID. Save it in some variable         
    s_id= snake.stamp()
    s_id_1=snake_1.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(s_id)
    stamp_list_1.append(s_id_1)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snake_start in range(START_LENGTH) :
    x_pos=snake.pos()[0]#Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos_1=snake_1.pos()[0]
    y_pos_1=snake_1.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE
    x_pos_1+=SQUARE_SIZE
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
    snake_1.goto(x_pos_1,y_pos_1)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
    
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position
    old_stamp_1= stamp_list_1.pop(0) # last piece of tail
    snake_1.clearstamp(old_stamp_1) # erase last piece of tail
    pos_list_1.pop(0) # remove last piece of tail's position
    


snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

def down():
    snake.direction="Down" #Change direction to up
    print("You pressed the down key!")

def left():
    snake.direction="Left" #Change direction to up
    print("You pressed the left key!")

def right():
    snake.direction="Right" #Change direction to up
    print("You pressed the right key!")

def w():
    snake_1.direction="Up" #Change direction to up
    print("You pressed the up(w) key!")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

def s():
    snake_1.direction="Down" #Change direction to up
    print("You pressed the down(s) key!")

def a():
    snake_1.direction="Left" #Change direction to up
    print("You pressed the left(a) key!")

def d():
    snake_1.direction="Right" #Change direction to up
    print("You pressed the right(d) key!")
    

turtle.onkeypress(up, "Up") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.onkeypress(up, "W") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.onkeypress(down, "S")
turtle.onkeypress(left, "A")
turtle.onkeypress(right, "D")

turtle.listen()

turtle.register_shape("ap.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("ap.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
        ####WRITE YOUR CODE HERE!!
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    food.hideturtle()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    my_pos_1=snake_1.pos()
    x_pos_1=my_pos_1[0]
    y_pos_1=my_pos_1[0]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    if snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)

    if snake_1.direction == "Up":
        snake_1.goto(x_pos_1, y_pos_1+ SQUARE_SIZE)
    elif snake_1.direction=="Down":
        snake_1.goto(x_pos_1, y_pos_1 - SQUARE_SIZE)
    

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    if snake_1.direction=="Left":
        snake_1.goto(x_pos_1-SQUARE_SIZE,y_pos_1)
    elif snake_1.direction=="Right":
        snake_1.goto(x_pos_1+SQUARE_SIZE,y_pos_1)

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        remove_tail()
        #HINT: This if statement may be useful for Part 8
    if snake_1.pos() in food_pos:
        food_index=food_pos.index(snake_1.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        remove_tail()   
    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()


    

    #remove the last piece of the snake (Hint Functions are FUN!)
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    new_pos_1 = snake_1.pos()
    new_x_pos_1 = new_pos_1[0]
    new_y_pos_1 = new_pos_1[1]
     # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <=LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()

    if len(food_stamps) <= 6 :
        make_food()

    if (new_x_pos,new_y_pos) in pos_list[:-1]:
        print("you are a loser")
        quit()
    
            
    turtle.ontimer(move_snake,250)


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
    food_s=food.stamp()
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append((food_x, food_y))
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamps.append(food_s)


move_snake()
















turtle.mainloop() 

