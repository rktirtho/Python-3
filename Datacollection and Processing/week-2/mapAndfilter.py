
def triple(value):
    return 3*value

def tripleStaf(a_list):
    new_list = map(lambda value : 3*value, a_list)
    return new_list


def evenList(a_list):
    newList = list(filter(lambda value : value%2==0, a_list))
    return newList

def oddList(a_list):
    new_list = filter(lambda value : value%2==1, a_list)
    return new_list

lst = [4,5,25,6,47,42,67,85,35,2,16,7]

tpl = tripleStaf(lst)
even = evenList(lst)
odd = oddList(lst)
print(list(tpl))
print(list(odd))
print(even)
