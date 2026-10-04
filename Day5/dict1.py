# Creating a dictionary
#dictionay dont accect duplicates 
student = {"name": "Alice","age": 21,"course": "Computer Science","marks": [85, 90, 88],"name1": "mike","age1": 21,"course1": "Computer Science","marks1": [85, 90, 88]}

students = {"student1": {"name": "Alice", "age": 21, "course": "Computer Science", "marks": [85, 90, 88]}, 
            "student2": {"name": "Mike", "age": 22, "course": "Mathematics", "marks": [80, 85, 90]}}
# print("Students dictionary:", students)
# print(students)

family = {"father": "Syed", "mother": "mother", "son": "Mike", "daughter": "Emily"}

# print(family["father"])
# print(family.get("father"))
# print(family["mother"])
# print(family.get("mother"))
# print(family["son"])
# print(family["daughter"])

# family["daughter2"] = "Emily2"
# print(family)
# family["son"] = "Mike2"
# print(family)
# family.pop("daughter2")
# print(family)

# print(family.keys())
# print(family.values())
print(family.items())


