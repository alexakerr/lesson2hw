# Task One -

def create_list(n):
    list = []
    for i in range(1, n + 1):
        list.append(i**2)
    print(list)

create_list(10)

'''
Because the loop iterates 'n' times, the function's time complexity is O(n).
Given that the list can accommodate 'n' integers, the function's space complexity
is also O(n)
'''





# Task Two - 

def reverse_list(n):
    n[3].reverse()
    print(n)

list = ['a', 'b', 'c', ['a', 'b', 'c']]

reverse_list(list)

'''
Given that the function doesn't involve any iteration, its time and space complexity
are both constant, represented as O(1).
'''






# Task Three - 

def sorted_merged(lst1, lst2):
    lst3 = lst1 + lst2
    lst3.sort()
    print(lst3)

sorted_merged([1, 2, 6, 5, 4, 3, 7],[9,10,11,17,19])
sorted_merged(["Alexa","Maria","Yasmin", "Erin"],["Lilah","Remy"])

'''
The time complexity of the function above is determined entirely by the sorting operation,
which has a time complexity of O(N log n). The space complexity is influenced by the size 
of the lists being sorted and the additional temporary space required during the sorting 
process.
'''




#----------------------------------




# Task One - 

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2} 

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

print(merge_dicts(dict1, dict2))





# Task Two -

def intersection_dicts(dict_a, dict_b):
    intersection_dict = {}

    for key in dict_a:
        if key in dict_b:
            intersection_dict[key] = dict_b[key]
    return intersection_dict

dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 20, 'c': 30, 'd': 40}

print(intersection_dicts(dict_a, dict_b))



# Task Three -

def count_words(words_list):
    word_frequency = {}
    for word in words_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

words_list = ['cat', 'dog', 'cat', 'bird', 'dog', 'dog', 'cat', 'rabbit']

print(count_words(words_list))