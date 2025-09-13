dict={'Chaitanya':50,'ram':70}
a=input('Enter the students name: ')
if(a in dict):
    print(f"{a} marks: {dict[a]}")
else:
    print("Student not found")