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
            for college in colleges:
                if search_name in college['name']:
                        print(f"\nCollege Name: {college['name']}")
                        print(f"Location: {college['location']}")
                        print("Courses Offered:")
                        for course, fee in college['courses'].items():
                            print(f"fees for {course} is {fee}")
                else:
                    print(f"No colleges found with the name '{search_name}'")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Please choose correct option")
EduGuide()
