
from Data import *
import datetime
def gettime():
    return datetime.datetime.now()
import  random



print("""Manager:-Hello Sir,Welcome to La Fountain : The Food Fair
         how many people will be dining today?
Customer:-We are 10 people
Manager:-I will take you to your table""")
name__=False
Num__=False
Gmail__=False


name=str(input("\nEnter Your Name:-"))
if name.isalpha() or name.isspace() or name.isascii():
    name__=True
else:
    print("Your name is Wrong")

Num=str(input("Enter Your Number:-"))
if len(Num)==10 :
        Num__=True
else:
    print("Your number is less than 10 Numeric")

email=str(input("Enter Your email:-"))
if email.endswith("@gmail.com"):
        Gmail__=True
else:
    print("Please Insert correct Gmail Id")

l1 = []
if Num__==True and name__==True and Gmail__==True:
    with open("Name.csv", "a") as op:
        op.write(f"{gettime()},")
        op.write(name + ",")
        op.write(Num + ",")
        op.write(email + "\n")
        
    print("-------------------------------------------------------------------------")
    print("                     La Fountain : The Food Fair")
    print("-------------------------------------------------------------------------")
    print("						 Menu Card")
    print("-------------------------------------------------------------------------")
    print("\n BEVARAGES							 26 Dal Fry................ 140.00")
    print("----------------------------------	 27 Dal Makhani............ 150.00")
    print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
    print(" 2 Masala Tea.............. 25.00")
    print(" 3 Coffee.................. 25.00	 ROTI")
    print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
    print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
    print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
    print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
    print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
    print(" 9 Cheese Toast Sandwich... 70.00")
    print(" 10 Grilled Sandwich........ 70.00	 RICE")
    print("									 ----------------------------------")
    print(" SOUPS								 33 Plain Rice.............. 90.00")
    print("----------------------------------	 34 Jeera Rice.............. 90.00")
    print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
    print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
    print(" 13 Veg. Noodle Soup....... 110.00")
    print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
    print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
    print("									 37 Plain Dosa............. 100.00")
    print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
    print("----------------------------------	 39 Masala Dosa............ 130.00")
    print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
    print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
    print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
    print(" 19 Palak Paneer........... 120.00")
    print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
    print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
    print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
    print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
    print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
    print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
    print("Press 0 -to end ")


    ch = 1
    while (ch != 0):

        ch = int(input("Please Enter A Item Index number-> "))

        # if-elif-conditions to assign item
        # prices listed in menu card
        if ch==1:
            l1.append(a_1)
        elif ch == 2:
            l1.append(a_2)
        elif ch == 3:
            l1.append(a_3)
        elif ch == 4:
            l1.append(a_4)
        elif ch == 5:
            l1.append(a_5)
        elif ch == 6:
            l1.append(a_6)
        elif ch == 7:
            l1.append(a_7)
        elif ch == 8:
            l1.append(a_8)
        elif ch == 9:
            l1.append(a_9)
        elif ch == 10:
            l1.append(a_10)
        elif ch == 11:
            l1.append(a_11)
        elif ch == 12:
            l1.append(a_12)
        elif ch == 13:
            l1.append(a_13)
        elif ch == 14:
            l1.append(a_14)
        elif ch == 15:
            l1.append(a_15)
        elif ch == 16:
            l1.append(a_16)
        elif ch == 17:
            l1.append(a_17)
        elif ch == 18:
            l1.append(a_18)
        elif ch == 19:
            l1.append(a_19)
        elif ch == 20:
            l1.append(a_20)
        elif ch == 21:
            l1.append(a_21)
        elif ch == 22:
            l1.append(a_22)
        elif ch == 23:
            l1.append(a_23)
        elif ch == 24:
            l1.append(a_24)
        elif ch == 25:
            l1.append(a_25)
        elif ch == 26:
            l1.append(a_26)
        elif ch == 27:
            l1.append(a_27)
        elif ch == 28:
            l1.append(a_28)
        elif ch == 29:
            l1.append(a_29)
        elif ch == 30:
            l1.append(a_30)
        elif ch == 31:
            l1.append(a_31)
        elif ch == 32:
            l1.append(a_32)
        elif ch == 33:
            l1.append(a_33)
        elif ch == 34:
            l1.append(a_34)
        elif ch == 35:
            l1.append(a_35)
        elif ch == 36:
            l1.append(a_36)
        elif ch == 37:
            l1.append(a_37)
        elif ch == 38:
            l1.append(a_38)
        elif ch == 39:
            l1.append(a_39)
        elif ch == 40:
            l1.append(a_40)
        elif ch == 41:
            l1.append(a_41)
        elif ch == 42:
            l1.append(a_42)
        elif ch == 43:
            l1.append(a_43)
        elif ch == 44:
            l1.append(a_44)
        elif ch == 45:
            l1.append(a_45)
        elif ch == 46:
            l1.append(a_46)
        elif ch == 0:
            pass
        else:
            print("Wrong Choice..!!")

ans=""
for i in l1:
    item=i[0]
    price=i[2]
    qty=i[1]
    ans=ans+f"{item:<25} {price:<10} {qty} \n"

total=0
Quantity=0


for i in l1:
    total=total+i[2]
    Quantity=Quantity+i[1]


g,s,c=int(0.18 * total),int(0.09 * total),int(0.09 * total)
if Num__==True and name__==True and Gmail__==True:
    print(
f"""
    
La Fountain : The Food Fair
    PH=07265844440
Mail=lafountain@gmail.com
----------------------------------

{datetime.date.today()}
----------------------------------
Bill Number --> {random.randint(1000,2000)}
----------------------------------
Item                       Price      Qty     
----------------------------------   
{ans}
---------------------------------- 
Total                      {total:<10} {Quantity}
---------------------------------- 

GSt 18%                     {g}
SGST 9%                     {s}
CGST 9%                     {c}

Total Bill With Tax         {int(total+g+s+c)}

        Thank You For Visiting
      La Fountain : The Food Fair  
""")
else:
    print()