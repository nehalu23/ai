#assignment by Nehal Uddin Shaikh
#Marksheet generator
#info about how to fill the Requirment details form !
print("┌────────────────────────────────────────────────────────────────────────┐")
print('''
    Note :

    name,collage name and class name cannot contain numbers

    roll no and subject's marks should only contain numbers

    marks cannot exceed from 100

    marks cannot be in -ve 
    

      ***Follow the above rules to generate correct marksheet***
    
    ''')

print("└────────────────────────────────────────────────────────────────────────┘")

proceed1 =input("\n\nPress Enter to Continue...")

#------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------


#--------------------------------------------------------------user inputs----------------------------------------------------

print("\n\nREQUIRED DETAILS :")    
print("┌────────────────────────────────────────────────────────────────────────┐")
name =input("(1/10) Enter your name :- ")
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
roll_no =input("(2/10) Enter Your Roll no. :- ")
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
college_name =input("(3/10) Enter Your College name :- ")
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
class_name =input("(4/10) Enter class you are in :- ")
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
eng =int(input("(5/10) Enter your Marks in English out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
maths =int(input("(6/10) Enter your Marks in Maths out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
urdu =int(input("(7/10) Enter your Marks in Urdu out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
phy =int(input("(8/10) Enter your Marks in Physics out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
chem =int(input("(9/10) Enter your Marks in Chemistry out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("┌────────────────────────────────────────────────────────────────────────┐")
pst =int(input("(10/10) Enter your Marks in Pakistan studies out of 100 :- "))
print("└────────────────────────────────────────────────────────────────────────┘")
print("\n\n")

#------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------x------











#Check if all marks are under 100 and above 0

if eng < 101 and eng > 0 and maths < 101 and maths > 0 and urdu < 101 and phy < 101 and chem < 101 and pst < 101:
    print("Yay ! You have entered marks according to the given condition")
    proceed2 =input("\n\nPress Enter to Continue...")

else:
    print('''****** INCORRECT VALUES FOUND ! YOU ARE RESPONSIBLE FOR THE FOLLOWING MARKSHEET !  ****** ''')
    proceed3 =input("\n\nPress Enter to Continue...")
    
#-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x







#Status(pass/fail) logic

if eng > 32:
 eng_status = "pass"
else:
 eng_status = "fail"

if maths > 32:
 maths_status = "pass"
else:
 maths_status = "fail"

if urdu > 32:
 urdu_status = "pass"
else:
 urdu_status = "fail"

if phy > 32:
 phy_status = "pass"
else:
 phy_status = "fail"

if chem > 32:
 chem_status = "pass"
else:
 chem_status = "fail"

if pst > 32:
 pst_status = "pass"
else:
 pst_status = "fail"

#-x-x-x-x-x-x-x-x-x-x-x-x-x


# Individual grades

#eng
if eng > 100:
    eng_grade = "■"
elif eng > 75:
    eng_grade = "A"
elif eng > 60:
    eng_grade = "B"
elif eng > 45:
    eng_grade = "C"
elif eng > 32:
    eng_grade = "D"
else:
    eng_grade = "F"

#urdu
if urdu > 100:
    urdu_grade = "■"
elif urdu > 75:
    urdu_grade = "A"
elif urdu > 60:
    urdu_grade = "B"
elif urdu > 45:
    urdu_grade = "C"
elif urdu > 32:
    urdu_grade = "D"
else:
    urdu_grade = "F"

#pst
if  pst> 100:
    pst_grade = "■"
elif pst > 75:
    pst_grade = "A"
elif pst > 60:
    pst_grade = "B"
elif pst > 45:
    pst_grade = "C"
elif pst > 32:
    pst_grade = "D"
else:
    pst_grade = "F"

#phy
if phy > 100:
    phy_grade = "■"
elif phy > 75:
    phy_grade = "A"
elif phy > 60:
    phy_grade = "B"
elif phy > 45:
    phy_grade = "C"
elif phy > 32:
    phy_grade = "D"
else:
    phy_grade = "F"

#chem
if chem > 100:
    chem_grade = "■"
elif chem > 75:
    chem_grade = "A"
elif chem > 60:
    chem_grade = "B"
elif chem > 45:
    chem_grade = "C"
elif chem > 32:
    chem_grade = "D"
else:
    chem_grade = "F"

#maths
if maths > 100:
    maths_grade = "■"
elif maths > 75:
    maths_grade = "A"
elif maths > 60:
    maths_grade = "B"
elif maths > 45:
    maths_grade = "C"
elif maths > 32:
    maths_grade = "D"
else:
    maths_grade = "F"

#-x-x-x-x-x-x-x-x-x-x-x

# TOTAL
total = eng + pst + urdu + phy + maths + chem
#-x-x-x-x-x-x-x-x-x-x-x-x-x

# Percentage
per0 = float((total/600)*100)
per00 = int(per0)
per = str(per00)+"%"
#-x-x-x-x-x-x-x-x-x-x-x-x-x

# Grades

if per00 > 100:
    grade = "■"
elif per00 > 75:
    grade = "A"
elif per00 > 60:
    grade = "B"
elif per00 > 45:
    grade = "C"
elif per00 > 33:
    grade = "D"
else:
    grade = "F"

#-x-x-x-x-x-x-x-x-x-x


#final status

if eng_grade == "F" or maths_grade == "F" or pst_grade == "F" or urdu_grade == "F" or phy_grade == "F" or chem_grade == "F" :
    status = "FAIL"
else:
    status = "PASS"

#-x-x-x-x-x-x-x-x-x


# Final result display

print("                    ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
print("                    │                                                                                                                   │")
print("                    │                               ▓▓▓ ▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓   ▓ ▓▓▓▓ ▓   ▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓                                │ ")
print("                    │                               ▓  ▓  ▓ ▓   ▓ ▓   ▓ ▓  ▓  ▓    ▓   ▓ ▓    ▓      ▓                                  │ ")
print("                    │                               ▓  ▓  ▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓   ▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓   ▓                                  │ ")
print("                    │                               ▓     ▓ ▓   ▓ ▓ ▓   ▓  ▓     ▓ ▓   ▓ ▓    ▓      ▓                                  │ ")
print("                    │                               ▓     ▓ ▓   ▓ ▓  ▓  ▓   ▓ ▓▓▓▓ ▓   ▓ ▓▓▓▓ ▓▓▓▓   ▓                                  │ ")
print("                    │      ───────────────────────────────────────────────────────────────────────────────────────────────────────      │")
print("                    │                                                                                                                   │")
print("                    │          Candidate's name:- " + str(name.upper()) + "      ")
print("                    │                                                                                                                   │")
print("                    │          Roll Number:-" + str(roll_no) + "                 ")
print("                    │                                                                                                                   │")
print("                    │          College name:- " + str(college_name.upper()) + "  ")
print("                    │                                                                                                                   │")
print("                    │          Class:- " + str(class_name.upper()) + "           ")
print("                    │                                                                                                                   │")
print("                    │                                                                                                                   │")
print("                    │      ───────────────────────────────────────────────────────────────────────────────────────────────────────      │")
print("                    │                     │  SUBJECTS  │  Max-NO.  │ OBTAINED │ OBT.% │ PASS % │ STATUS │ GRADE │              ")
print("                    │      ───────────────────────────────────────────────────────────────────────────────────────────────────────      │")
print("                    │                                                                                                                   │")
print("                    │                       ENGLISH        100         "+str(eng)+"        "+str(eng)+"%"+"     33 %     "+str(eng_status.upper())+"      "+eng_grade+" ")
print("                    │                                                                                                                   │")
print("                    │                       MATHS          100         "+str(maths)+"        "+str(maths)+"%"+"     33 %     "+str(maths_status.upper())+"      "+maths_grade+" ")
print("                    │                                                                                                                   │")
print("                    │                       URDU           100         "+str(urdu)+"        "+str(urdu)+"%"+"     33 %     "+str(urdu_status.upper())+"      "+urdu_grade+" ")
print("                    │                                                                                                                   │")
print("                    │                       PHYSICS        100         "+str(phy)+"        "+str(phy)+"%"+"     33 %     "+str(phy_status.upper())+"      "+phy_grade+" ")
print("                    │                                                                                                                   │")
print("                    │                       CHEMISTRY      100         "+str(chem)+"        "+str(chem)+"%"+"     33 %     "+str(chem_status.upper())+"      "+chem_grade+" ")
print("                    │                                                                                                                   │")
print("                    │                       PAK.STUDIES    100         "+str(pst)+"        "+str(pst)+"%"+"     33 %     "+str(pst_status.upper())+"      "+pst_grade+" ")
print("                    │                                                                                                                   │")
print("                    │      ───────────────────────────────────────────────────────────────────────────────────────────────────────      │")
print("                    │                     │    TOTAL   │   600     │   "+str(total)+"   │   "+per+"  │  33%   │  "+status+"  │   "+grade+"   │ ")
print("                    │      ───────────────────────────────────────────────────────────────────────────────────────────────────────      │")
print("                    │                                                                                                                   │")
print("                    │                                                                                                                   │")
print("                    │                                                                                                                   │")
print("                    │                                                                                                                   │")
print("                    │                                                                                                                   │")
print("                    └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")

#-x-x-x-x-x-x-x-x-x-x-x-x-x