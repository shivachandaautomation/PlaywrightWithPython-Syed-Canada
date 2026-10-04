# Python dictionary examples

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "marks": [85, 90, 88]
}

print("Student dictionary:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding and updating values
student["city"] = "New York"
student["age"] = 22
print("Updated student:", student)

# Removing items
student.pop("marks")
print("After removing marks:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Nested dictionary example
employee = {
    "name": "Bob",
    "details": {
        "department": "IT",
        "salary": 50000
    }
}

print("Department:", employee["details"]["department"])
print("Salary:", employee["details"]["salary"])

# Checking membership
print("name" in student)
print("salary" in employee)

# Python set examples
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)