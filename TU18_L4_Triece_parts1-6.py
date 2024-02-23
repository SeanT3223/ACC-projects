#Sean Triece
#TU18 Programming Fundamentals I (74564)
#2/20/24

# Many of the labs in this course have many parts. Each part can be developed
# in a separate file, and later combined into one large script. This makes it
# easier to test each part separately, and later have all the parts in one file.
#
# This python script is an example showing how to create a multiple option
# selection structure. It is useful to combine a large number of small
# blocks of python code into one large python script, with the option
# to jump to any one of the desired blocks of code.
#
# In addition to allowing the user to select from several options, it is useful
# to allow the user to keep selecting from multiple options until the user is done
# with the program. This can be done by enclosing a multiple selection option in a
# loop. There must always be an option available to quit the loop!
#

print('Welcome to the looping multiple option selection script.')
looping = True
while looping:
  print('Here are your options: 1)boxes   2)triangles   3)temps  4)prime  5)design  6)quit   Q)Quit')
  option = input('Which option do you want? ')
  # The option could be a string, type str, such as north south east west
  # The option could be a digit, which is a string, type str, such as 1 2 3
  # If needed, the option could be converted from str into int, float, etc.
  # Here, the option is 1 2 or 3 and is left as a string, type str.
  # For a more clear user interface, the print statements in the options
  # are indented a little.

  if option == '1':
    print('  You have chosen Part 1.')
    #a
    box_size = 1

    while box_size != 0:
        box_size = int(input("Enter a box size or enter 0 to exit:"))
        for i in range(box_size):
            print("*"*box_size)
        print("\n")
    print("Exiting Program")



    #b
    box_size = 1

    while box_size != 0:
        box_size = int(input("Enter a box size or enter 0 to exit:"))
        if box_size % 2 == 0:
            for i in range(box_size):
                print("*"*box_size)
            print("\n")
        else:
            for i in range(box_size):
                if i == 0 or i == box_size-1:
                    print("*"*box_size)
                else:
                    print("*"+" "*(box_size-2)+"*")

    print('  end of Part 1')
    print()
    
  elif option == '2':
    print('  You have chosen Part 2.')
    #a
    triangle_size = 1
    while triangle_size != 0:
        triangle_size = int(input("Enter a triangle size or enter 0 to exit:"))
        for i in range(triangle_size + 1):
            print("*"*i)

    print("Program Exiting")
    #b
    triangle_size = 1


    triangle_size = int(input("Enter a triangle size or enter 0 to exit:"))
    for p in range(0,triangle_size+1,1):
        for i in range(p+1):
            print("*"*i)

    print('  end of Part 2')
    print()
    
  elif option == '3':
    print('  You have chosen Part 3.')
    #a
    temp = input("Enter a temperature or enter 'q' to quit ")
    temp_list = []

    if temp == "Q" or temp == "q":
        print("Quitting")

    else:
        temp_list.append(int(temp))
        while temp != "q":
            temp = input("Enter a temperature or enter 'q' to quit ")
            temp_list.append(temp)
        del temp_list[-1]
        for i in range(len(temp_list)):
            temp_list[i] = int(temp_list[i])
        print("Number of temperatures entered:", len(temp_list))
        print("Highest temperature:",max(temp_list))
        print("Lowest temperature:", min(temp_list))
        average = sum(temp_list,0) / len(temp_list)
        print("Average temperature:",average)
        count = 0 
        for t in temp_list: 
            if t <= 32:
                count += 1
        print("Number of freezing temperatures:",count)

        #b
        temp_list = []
        flag = True
        while flag:
            temp = input("Enter a temperature in the range of -5 to +115 or enter 'q' to quit:\n")
            if temp == "Q" or temp == "q":
                print("Stop")
                flag = False
            try:
                temp = int(temp)
                if -5 < int(temp) < 115:
                    temp_list.append(temp)
                else:
                    print("Invalid Input")
                    continue


            except:
                if temp.lower() == "q":
                    print("Stop")
                else:
                    print("Invalid input")

        if temp_list:
            print("Number of temperatures entered:", len(temp_list))
            print("Highest temperature:",max(temp_list))
            print("Lowest temperature:", min(temp_list))
            average = sum(temp_list,0) / len(temp_list)
            print("Average temperature:",average)
    print('  end of Part 3')
    print()
  elif option == '4':
    print('  You have chosen Part 4.')
    flag = False
    num = int(input("Enter a number:"))

    if num == 1:
        print(num, "is composite")
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print(num, "is composite")
        else:
            print(num, "is a prime number")
    elif num <= 0:
        print("Goodbye.")
    print('  end of Part 4')
    print()
  
  elif option == '5':
    print('  You have chosen Part 5.')
    # This program draws a design using repeated circles.
    import turtle
    
    # Named constants
    NUM_CIRCLES = 36    # Number of circles to draw
    RADIUS = 100        # Radius of each circle
    ANGLE = 10          # Angle to turn
    ANIMATION_SPEED = 0 # Animation speed
    # Set the animation speed.
    turtle.speed(ANIMATION_SPEED)

      # Draw 36 circles, with the turtle tilted
      # by 10 degrees after each circle is drawn.
    for x in range(NUM_CIRCLES):     
        turtle.circle(RADIUS)
        turtle.left(ANGLE)
    print()

    print('  end of Part 5')

  elif option == '6': # this requires uppercase Q
    looping = False
    print()

  else:
    print(' ERROR: You did not choose a valid option.')
 
    

