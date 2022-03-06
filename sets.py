fruits = {'Banana','Apple','papaya'}
print(fruits)
fruits.add('Guvava')
print(fruits)
fruits.remove('Apple')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
del fruits
cities = ['New Delhi','New York','New Jeresy','New Delhi']
cities_set = set(cities)
print(cities_set)
cities_fruits = fruits.union(cities_set)
print(cities_fruits)
cities_set.update(cities_fruits)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))
print(whole_numbers.difference(even_numbers))

some_numbers ={1, 2, 3, 6, 6, 4, 9}
print(whole_numbers.symmetric_difference(some_numbers))

print(some_numbers.isdisjoint(whole_numbers))

it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
age = {22,19,24,25,26,24,25,24}

#Exercise-Level-1
#1
print(len(it_companies))
#2
it_companies.add('Twitter') 
print(it_companies)
it_companies.update(['Zoho','MicroLand','Wipro','Infosys']) #3
print(it_companies)
it_companies.remove('MicroLand') #4
print(it_companies)
#5
a = {'r','e','m','o','v','e'}
b = {'d','i','s','c','a','r','d'}
print(a.difference(b))

#Exercise-Level-2
#1
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B)) #6
del A #7

#Exercise-Level-3
#1
list_to_set = set(age)
print(list_to_set)
print(len(age))
print(len(list_to_set))
#3
sentence = 'I am a teacher and I love to inspire and teach people'
print(len(sentence))
print(sentence.split())
