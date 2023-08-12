""" Lesson One
try:
    file = open("my_file.txt")
    list_name =["Aman", "Shivam"]
    print(list_name[100])
except FileNotFoundError:
    file = open("my_file.txt", "w")
    file.write("Hello World")
except IndexError as index:
    print(f"Error: {index}")
    print(len(list_name))

else:
    content = file.read()
    print(content)
finally:
    file.close()
"""
"""
List bound error
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if height > 3:
    raise ValueError("Human height cannot be more then 3m")
else:
    bmi = height / weight ** 2
    print(bmi)

"""
pasword = {'Amazon.com': {'email': 'sg9967780426@gmail.com', 'password': 'gfi1!cea23d0jb#h'}, 'Facebook': {'email': 'sg9967780426@gmail.com', 'password': 'h0e!c$a1g#bdf'}, 'Twitter': {'email': 'sg9967780426@gmail.com', 'password': 'gfh1#d0!eaic$b'}}
print(pasword["adkdnd"])