print('Good bye.')

#TESTING

#1a

# Enter a box size or enter 0 to exit:4
# ****
# ****
# ****
# ****


# Enter a box size or enter 0 to exit:3
# ***
# ***
# ***


# Enter a box size or enter 0 to exit:2
# **
# **


# Enter a box size or enter 0 to exit:1
# *


# Enter a box size or enter 0 to exit:0


# Exiting Program


#1b

# Enter a box size or enter 0 to exit:4
# ****
# ****
# ****
# ****


# Enter a box size or enter 0 to exit:3
# ***
# * *
# ***
# Enter a box size or enter 0 to exit:2
# **
# **


# Enter a box size or enter 0 to exit:1
# *
# Enter a box size or enter 0 to exit:0

#2a

# Enter a triangle size or enter 0 to exit:4

# *
# **
# ***
# ****
# Enter a triangle size or enter 0 to exit:3

# *
# **
# ***
# Enter a triangle size or enter 0 to exit:2

# *
# **
# Enter a triangle size or enter 0 to exit:1

# *
# Enter a triangle size or enter 0 to exit:0

#2b

# Enter a triangle size or enter 0 to exit:4


# *

# *
# **

# *
# **
# ***

# *
# **
# ***
# ****
# Program Exiting

#3a

# Enter a temperature or enter 'q' to quit 22
# Enter a temperature or enter 'q' to quit 78
# Enter a temperature or enter 'q' to quit -11
# Enter a temperature or enter 'q' to quit 40
# Enter a temperature or enter 'q' to quit 14
# Enter a temperature or enter 'q' to quit q
# Number of temperatures entered: 5
# Highest temperature: 78
# Lowest temperature: -11
# Average temperature: 28.6
# Number of freezing temperatures: 3

#3b

# Enter a temperature in the range of -5 to +115 or enter 'q' to quit:
# 10
# Enter a temperature in the range of -5 to +115 or enter 'q' to quit:
# -10
# Invalid Input
# Enter a temperature in the range of -5 to +115 or enter 'q' to quit:
# 100
# Enter a temperature in the range of -5 to +115 or enter 'q' to quit:
# 56
# Enter a temperature in the range of -5 to +115 or enter 'q' to quit:
# q
# Stop
# Stop
# Number of temperatures entered: 3
# Highest temperature: 100
# Lowest temperature: 10
# Average temperature: 55.333333333333336

#4

# Enter a number:7
# 7 is a prime number

#5 
 
#see code