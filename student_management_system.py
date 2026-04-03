#student management system 
FILENAME = "students.txt"
def load_students():
    students = {}
    try:
        with open(FILENAME,"r")as file:
            for line in file :
                name,marks = line.strip().split(",")
                students[name] = float(marks)
    except FileNotFoundError:
        pass            
    return students

def save_students(students):
    with open(FILENAME,"w")as file:
        for name, marks in students.items():
            file.write(f"{name},{marks}\n")

def add_student(students):
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return
    try:
        marks = float(input("Enter student marks: "))
    except:
        print("Invalid marks! Please enter a number.")
        return              
    
    students[name]= marks
    save_students(students)
    print("Student added successfully!")

def show_students(students):
    if not students:
        print("No students found!")
        return
    
    print("\nStudents List:")
    for name, marks in students.items():
        print(f"{name} : {marks}")

def average_marks(students):
    if not students:
        return None 
    return sum(students.values()) /len(students)  

def find_topper(students):  
    if not students:
        return None 
    topper = max(students ,key = students.get)  
    return topper , students[topper]

def menu():
    students = load_students()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Average Marks")
        print("4. Find Topper")
        print("5. Exit")

        choice = input("Enter your choice:")

        if choice =="1":
            add_student(students)

        elif choice =="2":
            show_students(students)

        elif choice == "3":
            avg = average_marks(students)        
            if avg is None:
                print("No data available")
            else:
                print("Average Marks:",avg) 

        elif choice == "4":
            result = find_topper(students)
            if result is None:
                print("No data available")
            else:
                name , marks = result
                print(f"Topper is {name} with marks {marks}")   

        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid choice! Please try again.")

menu()                                 

