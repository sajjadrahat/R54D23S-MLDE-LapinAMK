# Alternative 1: Roman numerals

def arabicToRoman_ViceVersa (user_input):
        # Creating the table in dictionary to access values easily
        arabicToRomanTable={
                            1000: "M",
                            900: "CM", 
                            500: "D", 
                            400: "CD",
                            100: "C", 
                            90: "XC", 
                            50: "L", 
                            40: "XL",
                            10: "X", 
                            9: "IX", 
                            5: "V", 
                            4: "IV",
                            1: "I"
                            }
        
        #running a loop in whole dictionary
        try:
            if int(user_input)>3999:
                print("Error: maximum possible roman numeral is 3999")
            else:
                result=""
                user_input = int(user_input)
                for val, key in arabicToRomanTable.items():
                            # Dividing with the values and getting int number to know how many times to add the roman values.
                            n= int(user_input/val)
                            user_input = user_input-n*val
                            if n>0:
                                result+=key*n
                print(result)
        except ValueError:        
                        result=0
                        #Reversing the table Roman table for values.
                        RomantoArabicTable = dict(reversed(item) for item in arabicToRomanTable.items())

                        # Storing the key values for dual chracter roman values. Ex: "IX",  "CM"
                        key_values = 1000
                        for chracters in user_input:
                            values = RomantoArabicTable[chracters]
                            if values<key_values:
                                  result-=values
                            else:
                                   result+=values
                            key_values=values
                               
                        print(result)

        

user_input= input("Enter The Values You Want To Convert Arabic to Roman or Roman to Arabic: \n")
arabicToRoman_ViceVersa(user_input)