"""
Q3. DRIVING LICENSE REGISTRATION

Create the following custom exceptions:

1. InvalidAgeForDrivingLicenseException
2. InvalidMarkForDrivingLicenseException

Eligibility Rules:

1. Age must be greater than or equal to 18.
2. Age cannot be negative.
3. Road rules test marks must be between 0 and 100.
4. A person must score more than 80 marks to pass.

Requirements:

1. Create the Person class with:
   name
   age
   mark

2. Create the two custom exception classes.
3. Create a method named check_eligibility().
4. Validate age first.
5. If age is negative:
   InvalidAgeForDrivingLicenseException: Invalid age

6. If age is less than 18:
   InvalidAgeForDrivingLicenseException:
   Age should be more than 18 years old

7. Validate marks.
8. If marks are negative or greater than 100:
   InvalidMarkForDrivingLicenseException: Invalid mark

9. If marks are 80 or less:
   InvalidMarkForDrivingLicenseException:
   Mark should be more than 80

10. If all conditions are satisfied:
    Approved

11. Handle all exceptions using try-except.
"""

class InvalidAgeForDrivingLicenseException(Exception):
    pass

class InvalidMarkForDrivingLicenseException(Exception):
    pass

class Person:
   def __init__(self,name,age,marks):
        self.name = name 
        self.age = age
        self.marks = marks

   def checkEligibility(self):
       if self.age < 0:
           raise InvalidAgeForDrivingLicenseException("Invalid Age")
       if self.age < 18:
           raise InvalidAgeForDrivingLicenseException("Age should be more than 18 years old")
       if self.marks < 0 or self.marks > 100:
           raise InvalidMarkForDrivingLicenseException("Invalid Marks")
       if self.marks <= 80:
           raise InvalidMarkForDrivingLicenseException("Mark should be more than 80")


p1 = Person("Raghu",19,88)

try:
    p1.checkEligibility()
    print("Approved")
except InvalidMarkForDrivingLicenseException as e:
    print("InvalidMarkForDrivingLicenseException",e)
except InvalidAgeForDrivingLicenseException as e:
    print("InvalidAgeForDrivingLicenseException:",e)
