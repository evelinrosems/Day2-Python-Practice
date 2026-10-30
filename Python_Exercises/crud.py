
students = []

# CREATE
def add_student(name, age):
    student = {
        "name": name,
        "age": age
    }
    students.append(student)
    print("Student added successfully!")


# READ
def view_students():
    print("\nStudent Records:")
    for student in students:
        print(student)


# UPDATE
def update_student(old_name, new_name):
    for student in students:
        if student["name"] == old_name:
            student["name"] = new_name
            print("Student updated successfully!")
            return

    print("Student not found!")


# DELETE
def delete_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Testing CRUD operations
add_student("Anu", 22)
add_student("Meera", 23)

view_students()

update_student("Anu", "Anjali")

view_students()

delete_student("Meera")

view_students()
