from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'student_id'])

S = Student('Nandini', '19', '2541997')
f = Student('Jack','23','6414112')
g = Student('Anna','20','121231233')

#Student yoshi va ismlari
print("The Student age using index is : ", end="")
print(S[1])
print("The Student name using keyname is : ", end="")
print(S.name)
print("The Student id using index is : ", end="")
print(g[1])
print("The Student age using keyname is : ", end="")
print(g.name)
print("The Student name using index is : ", end="")
print(f[1])
print("The Student id using keyname is : ", end="")
print(f.name)



import collections

Student = collections.namedtuple('Student',['name', 'age', 'student_id'])

# Qiymatlarni qo'shish
S = Student('Nandini', '19', '2541997')

# iteratsiyani ishga tushirish
li = ['Manjeet', '19', '411997']

# ishga tushirish dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# OrderedDict() ni qaytarish uchun _asdict() dan foydalanish
print("Nametuple yordamida OrderedDict misoli  : ",(S._asdict()))



Person = namedtuple("Person", "name age email")
c1 = ['Jane',25,'jane@gmail.com']
c2 = ['Nasty',20,'nasty@gmail.com']
jane = (Person._make(c1))
print(jane.age)
nasty = (Person._make(c2))
print(nasty.name)




import collections
Student = collections.namedtuple('Student', ['name', 'age', 'student_id'])

# O'zgaruvchilar qo'shish
S = Student('Nandini', '19', '2541997')

print("Talabalarga tegishli malumotlar  : ",(S._fields))






























