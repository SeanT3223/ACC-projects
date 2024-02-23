#
# Many of the labs in this course have many parts. Each part can be developed
# in a separate file, and later combined into one large script. This makes it
# easier to test each part separately, and later have all the parts in one file.
#
# This python script is an example showing how to create a multiple option
# selection structure. It is useful to combine a large number of small
# blocks of python code into one large python script, with the option
# to jump to any one of the desired blocks of code.
#

print('Welcome to the multiple option selection script. Here are your options:\n'
      '1)Part 1   2)Part 2   3)Part 3  4)part 4  5)Part 5')
option = int(input('Which option do you want (1,2,3,4, or 5) ? '))
# The option could be a string, type str, such as north south east west
# The option could be a digit, which is a string, type str, such as 1 2 3
# If needed, the option could be converted from str into int, float, etc.
# Here, the option is 1 2 or 3 and is left as a string, type str.
# For a more clear user interface, the print statements in the options
# are indented a little.

if option == 1:
  print('  You have chosen Part 1.')
  print("Go to the window.")
  print("Read thermometer")
  temp = int(input("Enter the integer farenheit value:"))

  if temp < 50:
    print("Wear a coat.")
  print("Open the door.")
  rain = input("Is it raining (y/n)")
  rain.lower()
  if rain == "y":
    print("Bring an umbrella")

  print("Go outside.")
  print("End")

  print('  end of Part 1')
  
elif option == 2:
  print('  You have chosen Part 2.')
  print("Start Raid")
  print("Go to bridge")
  state_of_bridge = input("Is bridge intact (y/n)?")
  state_of_bridge.lower()
  if state_of_bridge == "y":
      print("Cross bridge")
  else:
    fins = input("Do your have diving fins (y/n)?")
    fins.lower()
    if fins == "y":
      print("Put on fins")
    print("swim across river")
  print("Go to warehouse and grab loot")
  print("Escape")
    
  print('  end of Part 2')
  
elif option == 3:
  print('  You have chosen Part 3.')
  playerA = input("playerA select Rock,Paper, or Scissors (r/p/s)")
  playerB = input("playerB select Rock,Paper, or Scissors (r/p/s)")
  playerA.lower()
  playerB.lower()
  if playerA != "r" and playerA != "p" and playerA != "s":
    playerA = "r"
  if playerB != "r" and playerB != "p" and playerB != "s":
    playerB = "r"
  if playerA == playerB:
    print(f"playerA ties playerB because {playerA} equals {playerB}")
  else:
      if playerA == "r" and playerB == "s" or playerA =="p" and "playerB" == "r" or playerA =="s" and playerB == "p":
        print(f"playerA beats playerB because {playerA} beats {playerB}")
      else: 
        print(f"playerB beats playerA because {playerB} beats {playerA}")
  print('  end of Part 3')

elif option == 4:
  print(' you have chosen Part 4. ')
  num = int(input("Enter a number from 1 to 4:"))

  if 0 < num < 5:
    if num == 1:
      print("Winter is White")
    elif num == 2:
      print("Spring is in bloom")
    elif num == 3:
      print("Summer is dry")
    elif num == 4:
      print("Fall is beautiful")
  else: 
    print("Error number out of season range!")

  print(' end of Part 4 ')

elif option == 5:
  print(' you have chosen Part 5. ')
  battery_charged=True
  got_car=True
  drunk=False
  gas=2  # (gallons) # gas currently in the tank of the car
  distance=100 # miles from home
  mpg=35 # miles per gallon expected to be used driving home
  nighttime=False
  headlights_out=True

  distance_possible = gas * mpg
  can_drive = None

  if battery_charged == False or got_car == False or drunk == True or distance > distance_possible or nighttime == True and headlights_out == True:
    can_drive = False
  else: 
    can_drive = True

  if can_drive:
    print("Drive home")
  else: 
    print("Do not drive home")

  print(' end of Part 5 ')
else:
  print('  You did not chose a valid option.')
  print('  statements for none-of-the-above go here...')
  print('  end of none-of-the-above')

print('Good bye.')


##Welcome to the multiple option selection script. Here are your options:
##1)Part 1   2)Part 2   3)Part 3
##Which option do you want? 2
##  You have chosen Part 2.
##  statements for part 2 go here...
##  end of Part 2
##Good bye.



#test part 1
# Go to the window.
# Read thermometer
# Enter the integer farenheit value:60
# Open the door.
# Is it raining (y/n)y
# Bring an umbrella
# Go outside.
# End

#test part 2
# Start Raid
# Go to bridge
# Is bridge intact (y/n)?y
# Cross bridge
# Go to warehouse and grab loot
# Escape

#test Part 3
# playerA select Rock,Paper, or Scissors (r/p/s)r
# playerB select Rock,Paper, or Scissors (r/p/s)s
# playerA beats playerB because r beats s

#test part 4
# Enter a number from 1 to 4:3
# Summer is dry

#test part 5
# Do not drive home