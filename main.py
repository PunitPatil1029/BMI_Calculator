
print("=" * 40)
print("          BMI CALCULATOR")
print("=" * 40)

print("Welcome to BMI Calculator!")

try:
    name = input("Enter your name: ")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Error: Enter positive weight and height.")

    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            message = "You may need to improve your nutrition."

        elif bmi < 25:
            category = "Normal"
            message = "Your BMI is within the normal range."

        elif bmi < 30:
            category = "Overweight"
            message = "Consider healthy lifestyle habits."

        else:
            category = "Obese"
            message = "Consider consulting a healthcare professional."

        print("\n" + "=" * 40)
        print("              BMI RESULT")
        print("=" * 40)

        print("Name:", name)
        print("Weight:", weight, "kg")
        print("Height:", height, "m")
        print("BMI:", f"{bmi:.2f}")
        print("Category:", category)
        print("Message:", message)

        print("=" * 40)

except ValueError:
    print("Error: Please enter valid numeric values!")

