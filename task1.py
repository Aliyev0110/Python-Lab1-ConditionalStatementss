print("Welcome to the Birthday Guessing Game!")
while True:
  start = input("\nDo you want to play? (Type 'quit' to exit): ")
  if start.lower() == "quit":
    print("Program exited. Thank you!")
    break
  set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
  set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
  set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
  set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
  set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
  birthday = 0
  print("\nSet 1:\n", set1)
  ans1 = input("Is your birthday included in this set? (yes/no): ")
  if ans1.lower() == "yes":
    birthday += 1
  print("\nSet 2:\n", set2)
  ans2 = input("Is your birthday included in this set? (yes/no): ")
  if ans2.lower() == "yes":
    birthday += 2
  print("\nSet 3:\n", set3)
  ans3 = input("Is your birthday included in this set? (yes/no): ")
  if ans3.lower() == "yes":
    birthday += 4
  print("\nSet 4:\n", set4)
  ans4 = input("Is your birthday included in this set? (yes/no): ")
  if ans4.lower() == "yes":
    birthday += 8
  print("\nSet 5:\n", set5)
  ans5 = input("Is your birthday included in this set? (yes/no): ")
  if ans5.lower() == "yes":
    birthday += 16
  print(f"\nYour birthday is: {birthday}")
