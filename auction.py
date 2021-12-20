from replit import clear
logo = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡾⠏⠩⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡿⠛⠁⢀⣀⣀⡈⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⣀⣠⣴⡾⠟⠋⠁⣠⣴⣾⣿⠿⢿⣿⣷⣄⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠈⠻⢿⣿⣦⡀⠈⢻⣿⣷⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠙⠿⣿⣶⣿⣿⡿⠁⠀⢀⣌⣛⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⠿⢻⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣦⡀⠀⠀⣀⣤⡈⠻⠿⠋⠁⣀⠴⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣾⡿⠟⠋⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣶⣬⣻⣿⣿⣶⣿⣿⠟⠋⠀⣠⣴⣷⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⠴⠚⠉⠁⠀⣀⣀⡀⠀⠀⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠁⣠⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣾⣿⠛⠀⠀⣠⣶⡦⠾⣿⠟⠃⠀⠈⢸⣿⣿⣍⣉⣩⣿⣿⡟⠛⢿⣿⣿⣿⣾⣟⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣦⠀⠀⣿⣿⣤⣤⣶⣶⣿⣷⣦⡀⠙⠿⣿⣻⡿⠟⠉⢀⣠⣴⣿⠿⢻⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⢿⣆⠀⠙⠿⠿⠿⠟⠛⠛⣿⣿⡿⠀⠀⠀⠀⢀⣤⣾⣿⠟⠋⠀⠀⠀⠈⠙⠻⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢻⡷⠀⢀⣴⣾⢶⣶⣶⣿⡿⠃⠀⢀⡀⢈⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⣰⡄⠙⠛⠻⠟⠋⠉⢀⣤⣶⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣆⠀⠀⣀⣤⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

#declare the dictionary like global variable
auction = {}

#use while loop to keep getting the bitter
while True:
  print(logo)
  #use the input to get name and bit value and add in auction dictionary
  name = input("what is your name? ")
  bit = int(input("what is your bit? "))
  auction[name] = bit
  answer = input("Are there any more person want to bit? ")
  if answer == "Yes":
    clear()
  else:
    break

#using loop to get highest bit in dictionary and person name with highest bit
max = 0
person_win =''
for person in auction:
  if max < auction[person]:
    max = auction[person]
    person_win = person

print(auction)
print(f"{person_win} has highest bit with ${max}")


