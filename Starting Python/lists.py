my_list = ['cat', 'bat', 'rat', 'elephant']
my_list.append('rhino')
my_list.remove('rat')

print(my_list[1])
print(my_list[0])

new_list = [ [0, 1, 3], ['a', 'b', 'c'], ['red', 'white', 'blue'] ]
print( new_list[2][0] ) #red
print( new_list [1][1] ) #[list 1][list-list 2]


print (len(my_list))
word = "fantastic"
print (len(word))

y = 0
for x in my_list:
    y += 1
    print(x)
    print(y)

for index, item in enumerate(my_list):
    print('The index: ' + str(index) + ' The item: ' + item)



water_list = ['lake', 'Ontario', 'river', 'Hudson', 'ocean', 'Atlantic']
water_list.sort()
print(water_list)


print(water_list)
['Atlantic', 'Hudson', 'Ontario', 'lake', 'ocean', 'river']
water_list.pop()
next_item = water_list.pop()
another_item = water_list.pop()
print(water_list)
['Atlantic', 'Hudson', 'Ontario']
print(next_item)
print(another_item)


my_list2 = ['cat', 'bat', 'rat']
foobar = my_list2
print(foobar)
['cat', 'bat', 'rat']
# you think you have a copy of my_list in foobar - you are wrong
my_list2.append('aardvark')
my_list2.append('zebra')
my_list2.remove('rat')
my_list2.sort()
print(my_list2)
['aardvark', 'bat', 'cat', 'zebra']
print(foobar)
['aardvark', 'bat', 'cat', 'zebra']
