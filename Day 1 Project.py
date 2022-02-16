#1. Create a greeting for your program.
print("Hello! Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
birth_city = input("Tell me, what beautiful city did you grow up in?\n")
#3. Ask the user for the name of a pet.
petname = input("Now, tell me the name of your favorite furbaby. It doesn't have to be your own!\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your cool new bandname could be " + birth_city + " " + petname + "!!")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/


##comment: On line 8, I forgot to account for the " " between the birth_city & petname, which resulted in these variables concatenating unnecessarily.