print ("***************WELCOME TO THE QUIZ******************")
#Asking for user details, name


while True:  
    name = input("Please enter your name : ")
    if name.replace(" ","").isalpha():
        print("Greetings",name,"welcome to the general knowledge quiz")
        break
    else:
        print("please enter name using only alphabets :)")
