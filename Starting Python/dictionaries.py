new_dict = {}
new_dict['name'] = 'Mahatma Gandhi'
new_dict[2] = 'India'
new_dict[3.14] = 'chakras'
new_dict['number'] = 108
new_dict['one'] = 1
print(new_dict)

print("imprimir las claves del diccionario")
for key in new_dict.keys():
    print(key)

print("imprimir las valores del diccionario")
for value in new_dict.values():
    print(value)

print("imprimir las claves y los valores del diccionario")
for key, value in new_dict.items():
    print(key, value)


keys_list = list(new_dict.keys())
print(keys_list)
values_list = list(new_dict.values())
print(values_list)


import csv
# open a CSV file
# note - the CSV must have column headings in top row
datafile = open("sample.csv", newline='')

# create a dictReader object
my_reader = csv.DictReader(datafile)

for row in my_reader:
    print(row['Year'], row['Author'], row['Title'])

datafile.close()