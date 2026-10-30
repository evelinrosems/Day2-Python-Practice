
try:
    file = open("Python_Exercises/sample.txt", "r")

    content = file.read()

    print("File Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An error occurred:", e)
