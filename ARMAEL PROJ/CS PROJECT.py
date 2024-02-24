# create database and table for customer details
'''import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root",passwd = "M@nn12344321")
mc = mydb.cursor()
mc.execute("create database if not exists details")
mydb.commit()

import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root",passwd = "M@nn12344321",database = "armael")
mc = mydb.cursor()
query = "create table details(NAME varchar(30), PHONE_No int(11), address varchar(100), DOB DATE, CHECK_IN_DATE DATE, CHECK_OUT_DATE DATE, NUMBER_OF_PEOPLE int(2))"
mc.execute(query)
mydb.commit()'''

import random

#welcome message
def welcome():
    f1 = open("ARMAEL.txt")
    rec = " "
    while rec:
        rec = f1.readline()
        print(rec)
    f1.close()

welcome()



#display choices
print("WE ARE DELIGHTED THAT YOU HAVE SELECTED OUR HOTEL")
print(" ")
print("THE HOTEL OFFERS A SELECTION OF SERVICES AND FACALITIES WHICH ARE DETAILED BELOW")
print(" ")




#information about the hotel

def info():
    f1 = open("INFO.txt")
    rec = " "
    while rec:
        rec = f1.readline()
        print(rec)
    f1.close()
                                                  
        


#enter customer details and select room
roombill = 0
def details():
    print("-----------------------------------------------------------------")
    print("                      ADD CUSTOMER DETAILS                       ")
    print("-----------------------------------------------------------------")
    import mysql.connector as m
    mydb = m.connect(host = "localhost",user = "root",passwd = "M@nn12344321",database = "armael")
    mc = mydb.cursor()
    for i in range(1):
        name = input("PLEASE ENTER YOUR FULL NAME : ")
        phone_no = int(input("PLEASE ENTER YOUR SEVEN DIGIT PHONE NUMBER : "))
        address = input("PLEASE ENTER YOUR ADDRESS : ")
        dob = input("ENTER YOUR DATE OF BIRTH IN YYYY-MM-DD FORMAT : ")
        checkin_date = input("PLEASE ENTER THE CHECK IN DATE IN YYYY-MM-DD FORMAT : ")
        checkout_date = input("PLEASE ENTER THE CHECK OUT DATE IN YYYY-MM-DD FORMAT : ")
        number_of_adults = int(input("PLEASE ENTER THE NUMBER OF ADULTS : "))
        number_of_kids = int(input("PLEASE ENTER THE NUMBER OF KIDS : "))
        number_of_people = number_of_adults + number_of_kids
        query = "insert into details(NAME,PHONE_NO,address,DOB,CHECK_IN_DATE,CHECK_OUT_DATE,NUMBER_OF_PEOPLE) values('{}',{},'{}','{}','{}','{}',{})".format(name,phone_no,address,dob,checkin_date,checkout_date,number_of_people)
        mc.execute(query)
    for r in mc:
        print(r)
    mydb.commit()
    
    print(" ")
    print("RECORD HAS BEEN ENTERED SUCCESSFULLY")
        
    
        

def rooms():
    global roombill 
    roomno = 0
    print("       ---------------------------------------------------------------      ")
    print("                          TYPES OF ROOMS                                     ")
    print("       ---------------------------------------------------------------      ")
    print("+---------+--------------------------------------------+-------------------+")
    print("|  SR_NO  |                   ROOMS                    |    PRICE_IN_AED   |")
    print("+---------+--------------------------------------------+-------------------+")
    print("|    1    |          The Grande Armael Suite           |       25,000      |")
    print("+---------+--------------------------------------------+-------------------+")
    print("|    2    |           Georgia De Kabel Suite           |       18,000      |")
    print("+---------+--------------------------------------------+-------------------+")
    print("|    3    |               Tel Aveiro Room              |        7,500      |")
    print("+---------+--------------------------------------------+-------------------+")
    print("|    4    |               Executive Room               |        5,000      |")
    print("+---------+--------------------------------------------+-------------------+")
    print("|    5    |                 Studio Room                |        2,500      |")
    print("+---------+--------------------------------------------+-------------------+")
    r = int(input("PLEASE ENTER SR_NO TO SELECT A ROOM : "))
    nd = int(input("PLEASE ENTER THE NUMBER OF DAYS FOR WHICH YOU WANT TO BOOK THIS ROOM : "))

    if r == 1:
        roombill = 25000*nd
        roomno = random.randrange(100,110)
                
    elif r == 2:
        roombill = 18000*nd
        roomno = random.randrange(200,250)
                
    elif r == 3:
        roombill = 7500*nd
        roomno = random.randrange(300,400)
                
    elif r == 4:
        roombill = 5000*nd
        roomno = random.randrange(401,500)
            
    elif r == 5:
        roombill = 2500*nd
        roomno = random.randrange(501,600)
                
    else:
        print("PLEASE ENTER A VALID SR_NO")
            
    print ("Your room number is - ",roomno,"\n")
    print ("Your room bill = AED ",roombill,"\n")
        
    




