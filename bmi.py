#bmi calculator
def calculate_bmi(weight, height):

    bmi= weight / (height ** 2)
    print("Your BMI is:",bmi)

    if bmi < 18.5:
        print("Underweight") 

    elif 18.5 <= bmi < 24.9:
        print("Normal weight")

    elif 25 <= bmi < 29.9:
        print( "Overweight")
    
    else:
        print("Obesity")


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
        
if weight <= 0 or height <= 0:
     print("Weight and height must be positive numbers.")
   
calculate_bmi(weight, height)

   
