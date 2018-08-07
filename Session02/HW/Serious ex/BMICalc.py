weight = int(input('Please enter your weight: '))
height = int(input('Please enter your height: ')) / 100

BMI = weight / (height ** 2)

if BMI < 16:
    print("You're severly underweight")
elif BMI < 18.5:
    print("You're underweight")
elif BMI < 25:
    print("You're normal")
elif BMI < 30:
    print("You're overweight")
else:
    print("You're obese")