#order from restaurant
    
restrobill = 0
def restaurant():
    global restrobill 
    print("     ------------------------------------------------------------------     ")
    print("                      WELCOME TO THE ARMAEL RESTAURANT                      ")
    print("     ------------------------------------------------------------------     ")
    print(" ")
    print(" ")
    print("+--------------------------------------------------------------------------+")
    print("|                                   MENU                                   |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("+--------------------------------------------------------------------------+")
    print("|      SR_NO      |              **DISHES**              |   PRICE_IN_AED  |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        1        |          ESPRESSO MACCHIATO          |       25.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        2        |              CAPPUCCINO              |       25.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        3        |           COLD BREW COFFEE           |       22.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        4        |           HAWAIIAN ICED TEA          |       22.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        5        |             LICHI ICED TEA           |       22.50     |")
    print("+-----------------+--------------------------------------+-----------------+")   
    print("|        6        |               MASALA TEA             |       22.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        7        |            DEVILED LOX EGGS          |       32.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        8        |                FALAFEL               |       32.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        9        |               EMPANADA               |       30.00     |")
    print("+-----------------+--------------------------------------+-----------------+")  
    print("|        10       |               FOCACCIA               |       35.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        11       |                BURRITO               |       35.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        12       |              CHELO KEBAB             |       37.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        13       |              DUM BIRYANI             |       50.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        14       |             VIRGIN MOJITO            |       27.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        15       |           CRANBERRY SANGRIA          |       27.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        16       |               PINA COLADA            |       27.50     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        17       |               CHOCO DOME             |       37.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        18       |                 BAKLAVA              |       38.00     |")
    print("+-----------------+--------------------------------------+-----------------+")
    print("|        19       |              BOTTLED WATER           |       11.50     |")
    print("+-----------------+--------------------------------------+-----------------+")

    r = 1
    while (r != 0):
        r = int(input("ENTER THE SR_NO TO ORDER FOOD OR ENTER 0 TO EXIT : "))
                
        if r == 1 or r == 2:
            restrobill += 25.00
                
        elif r <= 6 and r >= 3:
            restrobill + 22.50
                    
        elif r == 7 or r == 8:
            restrobill += 32.00
                
        elif r == 9:
            restrobill += 30.00
                    
        elif r == 10 or r == 11:
            restrobill += 35.00
                    
        elif r == 12 or r == 17:
            restrobill += 37.00
                    
        elif r == 13:
            restrobill += 50.00
                    
        elif r<=16 and r>=14:
            restrobill += 27.50
                    
        elif r == 18:
            restrobill += 38.00
                    
        elif r == 19:
            restrobill += 11.50
                    
        elif r == 0:
            print ("Your restaurant bill = AED ",restrobill,"\n")
                    
        else:
            print("PLEASE ENTER A VALID SR_NO")
        
         
    
        
            
#select an activity
            
activitybill = 0
def activities():
    global activitybill 
    print ("\n******ACTIVITY MENU*******\n")
    print("""1. THEME PARK -----> AED 400/4 hr  \n2. WATER PARK -----> AED 400/3 hr \n3. HELICOPTER RIDE & DESERT SAFARI -----> AED 600/4 hr \n4. SKY DIVING -----> AED 600/2 hr \n5. GOLF & INHOUSE ACTIVITIES -----> AED 500/3 hr \n6. SANCTUARY & ZOO VISIT -----> AED 350/3 hr \n7. PRIVATE THEATRE -----> AED 500/3 hr \n""")
    activity=int(input("Choose your activity number : "))
    NOS=int(input("Enter number of sessions you want : "))
    print("\n\n*************************************************\n")
            
    if activity==1:
        print("YOU HAVE SELECTED : THEME PARK ")
        activitybill += NOS * 400
                
    elif activity==2:
        print("YOU HAVE SELECTED : WATER PARK  ")
        activitybill += NOS * 400
                
    elif activity==3:
        print("YOU HAVE SELECTED : HELICOPTER RIDE & DESERT SAFARI")
        activitybill += NOS * 600
                
    elif activity==4:
        print("YOU HAVE SELECTED : SKY DIVING")
        activitybill += NOS * 600
                
    elif activity==5:
        print("YOU HAVE SELECTED : GOLF & INHOUSE ACTIVITIES")
        activitybill += NOS * 500
                
    elif activity==6:
        print("YOU HAVE SELECTED : SANCTUARY & ZOO VISIT")
        activitybill += NOS * 350
                
    elif activity==7:
        print("YOU HAVE SELECTED : PRIVATE THEATRE")
        activitybill += NOS * 500
                
            
    print("Your total activity bill = AED ",activitybill,"\n")
                
            

    



#gaming arena
    
gamingbill = 0    
def gaming():
    global gamingbill 
    print("          ------------------------------------------------------------------     ")
    print("                            WELCOME TO THE ARMAEL GAMING ARENA                    ")
    print("          ------------------------------------------------------------------     ")
    print(" ")
    print(" ")
    print("+-----------------------------------------------------------------------------------------+")
    print("|                                       PRICE LIST                                        |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|      SR_NO      |              **GAMES **              |     PLATFORM    | PRICE_IN_AED |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("+-----------------------------------------------------------------------------------------+")
    print("|        1        |               VALHEIM                |        PC       |     25.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        2        |            THE WITCHER 3             |        PC       |     25.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        3        |            PHASMAPHOBIA              |        PC       |     25.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        4        |       ASSASSIN'S CREED ODYSSEY       |        PC       |     25.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        5        |             SLAY THE SPIRE           |      PC/PS4     |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")   
    print("|        6        |            APEX LEGENDS              |      PC/PS4     |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        7        |          FINAL FANTASY 14            |     XBOX/PS4    |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        8        |           GENSHIN IMPACT             |      PC/PS4     |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        9        |            FORZA HORIZON             |       PS4       |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")  
    print("|        10       |               FIFA 21                |       PS4       |     27.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        11       |            RISK OF RAIN              |       PS4       |     30.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        12       |             UNCHARTED                |       PS4       |     30.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        13       |           HALF-LIFE:ALYX             |        VR       |     30.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        14       |             BEAT SABER               |        VR       |     30.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")
    print("|        15       |           ELITE:DANGEROUS            |        VR       |     30.00    |")
    print("+-----------------+--------------------------------------+-----------------+--------------+")

    o = 1
    while (o != 0):
        o = int(input("ENTER THE SR_NO TO SELECT A GAME OR ENTER 0 TO EXIT : "))
                
        if o <= 4 and o >= 1:
            gamingbill += 25.00
                    
        elif o <= 10 and o >= 5:
            gamingbill += 27.00
                    
        elif o <= 15 and o >= 11:
            gamingbill += 30.00
                    
        elif o == 0:
            print ("Your gaming bill = AED ",gamingbill,"\n")
                    
        else:
            print("PLEASE ENTER A VALID SR_NO")

    
                        
                

#laundry and dry cleaning services
            
laundrybill = 0
def laundry():
    global laundrybill
    print("             ----------------------------------------------------------------------------             ")
    print("                                  LAUNDRY & DRY CLEANING SERVICES                                     ")
    print("             ----------------------------------------------------------------------------             ")
    print(" ")
    print(" ")
    print("+-----------------------------------------------------------------------------------------------------+")
    print("|                                             PRICE LIST                                              |")
    print("+--------------+-----------+------------------------------+---------------------+---------------------+") 
    print("|   CATEGORY   |   SR_NO   |           ARTICLES           |       LAUNDRY       |     DRY CLEANING    |")
    print("+--------------+-----------+------------------------------+---------------------+---------------------+")
    print("+-----------------------------------------------------------------------------------------------------+")
    print("|              |     1     |          Suit(2pcs)          |        28.00        |        40.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     2     |             Coat             |        20.00        |        28.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     3     |             Shirt            |        14.00        |        20.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|     MENS     |     4     |            T-Shirt           |        14.00        |        16.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     5     |            Sweater           |        28.00        |        32.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     6     |              Tie             |                     |        16.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     7     |            Overcoat          |                     |        65.00        |")
    print("+--------------+-----------+------------------------------+---------------------+---------------------+")
    print("+-----------------------------------------------------------------------------------------------------+")
    print("|              |     8     |          Suit(2pcs)          |        28.00        |        40.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     9     |            Jacket            |        28.00        |        32.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     10    |         Evening Dress        |                     |        50.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|    LADIES    |     11    |           Cheongsam          |                     |        52.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     12    |          Wedding Gown        |                     |       250.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     13    |          Baju Kurong         |                     |        52.00        |")
    print("+              +-----------+------------------------------+---------------------+---------------------+")
    print("|              |     14    |          Indian Saree        |                     |        52.00        |")
    print("+--------------+-----------+------------------------------+---------------------+---------------------+")
    print("***all the prices in AED***")

    z = 1
    while (z != 0):
        z = int(input("ENTER THE SR_NO TO CHOOSE A SERVICE OR ENTER 0 TO EXIT : "))
                
        if z == 1 or z == 8:
            ch = input("ENTER L FOR LAUNDRY OR D FOR DRY CLEANING : ")
            if ch == 'L':
                laundrybill += 28.00
            elif ch == 'D':
                laundrybill += 40.00
            else:
                print("PLEASE INPUT L OR D")
                        
                    
        elif z == 2:
            ch = input("ENTER L FOR LAUNDRY OR D FOR DRY CLEANING : ")
            if ch == 'L':
                laundrybill += 20.00
            elif ch == 'D':
                laundrybill += 28.00
            else:
                print("PLEASE INPUT L OR D")
                
        elif z == 3:
            ch = input("ENTER L FOR LAUNDRY OR D FOR DRY CLEANING : ")
            if ch == 'L':
                laundrybill += 14.00
            elif ch == 'D':
                laundrybill += 20.00
            else:
                print("PLEASE INPUT L OR D")
                
        elif z == 4:
            ch = input("ENTER L FOR LAUNDRY OR D FOR DRY CLEANING : ")
            if ch == 'L':
                laundrybill += 14.00
            elif ch == 'D':
                laundrybill += 16.00
            else:
                print("PLEASE INPUT L OR D")

        elif z == 6:
            laundrybill += 16.00
                
        elif z == 5 or z == 9:
            ch = input("ENTER L FOR LAUNDRY OR D FOR DRY CLEANING : ")
            if ch == 'L':
                laundrybill += 28.00
            elif ch == 'D':
                laundrybill += 32.00
            else:
                print("PLEASE INPUT L OR D")
                    
        elif z == 7:
            laundrybill += 65.00
                    
        elif z == 10:
            laundrybill += 50.00
                    
        elif z == 11 or z == 13 or z == 14:
            laundrybill += 52.00
                    
        elif z == 12:
            laundrybill += 250.00
                    
        elif z == 0:
            print ("Your laundry bill = AED ",laundrybill,"\n")
                    
        else:
            print("PLEASE ENTER A VALID SR_NO")

    



#car rental servces
rentalbill = 0    
def rental():
    global rentalbill 
    print("     ----------------------------------------------------------------------             ")
    print("                              CAR RENTAL SERVICES                                       ")
    print("     ----------------------------------------------------------------------             ")
    print(" ")
    print(" ")
    print("+------------------------------------------------------------------------------+")
    print("|                             CAR RENTAL AT ARMAEL                             |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|  SR_NO  |            MODEL            |  SEATING CAPACITY  |  PRICE_IN_AED   |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    1    |       DODGE CHALLENGER      |         5          |      350.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    2    |  MERCEDES C200 CONVERTIBLE  |         4          |      450.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    3    |           AUDI A6           |         4          |      450.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    4    |        NISSAN PATROL        |         7          |      450.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    5    |      RANGE ROVER VOGUE      |         5          |      600.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    6    |      CADILLAC ESCALADE      |         7          |      700.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    7    |         BMW SERIES 7        |         5          |      720.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    8    |      ROLLS-ROYCE WRAITH     |         4          |     1500.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    9    |      MERCEDES G63 2021      |         5          |     2000.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("|    10   |       LAMBORGHINI URUS      |         5          |     4500.00     |")
    print("+---------+-----------------------------+--------------------+-----------------+")
    print("***charges/day***")
            
    p = int(input("ENTER THE SR_NO TO CHOOSE A SERVICE OR ENTER 0 TO EXIT : "))
            
    if p == 1:
        print("YOU HAVE OPTED FOR - DODGE CHALLENGER")
        rentalbill += 350.00
                
    elif p == 2:
        print("YOU HAVE OPTED FOR - MERCEDES C200 CONVERTIBLE")
        rentalbill += 450.00
                
    elif p == 3:
        print("YOU HAVE OPTED FOR - AUDI A6")
        rentalbill += 450.00
                
    elif p == 4:
        print("YOU HAVE OPTED FOR - NISSAN PATROL")
        rentalbill += 450.00
                
    elif p == 5:
        print("YOU HAVE OPTED FOR - RANGE ROVER VOGUE")
        rentalbill += 600.00
                
    elif p == 6:
        print("YOU HAVE OPTED FOR - CADILLAC ESCALADE")
        rentalbill += 700.00
                
    elif p == 7:
        print("YOU HAVE OPTED FOR - BMW SERIES 7")
        rentalbill += 720.00
                
    elif p == 8:
        print("YOU HAVE OPTED FOR - ROLLS ROYCE WRAITH")
        rentalbill += 1500.00
                
    elif p == 9:
        print("YOU HAVE OPTED FOR - MERCEDES G63 AMG")
        rentalbill += 2000.00
                
    elif p == 10:
        print("YOU HAVE OPTED FOR - LAMBORGHINI URUS")
        rentalbill += 4500.00
                
    else:
        print("PLEASE ENTER A VALID SR_NO")
    print ("Your car rental bill = AED ",rentalbill,"\n")

    

    
            

#search a customer
    
def search():
    import mysql.connector as m
    mydb = m.connect(host = "localhost",user = "root",passwd = "M@nn12344321",database = "armael")
    mc = mydb.cursor()
    nm = input("PLEASE ENTER THE CUSTOMER NAME TO BE SEARCHED(in capital letters only) : ")
    print("The following details are in the format (NAME, PHONE No., Address, DOB, Checkin date, Checkout date, No. of people)")
    mc.execute("select * from details where name ='"+nm+"'")
    for x in mc:
        print(x)




#delete a customer
def delete():
    import mysql.connector as m
    mydb = m.connect(host = "localhost",user = "root",passwd = "M@nn12344321",database = "armael")
    mc = mydb.cursor()
    nm = input("PLEASE ENTER THE NAME OF THE CUSTOMER TO DELETE THEIR RECORD(in capital letters only) : ")
    mc.execute("delete from details where name ='"+nm+"'")
    mydb.commit()
    print(" ")
    print("RECORD HAS BEEN DELETED SUCCESSFULLY")





z = 0
while (z != 9):
    print(" ")
    print("PLEASE SELECT A NUMBER FROM THE GIVEN CHOICES")
    print(" ")
    print("0--->INFORMATION ABOUT THE HOTEL")
    print("1--->ENTER CUSTOMER DETAILS AND SELECT ROOM")
    print("2--->ORDER FROM RESTAURANT")
    print("3--->SELECT AN ACTIVITY FOR THE DAY")
    print("4--->GAMING ARENA")
    print("5--->LAUNDRY AND DRY CLEANING SERVICES")
    print("6--->CAR RENTAL SERVICES")
    print("7--->SEARCH CUSTOMER")
    print("8--->DELETE A CUSTOMER FROM THE RECORDS")
    print("9--->TOTAL BILL")
    print("10--->EXIT")
    print(" ")
    c = 1
    c = int(input("PLEASE ENTER YOUR CHOICE FROM THE ABOVE LIST : "))

    if c == 0:
        info()

    elif c == 1:
        details()
        rooms()

    elif c == 2:
        restaurant()

    elif c == 3:
        activities()

    elif c == 4:
        gaming()

    elif c == 5:
        laundry()

    elif c == 6:
        rental()

    elif c == 7:
        search()

    elif c == 8:
        delete()

    elif c == 9:
        print("YOUR ROOM BILL IS - AED ",roombill)
        print("YOUR RESTAURANT BILL IS - AED ",restrobill)
        print("YOUR ACTIVITY BILL IS - AED ",activitybill)
        print("YOUR GAMING BILL IS - AED ",gamingbill)
        print("YOUR LAUNDRY BILL IS - AED ",laundrybill)
        print("YOUR CAR RENTAL BILL IS - AED ",rentalbill)
        total_bill = roombill+restrobill+activitybill+gamingbill+laundrybill+rentalbill 
        print("YOUR TOTAL BILL IS - AED ",total_bill)

    elif c == 10:
        f1 = open("EXIT.txt")
        rec = " "
        while rec:
            rec = f1.readline()
            print(rec)
        f1.close()
        break


    
            

    
