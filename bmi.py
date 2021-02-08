# bmi.py
# This program calculates your Body Mass Index (BMI).
# author: Barry Gardiner

#User is prompted to enter height and weight as a float 
# (real number i.e. 1.0) number. The users weight is divided
# by the height in metres to the power of 2. The output
# is printed to the screen. The code "{:.2f}'.format(BMI)" 
# specifies the format of the string. "2f" represents a floating
# point number to a precision of 2 decimal places. 

height = float(input("Please Enter Your Height In Centimetres:"))
weight = float(input("Please Enter Your Weight in kilograms:"))

bmi = ((weight) / ((height/100))**2)#Formula: weight (kg) / [height (m)]2

print('BMI is {:.2f}.'.format(bmi))