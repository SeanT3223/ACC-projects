# Name:Sean Triece
# COSC1336, Lab 2, 4 parts:
#   part 1: Compute MPG
#   part 2: Convert temperature
#   part 3: Stock sale
#   part 4: Draw initials using turtle graphics
#
# Part 1: Compute the mileage for a car.
#   Ask the user for all values.
#   Format mileage amounts to appear like: xx.x
#   Run at least two test cases.

print("Lab 2: Part 1: compute MPG;     Part 2: convert temp;")
print("       Part 3: stock gain/loss; Part 4: draw initials.\n")

print("This part computes gas mileage.")
# Ask for and get the vehicle make and model. These are separate items.
make = input("Enter vehicle make:")
model = input("Enter vehicle model:")
# Ask for and get the amount of miles traveled.
miles_travel = input("Enter the number of miles traveled:")
mt_f = "{:04.1f}".format(int(miles_travel))
# Ask for and get the number of gallons used.
gallons_used = input("Enter the number of gallons of gas used:")
gu_f = "{:04.1f}".format(int(gallons_used))
# Calculate the gas mileage.
Mileage = int(miles_travel) / int(gallons_used)
new_Mileage = "{:04.1f}".format(Mileage)
# Output the results.
print("Your", make, model,"traveled", mt_f,"miles using", gu_f,"gallons of gas resulting in a MPG of", new_Mileage )
# Include: vehicle make and model, miles traveled, gallons used, mileage.   
print("Drive safely.\n")



# Part 2: Convert temperature units from celsius to fahrenheit
#   Ask the user for all values.
celsius = int(input("Please provide the temperature in degrees celsius:"))
F_cel = "{:04.1f}".format(celsius)
#   Format temperature amounts to appear like: xx.x
#   Run at least two test cases.
print("This part performs a temperature unit conversion from celsius to fahrenheit.")
# Ask for and get celsius temperature
fahrenheit = (9/5)*celsius + 32
F_far = "{:04.1f}".format(fahrenheit)
# Convert celsius temperature to fahrenheit
# Display result
print("The temperature in Degrees farenheit when it is", F_cel,"degrees celsius is:",F_far,  )
 
print("Enjoy the great outdoors.\n")


# Part 3: Compute gain (or loss) on security transaction
#   Ask the user for all values (see textbook)
num_shares_purchased = float(input("Enter Number of shares purchased:"))
paid_pershare = float(input("Enter the amount paid for each share:"))
commission_percentage_bought = float(input("Enter the percentage commission given to broker when stock is purchased (do not enter percentage sign just enter percentage as a whole number):"))

num_shares_sold = float(input("Enter number of shares sold:"))
sold_pershare = float(input("Enter the rate at which you sold each share:"))
commission_percentage_sold = float(input("Enter the percentage commission given to broker when stock is sold (do not enter percentage sign just enter percentage as a whole number):"))
#   Perform stock transaction, buy and sell, show profit/loss

#   Format dollar amounts to appear like: $1,234.56
#   Run test case with this data:
#     buy 2000 shares at $40 per share, commission is 3%
#     sell 2000 shares at $42.75, commission is 3%
print ("This part computes the result of a stock transaction.")

pcad =   (commission_percentage_bought / 100)
scad = (commission_percentage_sold / 100)

purchase_total = (num_shares_purchased * paid_pershare) 
sale_total = (num_shares_sold * sold_pershare) 

net_purchase = purchase_total + pcad
net_sale = sale_total - pcad


profit_or_loss = net_sale - net_purchase

print("your stock transaction resulted in a net profit of $"+"{:.2f}".format(profit_or_loss))

print ("Buy high, sell higher, make money, spend wisely.\n")


if True: # Change False to True when ready to work on Part 4
  # Part 4: Write initials on screen using Python Turtle graphics
  #
  # Using python turtle graphics, draw initials on the screen
  # My initials are 'PT' <change this to your initials>
  #
  # Provided: Startup code that draws instructor's initials
  # Modify this startup code to draw your initials:
  #   Two letters is enough. Draw just one if it is taking too long.
  #   Use straight lines and circles
  #   Use penup to position pen, pendown to start drawing
  #   Subdivide each portion into "paragraphs"
  #   Drawing should complete within 5 seconds
  #   Drawing should be inside a box of 400 x 400 pixels
  #   Comment what you are doing

  print("This part draws my initials.")
  import turtle
  
  # Set up the screen
  screen = turtle.Screen()
  screen.setup(width=400, height=400)

  # Create a turtle instance
  turtle = turtle.Turtle()

  # Set the speed of the turtle
  turtle.speed(2)
  # Draw the letter S in block style

  turtle.penup()
  turtle.goto(-100, 0)
  turtle.pendown()
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)

  # Draw the letter T in block style
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)
  turtle.backward(100)
  # Keep the window open until it's manually closed

  screen.mainloop()

  print("End of turtle lab to draw my initials.")



# Paste your output for parts 1, 2, and 3 below:

# part 1 output 
# This part computes gas mileage.
# Enter vehicle make:chevy 
# Enter vehicle model:malibu
# Enter the number of miles traveled:15
# Enter the number of gallons of gas used:3
# Your chevy  malibu traveled 15.0 miles using 03.0 gallons of gas resulting in a MPG of 05.0
# Drive safely.
  
#part 2 output:
  
# Please provide the temperature in degrees celsius:40
# This part performs a temperature unit conversion from celsius to fahrenheit.
# The temperature in Degrees farenheit when it is 40.0 degrees celsius is: 104.0
# Enjoy the great outdoors.
  
# Please provide the temperature in degrees celsius:50
# This part performs a temperature unit conversion from celsius to fahrenheit.
# The temperature in Degrees farenheit when it is 50.0 degrees celsius is: 122.0
# Enjoy the great outdoors.
  
#Part 3 
# Enter Number of shares purchased:2000
# Enter the amount paid for each share:40
# Enter the percentage commission given to broker when stock is purchased (do not enter percentage sign just enter percentage as a whole number):3
# Enter number of shares sold:2000
# Enter the rate at which you sold each share:42.75
# Enter the percentage commission given to broker when stock is sold (do not enter percentage sign just enter percentage as a whole number):3
# This part computes the result of a stock transaction.
# your stock transaction resulted in a net profit of $5499.94
# Buy high, sell higher, make money, spend wisely.
  
#Part 4
#see turtle