'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''
patients = {}

while True:
    print('''
=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit''')

    n = int(input("Select an option: "))

    match n:
        case 1:
            id = int(input("Enter patient ID: "))

            if id in patients:
                print("{Patient Already Exists}")
            else:
                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                gender = input("Enter gender(Male/Female): ")
                disease = input("Enter disease name: ")
                DoctorName = input("Enter name of the doctor handling: ")

                patients[id] = {'Name':name,'Age':age,'Gender':gender,'Disease':disease,'Doctor':DoctorName}
                print()
                print("Patient Successfully Added.")
                print()

        case 2:
            id = int(input("Enter patient id: "))
            print()
            if id in patients:
                p = patients[id]
                print(f"Patient ID : {id}")
                for k,v in p.items():
                    print(f"{k} : {v}")
                print()
            else:
                print("Patient Not found")

        case 3:
            id = int(input("Enter patient id: "))
            if id in patients:
                disease = input("Enter updated disease: ")
                patients[id]["Disease"] = disease
                print()
                print("Disease Updated Successfully.")
            else:
                print("[Patient Not Found]")
            print()

        case 4:
            id = int(input("Enter patient id: "))

            if id in patients:
                del patients[id]
                print("[Patient Record Deleted Successfully]")
            else:
                print("[Patient not found]")
            print()

        case 5:
            if len(patients) > 0:
                for id in patients:
                    print("----------------------------")
                    print(f"Patient ID : {id}")

                    for k,v in patients[id].items():
                        print(f"{k} : {v}")
                    print()
            else:
                print("[No patients available.]")

        case 6:
            print(f"Total Patients: {len(patients)}")

        case 7:
            disease = input("Enter Disease: ")
            found = False
            for id in patients:
                if patients[id]['Disease'] == disease:
                    print(f"{id}  {patients[id]['Name']}")
                    found = True

            if found == False:
                print("[No Patient Found]")
            print()

        case 8:
            oldest = 0
            oldestID = None
            for id in patients:
                if patients[id]['Age'] > oldest:
                    oldest = patients[id]['Age']
                    oldestID = id

            print(f"Patient ID : {oldestID}")
            for k,v in patients[oldestID].items():
                print(f"{k} : {v}")

            print()

        case 9:
            print()
            youngest = 200
            youngestID = None
            for id in patients:
                if patients[id]['Age'] < youngest:
                    youngest = patients[id]['Age']
                    youngestID = id

            print(f"Patient ID : {youngestID}")
            for k,v in patients[youngestID].items():
                print(f"{k} : {v}")
                
            print()

        case 10:
            print("Thank You For Using Hospital Patient Management System")
            print("[=== Exiting ===]")
            break

        case __:
            continue            
            
                    
