
def triple(value):
    return 3*value

def tripleStaf(a_list):
    new_list = map(lambda value : 3*value, a_list)
    return new_list

lst = [4,5,25]

tpl = tripleStaf(lst)
print(list(tpl))
