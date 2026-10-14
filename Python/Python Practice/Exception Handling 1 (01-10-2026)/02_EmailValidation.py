"""
Q2. EMAIL VALIDATION USING CUSTOM EXCEPTIONS

Create the following custom exception classes:

1. DotException
2. AtTheRateException
3. DomainException

Requirements:

1. Create all three custom exceptions by inheriting from Exception.
2. Accept an email address from the user.
3. Validate the email according to the following rules.

Rule 1:
The email must contain exactly one '@' character.

If this rule fails:
AtTheRateException: Invalid @ usage

Rule 2:
The email must contain a '.' character after '@'.

If this rule fails:
DotException: Invalid Dot usage

Rule 3:
The email must end with one of the following valid domains:

in
com
net
biz

If this rule fails:
DomainException: Invalid Domain

4. Handle exceptions using try-except.
5. If all conditions are satisfied:
   Valid email address
6. Otherwise display the exception message followed by:
   Invalid email address
"""
class DotException(Exception):
    pass

class AtTheRateException(Exception):
    pass

class DomainException(Exception):
    pass

def validateEmail(email):
   if email.count("@") != 1:
      raise AtTheRateException("Invalid @ usage")

   if email.count(".") != 1 or email.index(".") < email.index("@"):
      raise DotException("Invalid Dot usage")

   if email[email.index(".")+1:] not in ("in","com","net","biz"):
      raise DomainException("Invalid Domain")
   
email = input("Enter your Mail: ")

try:
   validateEmail(email)   
   print(f"Valid Email Address: {email}")
except AtTheRateException as e:
   print("Invalid Email Address")
   print("Error: ",e)
except DomainException as e:
   print("Invalid Email Address")
   print("Error: ",e)
except DotException as e:
   print("Invalid Email Address")
   print("Error: ",e)
