#Alternative 3: Text squares.

def text_sqaures(row, column):
    #Determining plus, minus and bar sign coordinate values series.

    #plus_sign = [(1,1), (1,1+8), (1, 1+8+8), ...., (4,1), (4,1+8), (4,1+8+8).... ,(4+4, 1).....]
    #plus sign 'x' values are if i==1 or i%4==0 every time. 
    #plus sign 'y' are adding 8 each time... 
    plus=1

    # minus_sign i=1 and i%4==0 and j is odd number always
    minus= None

    # Bar sign 'x', should be like x!=1 and x%4!=0 always 
    # Bar sign 'y', should be like y==1 and add 8 to that val each time.
    bar = 1

    #Sign finder function to find sign based on x, y values
    def sign_finder(x, y):
        #getting the non local variables to get & update value on conditions
        nonlocal plus
        nonlocal bar

        #plus sign
        if (x==1 and y==plus) or (x%4==0 and y==plus):
                    print("+", end="")
                    plus+=8
        #minus sign
        elif(x==1 and y%2!=0) or (x%4==0 and y%2!=0):
                    print("-", end="")
        #bar sign
        elif y==bar:
                    print("|", end="")
                    bar+=8
        #If no condtion is true then it should be space always
        else:
                    print(" ", end="")

    #This is to loop to to check all the rows and columns and update sign
    #Chracters for row is row*4+1
    #Characters for column is column*8+2
    for r in range(1,row*4+1):
        plus=1
        bar=1
        for c in range(1,column*8+2):
            sign_finder(r, c)
        #printing a blank line so that it breaks the row and goes to second line
        print()
                    

user_input_row = int(input("How  many rows do you want? \n"))
user_input_col= int(input("How  many columns do you want? \n"))

#calling the function based on row, column                
text_sqaures(user_input_row, user_input_col)