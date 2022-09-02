my_list = [44,4345,435,4565,6768,23]

count = 0

for i in range(len(my_list)):
    if(my_list [i]%2 == 0):
        count += 1

print("Even elements in the list are: ",count)
