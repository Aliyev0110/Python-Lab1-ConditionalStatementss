print("Hello, it's BMI calculator")
while True:
    giris_ceki = input("\nEnter your weight in kg (Type 'q' to exit): ")
    if giris_ceki.lower() == "q":
        print("Program exited. Thank you!")
        break
    try:
        weight = float(giris_ceki)
        height = float(input("Enter your height (for example, 1.75): "))
        if height <= 0:
            print("Height cannot be zero or negative. Please try again.")
            continue
        BMI = weight / (height * height)
        print(f"Your BMI is: {BMI:.2f}")
        if BMI < 18.5:
            print("Result: Underweight")
        elif 18.5 <= BMI < 24.9:
            print("Result: Normal Weight")
        elif 25.0 <= BMI < 29.9:
            print("Result: Overweight")
        else:
            print("Result: Obese")
    except ValueError:
        print("Please enter valid numbers only!")
