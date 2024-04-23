import copy

orig_dict = {'key1': 'value1', 'key2': {'key3': 'value3'}}

# Deep copy
deep_dict = copy.deepcopy(orig_dict)

orig_dict['key2']['key3'] = 'new value'

print('Original:', id(orig_dict),orig_dict)
print('Deep Copy:', id(deep_dict),deep_dict)


# Original list
orig_list = [1, 2, [3, 4]]

# Shallow copy
shallow_list = copy.copy(orig_list)

orig_list[2][0] = 'a'

print('Original:', id(orig_list),orig_list)
print('Shallow Copy:',id( shallow_list),shallow_list)




# List
my_list = [1, 2, 3]
my_list[0] = 'a'  #listning keyingi korinishi  ['a', 2, 3]
print(my_list)

# Dictionary
my_dict = {'name': 'John', 'age': 30}
my_dict['age'] = 31  # listning ozgargandan keyingi  korinishi  {'name': 'John', 'age': 31}
print(my_dict)

# Set
my_set = {1, 2, 3}
my_set.add(4) # add orqali ozgaruvchi qoshish
print(my_set)



























