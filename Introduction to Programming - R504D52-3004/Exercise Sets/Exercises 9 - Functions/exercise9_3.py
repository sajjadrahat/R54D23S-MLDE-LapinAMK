import functions

user_ssn = input("Give an ISSN-serial: \n")

if functions.magazine_serial_check(user_ssn):
    print("Valid ISSN.")
else:
    print("Incorrect ISSN.")