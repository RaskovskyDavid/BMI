# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

imc = weight/(height**2)
if imc <= 18.5:
  print("You are Under the normal weight")
elif imc <= 25:
  print("You are in a normal weight")
elif imc <= 30:
  print("You are overweight")
elif imc <= 35:
  print("You are obese")
elif imc > 35:
  print("You are clinically obese")
else:
  print("try again")
print("Your BMI" + str(round(imc,2)))




