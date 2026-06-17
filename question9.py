file = open("student.txt", "w")

name = input("Enter Name: ")
marks = input("Enter Marks: ")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()
