print("Welcome to the Multi-Tool Program!")

while True:
  print("\n--- MAIN MENU ---")
  print("1. BMI Calculator")
  print("2. Chinese Zodiac Finder")
  print("3. Birthday Guessing Game")
  print("4. Quit")

  choice = input("Please choose an option (1-4): ")

  if choice == "1":
    print("\n--- BMI Calculator ---")
    while True:
      giris_ceki = input("Enter your weight in kg (or type 'back' to menu): ")
      if giris_ceki.lower() == "back":
        break
      try:
        weight = float(giris_ceki)
        height = float(input("Enter your height (e.g., 1.75): "))
        if height <= 0:
          print("Height cannot be zero or negative. Try again.")
          continue
        BMI = weight / (height * height)
        print(f"Your BMI result: {BMI:.2f}")
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

  elif choice == "2":
    print("\n--- Chinese Zodiac Finder ---")
    while True:
      giris = input("Enter your birth year (or type 'back' to menu): ")
      if giris.lower() == "back":
        break
      try:
        yas = int(giris)
        zodiak = yas % 12
        animals = [
            "Monkey",
            "Rooster",
            "Dog",
            "Pig",
            "Rat",
            "Ox",
            "Tiger",
            "Rabbit",
            "Dragon",
            "Snake",
            "Horse",
            "Goat",
        ]
        print(f"Your zodiac sign is: {animals[zodiak]}")
      except ValueError:
        print("Please enter a valid number!")

  elif choice == "3":
    print("\n--- Birthday Guessing Game ---")
    while True:
      start = input("Do you want to play? (yes/back): ")
      if start.lower() == "back":
        break
      if start.lower() != "yes":
        print("Please type 'yes' to play or 'back' to return.")
        continue

      set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
      set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
      set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
      set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
      set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
      birthday = 0

      sets_list = [set1, set2, set3, set4, set5]
      powers = [1, 2, 4, 8, 16]

      for i in range(5):
        print(f"\nSet {i+1}:\n", sets_list[i])
        while True:
          ans = input(
              "Is your birthday included in this set? (yes/no): "
          ).lower()
          if ans == "yes":
            birthday += powers[i]
            break
          elif ans == "no":
            break
          else:
            print("Invalid input! Please type 'yes' or 'no'.")

      print(f"\nYour birthday is: {birthday}")

  elif choice == "4":
    print("Program exited. Thank you!")
    break
  else:
    print("Invalid choice! Please enter a number between 1 and 4.")
