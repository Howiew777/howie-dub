# three data types at input
 
# string
 phrase = input("Enter a string: ")
 print("You said " + phrase) #string concatenation
 print(f"You said {phrase}") # formatted string literal

 # float
 someFloat = float(input("Enter a float:"))
 print("You entered float: " + str(someFloat))
 print(f"You entered float: {someFloat}")

 # int
 someInt = float(input("Enter an int: "))
 print("You entered int: " + str(someInt))
 print(f"You entered int: {someInt}")

 # string interpolation is sweet
 print(f"Do Python inline, like this: {someFloat} * {someInt} = {someFloat * someInt}")