file=open("file.txt")
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open('file.txt') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

with open('file.txt', 'w') as file:
    file.write("kowshik")

with open('hi.txt', 'w') as file:
    file.write("kowshik")

with open('file.txt', 'a') as file:
    file.write("kowshik")

with open('file.txt', 'a+') as file:
    file.write("kowshik fff")
    file.seek(0)
    print(file.read())

with open('file.txt', 'w+') as file:
    file.write("kowshik fff")
    file.seek(0)
    print(file.read())