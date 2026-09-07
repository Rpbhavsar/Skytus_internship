tuple = ('1', '2', '3', '4', '5')

print(tuple[3])

# unpack tuple
a, b, c, d, e = tuple
print(a)
print(b)
print(c)
print(d)
print(e)

fruits={'banana','apple','melon','strawberry','grapes'}
print(fruits)
fruits.add('papaya')
print(fruits)
fruits.remove('strawberry')
print(fruits)

a={1,2,3}
b={3,4,5}
print(a.union(b))

print(a.intersection(b))

print (a.issubset(b))

lst = [1, 2, 2, 3, 3, 4, 5, 5]
s = set(lst)
print(s)