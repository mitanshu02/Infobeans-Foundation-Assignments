'''
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2

'''

from collections import namedtuple

patient = namedtuple("patient",["p_id","p_name","age","disease"])

n = int(input("Enter number of patients: "))

p = []

for i in range(n):
    p_id = input(f"Enter id of patient {i+1}: ")
    name = input(f"Enter name of patient {i+1}: ")
    age = int(input(f"Enter age of student {i+1}: "))
    disease = input(f"Enter disease of patient {i+1}: ")
   
    pt = patient(p_id,name,age,disease)
    p.append(pt)
    print()

id = input("Enter patient id: ")
disease = input("Enter disease: ")
print()

for pt in p:
    print(pt.p_id,pt.p_name,pt.age,pt.disease)

dCount = 0

print()
print("Patient Found: ")
for i in range(n):
    if p[i].p_id == id:
        print(p[i].p_id,p[i].p_name,p[i].age,p[i].disease)
    if p[i].disease.lower() == "diabetes":
        dCount += 1
    
print()
print("Patient Above 60: ")

for pt in p:
    if pt.age > 60:
        print(pt.p_id,pt.p_name,pt.age,pt.disease)
print()

print("Patients with Diabetes: ")
print(dCount)
    
        