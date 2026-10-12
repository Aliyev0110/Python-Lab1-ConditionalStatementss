print("Welcome to the Zodiac Sign Program!")
while True:
  giris = input("\nEnter your birth year (Type 'q' to exit): ")
  if giris.lower() == "q":
    print("Program exited. Thank you!")
    break
  try:
    yas = int(giris)
    zodiak = yas % 12
    if zodiak == 0:
      print("Your zodiac sign is: Monkey")
    elif zodiak == 1:
      print("Your zodiac sign is: Rooster")
    elif zodiak == 2:
      print("Your zodiac sign is: Dog")
    elif zodiak == 3:
      print("Your zodiac sign is: Pig")
    elif zodiak == 4:
      print("Your zodiac sign is: Rat")
    elif zodiak == 5:
      print("Your zodiac sign is: Ox")
    elif zodiak == 6:
      print("Your zodiac sign is: Tiger")
    elif zodiak == 7:
      print("Your zodiac sign is: Rabbit")
    elif zodiak == 8:
      print("Your zodiac sign is: Dragon")
    elif zodiak == 9:
      print("Your zodiac sign is: Snake")
    elif zodiak == 10:
      print("Your zodiac sign is: Horse")
    elif zodiak == 11:
      print("Your zodiac sign is: Sheep")
  except ValueError:
    print("Please enter a valid number!")
