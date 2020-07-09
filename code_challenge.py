
'''
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''

#iterate over each element list
#find min of each list
    # iterate of each item and 
#add min to a new list
#sum that new list

def sum_of_min(list):
    list_of_min = []
    for element in list:
        min_of_element = None
        for num in element:
            if min_of_element == None:
                min_of_element = num
            elif num < min_of_element:
                min_of_element = num
        list_of_min.append(min_of_element)
    sum_of_list = None
    for num in list_of_min:
        sum_of_list += num
    return sum_of_list

print(sum_of_min([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]))