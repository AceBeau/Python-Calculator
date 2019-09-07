#Python Program :- Simple Calculator With Functions

def Addition():
    print("#"*75)
    print("#"*9 + " "*20 + "Devil Calculator" + " "*21 + "#"*9)
    print("#"*75)

  
    x = int(input("\n How Many Values You Want To Add? \n (2-5) >> "))
    if x == 2:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        print("\n Addition Of ", num_1 ,"And", num_2 ," Is >> ", num_1+num_2)
        lets_begin()
        

    if x == 3:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        print("\n Addition Of ", num_1 ,"And", num_2 ,"And", num_3 ," Is >> ", num_1+num_2+num_3)
        lets_begin()

    if x == 4:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        print("\n Addition Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ," Is >> ", num_1+num_2+num_3+num_4)
        lets_begin()
        
    if x == 5:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        num_5 = int(input("\n Enter the Fifth Value >> "))
        print("\n Addition Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ,"And", num_5 ," Is >> " ,num_1+num_2+num_3+num_4+num_5)
        lets_begin()

def Substraction():
    print("#"*75)
    print("#"*9 + " "*20 + "Devil Calculator" + " "*21 + "#"*9)
    print("#"*75)

   
    x = int(input("\n How Many Values You Want To Substract? \n (2-5) >> "))
    if x == 2:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        print("\n Substraction Of ", num_1 ,"And", num_2 ," Is >> ", num_1-num_2)
        lets_begin()
        

    if x == 3:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        print("\n Substraction Of ", num_1 ,"And", num_2 ,"And", num_3 ," Is >> ", num_1-num_2-num_3)
        lets_begin()

    if x == 4:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        print("\n Substraction Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ," Is >> ", num_1-num_2-num_3-num_4)
        lets_begin()

    if x == 5:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        num_5 = int(input("\n Enter the Fifth Value >> "))
        print("\n Substraction Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ,"And", num_5 ," Is >> ", num_1-num_2-num_3-num_4-num_5)
        lets_begin()

def Multiplication():
    print("#"*75)
    print("#"*9 + " "*20 + "Devil Calculator" + " "*21 + "#"*9)
    print("#"*75)


    x = int(input("\n How Many Values You Want To Multiply? \n (2-5) >> "))
    if x == 2:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        print("\n Multiplication Of ", num_1 ,"And", num_2 ," Is >> ", num_1*num_2)
        lets_begin()

    if x == 3:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        print("\n Multiplication Of ", num_1 ,"And", num_2 ,"And", num_3 ," Is >> ", num_1*num_2*num_3)
        lets_begin()

    if x == 4:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        print("\n Multiplication Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ," Is >> ", num_1*num_2*num_3*num_4)
        lets_begin()

    if x == 5:
        num_1 = int(input("\n Enter the First Value >> "))
        num_2 = int(input("\n Enter the Second Value >> "))
        num_3 = int(input("\n Enter the Third Value >> "))
        num_4 = int(input("\n Enter the Fourth Value >> "))
        num_5 = int(input("\n Enter the Fifth Value >> "))
        print("\n Multiplication Of ", num_1 ,"And", num_2 ,"And", num_3 ,"And", num_4 ,"And", num_5 ," Is >> ", num_1*num_2*num_3*num_4*num_5)
        lets_begin()

def Division():
    print("#"*75)
    print("#"*9 + " "*20 + "Devil Calculator" + " "*21 + "#"*9)
    print("#"*75)

    num_1 = int(input("\n Enter the First Value >> "))
    num_2 = int(input("\n Enter the Second Value >> "))
    print("\n Division Of ", num_1 ,"And", num_2 ," Is >> ", num_1/num_2)
    lets_begin()

def lets_begin():
    print("#"*75)
    print("#"*9 + " "*20 + "Devil Calculator" + " "*21 + "#"*9)
    print("#"*75)

    choice = int(input("\n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division \n 5. Exit \n\n >> "))
    while True:
        if choice == 1:
            Addition()
        elif choice == 2:
            Substraction()
        elif choice == 3:
            Multiplication()
        elif choice == 4:
            Division()
        elif choice == 5:
            exit()
        else:
            print("\n Worng Choice! Try Again")

lets_begin()