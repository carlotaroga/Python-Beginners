new_dict = {}
new_dict['name'] = 'Mahatma Gandhi'
new_dict[2] = 'India'
new_dict[3.14] = 'chakras'
new_dict['number'] = 108
new_dict['one'] = 1
print(new_dict)

keys_list = list(dict.keys())
values_list = list(dict.values())



import csv

# open a CSV file
# note - the CSV must have column headings in top row
datafile = open("sample.csv", newline='')

# create a dictReader object
my_reader = csv.DictReader(datafile)

for row in my_reader:
    print(row['Year'], row['Author'], row['Title'])

datafile.close()