patients = {}

while True:
    print("1. Add patient records")
    print("2. View all records")
    print("3. Modify records")
    print("4. Remove records")
    print("5. Search by any detail of patient")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        if not age.isdigit():
            print("Age must be an integer!")
            continue
        gender = input("Enter patient gender: ")
        address = input("Enter patient address: ")
        phone_number = input("Enter patient phone number: ")
        if not (phone_number.isdigit() and len(phone_number) == 10):
            print("Phone number must be a 10-digit integer!")
            continue
        blood_group = input("Enter patient blood group: ")
        disease = input("Enter patient disease: ")
        doctor_name = input("Enter doctor name:")
        patients[name] = {"Age": int(age), "Gender": gender, "Address": address, "Phone Number": phone_number, "Blood Group": blood_group, "disease": disease,"Doctor Name": doctor_name}
        print("Patient added successfully!")

    elif choice == 2:
        if patients:
            for name, patient in patients.items():
                print("Name:", name)
                for key, value in patient.items():
                    print(key + ":", value)
                print()
        else:
            print("No patients found!")

    elif choice == 3:
        name = input("Enter patient name: ")
        if name in patients:
            age = input("Enter patient age: ")
            if not age.isdigit():
                print("Age must be an integer!")
                continue
            gender = input("Enter patient gender: ")
            address = input("Enter patient address: ")
            phone_number = input("Enter patient phone number: ")
            if not (phone_number.isdigit() and len(phone_number) == 10):
                print("Phone number must be a 10-digit integer!")
                continue
            blood_group = input("Enter patient blood group : ")
            disease = input("Enter patient disease: ")
            doctor_name = input("Enter doctor name:")
            patients[name] = {"Age": int(age), "Gender": gender, "Address": address, "Phone Number": phone_number, "Blood Group": blood_group, "Disease": disease, "Doctor Name" : doctor_name}
            print("Patient details updated successfully!")
        else:
            print("Patient not found!")

    elif choice == 4:
        name = input("Enter patient name: ")
        if name in patients:
            del patients[name]
            print("Patient details deleted successfully!")
        else:
            print("Patient not found!")
            
    elif choice == 5:
        search_value = input("Enter patient detail to search: ")
        found = False
        for name, patient in patients.items():
            for key, value in patient.items():
                if search_value.lower() in str(value).lower():
                    print("Name:", name)
                    for key, value in patient.items():
                        print(key + ":", value)
                    found = True
                    break
            if found:
                break
        if not found:
            print("Patient not found!")

    elif choice == 6:
        break

    else:
        print("Invalid choice! Please try again.")

print("Thank you for using the Hospital Management System")
