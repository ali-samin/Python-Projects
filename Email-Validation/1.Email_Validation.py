#Email validation using string function
# conditions
'''
1. minimum character length should be 6
2. first letter should be alphabets
3. use '@' at a time
4. position of dot '.' should be third or fourth from the end
5. there is no uppercase character.
6. the should not any space in between the space

'''

email = input("Enter yourr Email:--  ")    #  g@g.in , name@gmail.com

k = 0
j = 0
d = 0
if len(email)>=6:
    if email[0].isalpha():    # check the first character of your email is alphabet or not
        if ("@" in email) and (email.count("@")==1):   # check that @ is present in email or it should be one
            if (email[-3]==".") ^ (email[-4]=="."):  # use exor operator to check position of dot '.' should be third or fourth from the end
                for i in email:
                    if i==i.isspace():  # check space in the string
                        k=1
                    elif i.isalpha():   # check i character is alphabets
                        if i==i.upper():   # if i is alphabets then check that i is uppercase character
                            j=1
                    elif i.isdigit():      # check if any digit present in the email then continue for loop
                        continue
                    elif i=="_" or i=="." or i=="@": # if any spacial character from " _ , . , @" then continue
                        continue
                    else:               # else return wrong email
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("You have entered Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("There is no '@' or more then 1 '@' present in the string")
    else:
        print("First Letter of your email should be alphabet")
else:
    print("Length of you email should be greater then 6")