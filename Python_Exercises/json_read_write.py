
import json

# Student data
student = {
    "name": "Anu",
    "age": 22,
    "course": "MCA",
    "college": "LEAD College"
}

# WRITE JSON data into a file
with open("Python_Exercises/students.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")

# READ JSON data from the file
with open("Python_Exercises/students.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("College:", data["college"])
