# Python dictionary examples
# Key value pair 

family = {"father": "Syed", "mother": "mother", "son": "Mike", "daughter": "Emily"}
family1 = {"father": 50, "mother": 45, "son":20, "daughter": 10}
marks_shiva = {"Maths": 90, "Science": 85, "English": 95}
marks_john = {"Maths": 80, "Science": 75, "English": 85}
Marks_students = {"shiva": marks_shiva, "John": marks_john}


# Creating a dictionary
student = {"name": "Alice","age": 21,"course": "Computer Science","marks": [85, 90, 88],"name": "mike","age": 21,"course": "Computer Science","marks": [85, 90, 88]}

print(student)





print("Student dictionary:", student)
# print("Name:", student["name"])
# print("Age:", student.get("age"))

# # Adding and updating values
# student["city"] = "New York"
# student["age"] = 22
# print("Updated student:", student)
# 
# # Removing items
# student.pop("marks")
# print("After removing marks:", student)

# # Dictionary methods
# print("Keys:", student.keys())
# print("Values:", student.values())
# print("Items:", student.items())

# # Nested dictionary example
employee = {
    "name": "Bob",
    "details": {
        "department": "IT",
        "salary": 50000,
        "children" :{"name1": "Alice", "name2": "xxx", "name3": "Mike"}
    }
}
employee["details"]["salary"] = 55000
employee.get("details").get("salary")
employee.get("details").get("children").get("name3")


# print("Department:", employee["details"]["department"])
# print("Salary:", employee["details"]["salary"])

# # Checking membership
# print("india" in student)
# print("salary" in employee)

# looping dictionary

# for keys in student.keys():
#     print(keys)

# for v in student.values():
#     print(v)

for key, value in student.items():
    print(key, 'is', value)

    # -------------------------------------------

# # Python set examples
# my_set = {1, 2, 3, 4, 5}
# print("Set:", my_set)