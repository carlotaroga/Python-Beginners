import pathlib
path = pathlib.Path('foobar.txt')
path.exists()

myfile = open('temp.txt', 'w')
myfile.write('hello my little file\n')
myfile.write('goodbye my little file\n')
myfile.close()
myfile = open('temp.txt')
print( myfile.readline() )
print( myfile.readline() )
myfile.close()

myfile = open('temp.txt')
print( myfile.readlines() )
['hello my little file', 'goodbye my little file']
myfile.close()
 

with open('temp.txt', 'a') as f:
    words = "I would not like to eat any spam."
    f.write(words)

 # open a file for reading
states = open('state_data.txt')
# open a new file for writing
capitals = open('capitals.txt', 'w')
# store the result of readlines() in a variable
states_list = states.readlines()
# loop over the list that resulted from readlines()
for state in states_list:
    foo = state.split('\t')               # split the line at the tabs
    text = foo[1] + ", " + foo[0] + '\n'  # create text: capital, state
    capitals.write(text)                  # write text into the new file
# close both files
capitals.close()
states.close()
