
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Bangkok"
}

#create
# Empty dictionary
empty_dict = {}

# With data
person = {"name": "John", "age": 30, "city": "London"}

# Using dict()
person2 = dict(name="Jane", age=28, city="Paris")

#access
person = {"name": "John", "age": 30, "city": "London"}

print(person["name"])   # John
print(person.get("age"))  # 30
print(person.get("country", "Not Found"))  # Default value if key doesn’t exist

#add/update

person["email"] = "john@example.com"   # Add
person["age"] = 31                    # Update
print(person)

#remove
person.pop("city")       # Removes key "city"
del person["age"]        # Delete specific key
person.clear()           # Removes everything
del person               # Delete dictionary completely

#looping
person = {"name": "John", "age": 30, "city": "London"}

# Keys only
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Both keys & values
for key, value in person.items():
    print(key, ":", value)

#methods
person = {"name": "John", "age": 30, "city": "London"}

print(person.keys())     # dict_keys(['name', 'age', 'city'])
print(person.values())   # dict_values(['John', 30, 'London'])
print(person.items())    # dict_items([('name', 'John'), ('age', 30), ('city', 'London')])

person.update({"country": "UK"})  # Add/Update
print(person)

#nesting
students = {
    "A001": {"name": "Alice", "age": 20},
    "A002": {"name": "Bob", "age": 22}
}

print(students["A001"]["name"])  # Alice
