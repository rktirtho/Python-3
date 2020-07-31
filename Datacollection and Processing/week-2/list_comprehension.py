

lst = [4,5,25,6,47,42,67,85,35,2,16,7]

new_list = [value *2 for value in lst]
evens = [value for value in lst if value%2==0]
new_quad = [i+2 for i in lst]


odds =  [i*3 for i in lst if i%2==1]



print(new_list)
print(new_quad)
print(evens)
print(odds)
