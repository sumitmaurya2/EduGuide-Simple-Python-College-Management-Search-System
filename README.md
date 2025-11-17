# EduGuide-Simple-Python-College-Management-Search-System
A beginner-friendly Python program that allows users to add college details (name, location, and courses with fees) and search for colleges interactively using a console-based interface.


# 🎓 EduGuide – Python College Management & Search System

EduGuide is a simple and interactive **console-based Python application** that allows users to:

- Add colleges with their location
- Add multiple courses with fee details
- Search for colleges by name
- View college details and available courses instantly

This project is perfect for beginners learning Python, loops, dictionaries, and list handling.

---

## 🚀 Features

### ✅ **Add Colleges**
Users can input:
- College Name  
- Location  
- Unlimited courses with fee structure

### 🔍 **Search Colleges**
Search any college by name (partial name supported) and display:
- College name  
- Location  
- Courses & fees  

### 🧹 **Simple Menu System**
Easy-to-understand menu-based navigation:
- Option 1 → Add College  
- Option 2 → Search College  
- Option 3 → Exit  

---

## 🧩 Code Structure

```python
def EduGuide():
    colleges = []
    while True:
        print("Choose the correct option : ")
        print("1 for Adding College")
        print("2 for Search College")
        print("3 for Exit")
        choice = input("Enter your choice : ")
        if choice == '1':
            college_name = input("Enter college name: ").title()
            courses = {}
            while True:
                course_name = input("Enter course name or done for finish : ").title()
                if course_name == 'Done':
                    break
                else:
                    fee = float(input(f"Enter the fee for {course_name}: "))
                courses[course_name] = fee
            location = input("Enter the location of the college: ").title()
            colleges.append({
                "name": college_name,
                "courses": courses,
                "location": location
            })
            print(f"College '{college_name}' added successfully!")
        elif choice == '2':
            search_name = input("Enter the college name to search: ").title()
            found = False
            for college in colleges:
                if search_name in college['name']:
                    found = True
                    print(f"\nCollege Name: {college['name']}")
                    print(f"Location: {college['location']}")
                    print("Courses Offered:")
                    for course, fee in college['courses'].items():
                        print(f"Fees for {course}: {fee}")
            if not found:
                print(f"No colleges found with the name '{search_name}'")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Please choose correct option")

EduGuide()
