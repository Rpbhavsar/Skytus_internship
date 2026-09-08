std={"Ronit":95,
     "kunal":85,
     "Hem":90
    }
print(std)

std["Amit"]=90
print(std)

del std["kunal"]
print(std)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)

if "Ronit" in std:
    print("key exist")
else:
    print("key don't exist")


text = "apple banana apple mango banana apple"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

marks = {
    "Ronit": 85,
    "Rahul": 78,
    "Amit": 90
}

maximum = max(marks, key=marks.get)
print(maximum)

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

reverse = {}
for key, value in d.items():
    reverse[value] = key

print(reverse)

students = {
    "Ronit": 85,
    "Rahul": 78
}

students["Ronit"] = 95
print(students)

lst = [
    ("a", 1),
    ("b", 2),
    ("c", 3)
]

d = dict(lst)
print(d)

def interest(p,r,t):
    si=(p*r*t)/100
    return si
print(interest(10000,5,4))

