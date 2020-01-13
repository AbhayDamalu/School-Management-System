import random

def students():
    def admission_no_generator():
        f=open(r'Students.txt',"r")
        listt=[]
        data=f.readlines()
        for entry in data:
            entry=entry.split()
            listt+=entry[0]
                
        digit=[str(i) for i in range(1,10)]
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        admission_no=""
        while admission_no in listt or  admission_no=="":
            admission_no=""
            for i in range(1,6):
                if i in [1,3,5]:
                    admission_no+=random.choice(digit)
                else:
                    admission_no+=random.choice(alpha)
        return admission_no
        
    def view_students():
        f=open(r'Students.txt',"r")
        data=f.readlines()
        print("________________________________________________")
        print("|Admission no.  |Name                 |Class    |")
        print("|_______________________________________________|")
        if data==[]:
            print("|                                               |")
            print("|                 No Entries                    |")
            print("|_______________________________________________|")
        else:
            for entry in data:
                entry=entry.split()
                entry[0]+=(15-len(entry[0]))*" "
                entry[1]+=(21-len(entry[1]))*" "
                entry[2]+=(9-len(entry[2]))*" "
                print(f"|{entry[0]}|{entry[1].replace('_',' ')}|{entry[2]}|")
                print("|_______________________________________________|")
        input("...")
        f.close()
        
    def search_student():
        f=open(r'Students.txt',"r")
        print("Search by :-")
        print()
        print("1. Admission No.")
        print("2. Name")
        print("3. Class")
        ch=input(">>>")
        while ch not in ["1","2","3"]:
            print("Invalid Choice...")
            ch=input(">>>")
        if ch=="1":
            search_option=input("Enter Student's Admission No: ")
            
        if ch=="2":
            search_option=input("Enter Student's name: ")
            search_option=search_option.replace(' ','_')
        if ch=="3":
            search_option=input("Enter Student's class: ")
        data=f.readlines()
        print()
        print(f'Searching for "{search_option.replace("_"," ")}"...')
        print()
        print("===========================================")
        count=0
        for entry in data:
            entry=entry.split()
            if entry[0]==search_option or entry[1]==search_option or entry[2]==search_option:
                print("Admission no:",entry[0])
                print("Name:",entry[1].replace("_"," "))
                print("Class:",entry[2])
                print("Address:",entry[3].replace("_"," "))
                print("Contact no:",entry[4])
                print("Email:",entry[5])
                print("===========================================")
                count+=1
                
        if count==0:
            print("              No result(s)")
            print("===========================================")
        else:
            print(f"{count} result(s) found...")
        input("...")
        f.close()
        
    def add_student():
        f=open(r'Students.txt',"a")
        admission_no=admission_no_generator()
        print(f"Admission No. {admission_no}")
        print()
        New_student=input("New Student's First name:")
        while len(New_student)<=2 or len(New_student)>=10 or New_student.isalpha()==False:
            if New_student=="":
                print("* Mandatory Field...")
            else:
                if len(New_student)<=2:
                    print("Name too short...")
                if len(New_student)>10:
                    print("Exceeded 10 characters...")
                if New_student.isalpha()==False:
                    print("Only Alphabets Accepted...")
            print()
            print("Enter Again...")
            New_student=input("New Student's First name:")
        print()
        New_lastname=input("New Student's Last name:")
        while len(New_lastname)<=2 or len(New_lastname)>=10 or New_lastname.isalpha()==False:
            if New_lastname=="":
                print("* Mandatory Field...")
            else:
                if len(New_lastname)<=2:
                    print("Surname too short...")
                if len(New_lastname)>=10:
                    print("Exceeded 10 characters...")
                if New_lastname.isalpha()==False:
                    print("Only Alphabets Accepted...")
            print()
            print("Enter Again...")
            New_lastname=input("New Student's Last name:")
        print()
        Class=input("Class (1-12):")
        while Class not in [str(classs) for classs in range(1,13)]:
            if Class=="":
                print("* Mandatory Field...")
            else:
                print("Invalid Class...")
            Class=input("Class (1-12):")
        print()
        Address=input("Address:")
        while Address=="":
            print("* Mandatory Field...")
            Address=input("Address:")
        print()
        Contact_no=input("Contact no:")
        while len(Contact_no)!=10 or Contact_no.isdigit()==False:
            if Contact_no=="":
                print("* Mandatory Field...")
            else:
                if len(Contact_no)!=10:
                    print("Invalid number...")
                    print("Only 10 digit number accepted..")
                else:
                    print("Invalid number...")
                    print("Only digits accepted...")
            Contact_no=input("Contact no:")
        print()
        Email=input("Email:")
        if Email=="":
            Email="Null"
        else:
           while ("@"not in Email) or ((".com" not in Email) and (".co.in" not in Email) ):
               if Email=="":
                   Email="Null"
                   break
               else:
                   print("Invalid Email...")
                   Email=input("Email:")
        Email=Email.lower()
        print()
        print("Confirm (c) or Reject (r) :")
        confirm=input(">>>")
        if confirm.upper()=="C":
            f.write(f'{admission_no} {New_student}_{New_lastname} {Class} {Address.replace(" ","_")} {Contact_no} {Email}')
            f.write("\n")
            print("New student",New_student,"added successfully")
        else:
            print("New Student data entry terminated...")
        f.close()
        input("...")
        
    def remove_student():
        f=open(r'Students.txt',"r")
        data=f.readlines()
        Entry=[]
        for entry in data:
            Entry+=[entry.split()]
        print(Entry)
        admission_no_list=[Entry[admno][0] for admno in range(len(Entry))]
        print(admission_no_list)
        admission_no=input("Enter student's admission no: ")
        while admission_no not in admission_no_list:
            print("Admisson no. not found...")
            print("Enter Again")
            print()
            admission_no=input("Enter student's admission no: ")
        for entry in data:
            if entry.split()[0]==admission_no:
                ch=input("confirm (c) or reject (r)--")
                if ch.lower()=="c":
                    data.remove(entry)
                    print("Successfully removed..")
                else:
                    print("Operaton Terminated...")
        input("...")
        f.close()
        f=open(r'Students.txt',"w")
        for record in data:
            f.write(record)
        f.close()
          
    print("--------------STUDENT MANAGEMENT--------------")
    print("|                                            |")
    print("|1.View all Students                         |")
    print("|2.Search student                            |")
    print("|3.Add student                               |")
    print("|4.Remove student                            |")
    print("|============================================|")
    print()
    ch=input(">>>")
    while (ch!="1" and ch!="2" and ch!="3" and ch!="4"):
        print("Invalid Choice...")
        ch=input(">>>")
    try:
        f=open(r'Students.txt',"r")
        f.close()
    except:
        f=open(r'Students.txt',"w")
        f.close() 
    if ch=="1":
        view_students()
    if ch=="2":
        search_student()
    if ch=="3":
        add_student()
    if ch=="4":
        remove_student()
        
        
def staff():
    def view_staff():
        f=open(r'Staff.txt',"r")
        data=f.readlines()
        print("______________________________________________________________")
        print("|Name                 |Category            |Designation       |")
        print("|_____________________________________________________________|")
        if data==[]:
            print("|                                                             |")
            print("|                         No Entries                          |")
            print("|_____________________________________________________________|")
        else:
            for entry in data:
                entry=entry.split()
                entry[0]+=(21-len(entry[0]))*" "
                entry[1]+=(20-len(entry[1]))*" "
                entry[2]+=(18-len(entry[2]))*" "
                print(f"|{entry[0].replace('_',' ')}|{entry[1].replace('_',' ')}|{entry[2].replace('_',' ')}|")
                print("|_____________________________________________________________|")
        input("...")
        f.close()
        
    def search_staff():
        f=open(r'Staff.txt',"r")
        print("Search by :-")
        print()
        print("1. Name")
        print("2. Category")
        print("3. Designation")
        ch=input(">>>")
        while ch not in ["1","2","3"]:
            print("Invalid Choice...")
            ch=input(">>>")
        if ch=="2":
            print("1. Teaching Staff")
            print("2. Non-Teaching staff")
            print()
            search_option=input("Select Category: ")
            while search_option not in ["1","2"]:
                print("Invalid Choice...")
                search_option=input("Select Category: ")
            if search_option=="1":
                search_option="Teaching_Staff"
            else:
                search_option="Non-Teaching_Staff"
        if ch=="1":
            search_option=input("Enter Staff member's name: ")
            search_option=search_option.replace(" ","_") 
        if ch=="3":
            search_option=input("Enter Designation: ")
            search_option=search_option.replace(" ","_")
            
        data=f.readlines()
        print()
        print(f'''Searching for "{search_option.replace('_',' ') }"...''')
        print()
        print("===========================================")
        count=0
        for entry in data:
            entry=entry.split()
            if entry[0]==search_option or entry[1]==search_option or entry[2]==search_option:
                print("Name:",entry[0].replace('_',' '))
                print("Category:",entry[1].replace("_"," "))
                print("Designation:",entry[2].replace("_"," "))
                print("Address:",entry[3].replace("_"," "))
                print("Contact no:",entry[4])
                print("Email:",entry[5])
                print("===========================================")
                count+=1
                
        if count==0:
            print("              No result(s)")
            print("===========================================")
        else:
            print(f"{count} result(s) found...")
        input("...")
        f.close()
        
    def add_staff():
        f=open(r'Staff.txt',"a")
        New_staff_member=input("New staff member's First name:")
        while len(New_staff_member)<=2 or len(New_staff_member)>=10 or New_staff_member.isalpha()==False:
            if New_staff_member=="":
                print("* Mandatory Field...")
            else:
                if len(New_staff_member)<=2:
                    print("Name too short...")
                if len(New_staff_member)>10:
                    print("Exceeded 10 characters...")
                if New_staff_member.isalpha()==False:
                    print("Only Alphabets Accepted...")
            print()
            
            print("Enter Again...")
            New_staff_member=input("New Staff member's Firstname:")
        print()
        New_lastname=input("New Staff member's Last name:")
        while len(New_lastname)<=2 or len(New_lastname)>=10 or New_lastname.isalpha()==False:
            if New_lastname=="":
                print("* Mandatory Field...")
            else:
                if len(New_lastname)<=2:
                    print("Surname too short...")
                if len(New_lastname)>=10:
                    print("Exceeded 10 characters...")
                if New_lastname.isalpha()==False:
                    print("Only Alphabets Accepted...")
            print()
            print("Enter Again...")
            New_lastname=input("New Staff member's Last name:")
        print()
        print("Category:")
        print("1.Teaching Staff")
        print("2.Non-Teaching Staff")
        print()
        print("Enter choice (1/2)")
        category=input(">>>")
        while category!="1" and category!="2":
            if category=="":
                print("* Mandatory...")
            else:
                print("Invalid Choice...")
            category=input(">>>")
        if category=="1":
            category="Teaching_Staff"
            print("Designation:")
            print("1.Principal")
            print("2.Physics Teacher")
            print("3.Chemistry Teacher")
            print("4.Maths Teacher")
            print("5.Biology Teacher")
            print("6.English Teacher")
            print("7.Hindi Teacher")
            print("8.Computer Teacher")
            print("9.Others")
            ch=input(">>>")
            while ch not in ["1","2","3","4","5","6","7","8","9"]:
                if ch=="":
                    print("* Mandatory Field...")
                else:
                    print("Invalid Choice...")
                ch=input(">>>")
            if ch=="1":
                occupation="Principal"
            if ch=="2":
                occupation="Physics_Teacher"
            if ch=="3":
                occupation="Chemistry_Teacher"
            if ch=="4":
                occupation="Maths_Teacher"
            if ch=="5":
                occupation="Biology_Teacher"
            if ch=="6":
                occupation="English_Teacher"
            if ch=="7":
                occupation="Hindi_Teacher"
            if ch=="8":
                occupation="Computer_Teacher"
            if ch=="9":
                print("Please specify:")
                occupation=input(">>>")
                while occupation=="":
                    print("* Mandatory Field...")
                    occupation=input(">>>")
                occupation=occupation.replace(" ","_")
        else:
            category="Non-Teaching_Staff"
            print("Post:")
            print("1.Clerk")
            print("2.Accountant")
            print("3.Librarian")
            print("4.Security Guard")
            print("5.Peon")
            print("6.Others")
            print()
            ch=input(">>>")
            while ch not in ["1","2","3","4","5","6"]:
                if ch=="":
                    print("* Mandatory Field...")
                else:
                    print("Invalid Choice...")
                ch=input(">>>")
            if ch=="1":
                occupation="Clerk"
            if ch=="2":
                occupation="Accountant"
            if ch=="3":
                occupation="Librarian"
            if ch=="4":
                occupation="Security_Guard"
            if ch=="5":
                occupation="Peon"
            if ch=="6":
                print("Please specify:")
                occupation=input(">>>")
                while occupation=="":
                    print("* Mandatory Field...")
                    occupation=input(">>>")
                occupation=occupation.replace(" ","_")
        Address=input("Address:")
        while Address=="":
            print("* Mandatory Field...")
            Address=input("Address:")
        print()
        Address=Address.replace(" ","_")
        Contact_no=input("Contact no:")
        while len(Contact_no)!=10 or Contact_no.isdigit()==False:
            if Contact_no=="":
                print("* Mandatory Field...")
            else:
                if len(Contact_no)!=10:
                    print("Invalid number...")
                    print("Only 10 digit number accepted..")
                else:
                    print("Invalid number...")
                    print("Only digits accepted...")
            Contact_no=input("Contact no:")
        print()
        Email=input("Email:")
        if Email=="":
            Email="Null"
        else:
           while ("@"not in Email) or ((".com" not in Email) and (".co.in" not in Email) ):
               if Email=="":
                   Email="Null"
                   break
               else:
                   print("Invalid Email...")
                   Email=input("Email:")
        Email=Email.lower()
        print()
        print("Confirm (c) or Reject (r) :")
        confirm=input(">>>")
        if confirm.upper()=="C":
            f.write(f'{New_staff_member}_{New_lastname} {category} {occupation} {Address} {Contact_no} {Email}')
            f.write("\n")
            print("New Staff Member",New_staff_member,"added successfully")
        else:
            print("New Staff Member data entry terminated...")
        f.close()
        input("...")
        
    def remove_staff():
        f=open(r'Staff.txt',"rw+")
        print("1. Edit")
        print("2. Remove")
        ch=input(">>>")
        while ch not in ["1","2"]:
            print("Invalid Choice...")
            ch=input(">>>")
        admission_no=input("Enter student's admission no: ")
        data=f.readlines()
        for entry in data:
            entry=entry.split()
        if ch=="1":
            if entry[0]==admission_no:
                data.remove(entry)
                print("Successfully removed...")
        f.write(data)
        f.close()
        
        
    print("--------------STAFF MANAGEMENT----------------")
    print("|                                            |")
    print("|1.View all Staff members                    |")
    print("|2.Search staff member                       |")
    print("|3.Add staff member                          |")
    print("|4.Remove staff member                       |")
    print("|============================================|")
    print()
    ch=input(">>>")
    while (ch!="1" and ch!="2" and ch!="3" and ch!="4"):
        print("Invalid Choice...")
        ch=input(">>>")
    try:
        f=open(r'Staff.txt',"r")
        f.close()
    except:
        f=open(r'Staff.txt',"w")
        f.close() 
    if ch=="1":
        view_staff()
    if ch=="2":
        search_staff()
    if ch=="3":
        add_staff()
    if ch=="4":
        remove_staff()
        
def infrastructure():
    def library():
        def display_books():
            f=open(r'Infrastructure.txt',"r")
            data=f.readlines()
            print(" ____________________________________________________________________________________")
            print("| BOOK NAME                | AUTHER               | PUBLISHER            | PRICE     |")
            print("|____________________________________________________________________________________|")
            
            if data==[]:
                print("|                                                                                    |")
                print("|                                    No Enteries                                     |")
                print("|____________________________________________________________________________________|")
            else:   
                for entry in data:
                    entry=entry.split()
                    entry[0]+=(25-len(entry[0]))*" "
                    entry[1]+=(21-len(entry[1]))*" "
                    entry[2]+=(21-len(entry[2]))*" "
                    entry[3]+=(10-len(entry[3]))*" "
                    print(f"| {entry[0].replace('_',' ')}| {entry[1].replace('_',' ')}| {entry[2].replace('_',' ')}| {entry[3]}|")
                    print("|____________________________________________________________________________________|")
            f.close()
            
        def add_book():
            f=open(r'Infrastructure.txt',"a")
            book_name=input("Book Name: ")
            while book_name=="":
                print("* Mandatory Field...")
                book_name=input("Book Name: ")
            book_name=book_name.replace(" ","_")
            author=input("Author: ")
            while author=="":
                print("* Mandatory Field...")
                author=input("Author: ")
            author=author.replace(" ","_")
            publisher=input("Publisher: ")
            while publisher=="":
                print("* Mandatory Field...")
                publisher=input("Publisher: ")
            publisher=publisher.replace(" ","_")
            price=input("Price {INR}: ")
            while price=="" or price.isdigit()==False:
                if price=="":
                    print("* Mandatory Field...")
                else:
                    print("Only numericals allowed...")
                price=input("Price {INR}: ")
            f.write(f"{book_name} {author} {publisher} {price}")
            f.close()
        def issues():
            pass
            
            
        
        print("-------LIBRARY--------")
        print("1. List of Books")
        print("2. Add a book")
        print("3. Issues")
        print()
        ch=input(">>>")
        while ch not in ["1","2","3"]:
            print("Invalid Choice...")
            ch=input(">>>")
        if ch=="1":
            display_books()
        if ch=="2":
            add_book()
        if ch=="3":
            issues()
        f.close()
        input("...")
        
    def labs():
        print("-------LABS-----------")
        print("|1.Physics Lab       |")
        print("|2.Chemistry Lab     |")
        print("|3.Bio Lab           |")
        print("|4.Computer Lab      |")
        print("======================")
        input("...")
        
    print("--------------INFRASTRUCTURE------------------")
    print("|                                            |")
    print("|1.Library                                   |")
    print("|2.Labs                                      |")
    print("|============================================|")
    print()
    ch=input(">>>")
    while (ch!="1" and ch!="2"):
        print("Invalid Choice...")
        ch=input(">>>")
    try:
        f=open(r'Infrastructure.txt',"r")
        f.close()
    except:
        f=open(r'Infrastructure.txt',"w")
        f.close() 
    if ch=="1":
        library()
    if ch=="2":
        labs()
    
def reocc():
    global system
    print('''  ------------------------------------------------------
 |======================================================| 
 |============= School Management System ===============|
 |======================================================|
  ------------------------------------------------------''')
    print()
    print("1.STUDENTS")
    print("2.STAFF")
    print("3.INFRACTRUCTURE")
    print()
    print("4.quit")
    print()
    print("Enter your choice")
    ch=input(">>>")
    while (ch!="1" and ch!="2" and ch!="3" and ch!="4"):
        print("Enter a valid choice (1/2/3/4)")
        ch=input(">>>")
    print()
    if ch=="4":
        system=False
    else:   
        if ch=="1":
            students()
        elif ch=="2":
            staff()
        else:
            infrastructure()
       
###main###################################################
user_ID=''
passcode=''
print("            Login")
print()
user_id=input("Enter user id: ")
password=input("Enter password: ")
if user_id==user_ID and password==passcode:
    print()
    print("Successfully Logged in...")
    system=True
    while system==True:
        reocc()
    else:
        print()
        print("Successfully Logged out...")
        input("...")
else:
    print()
    print("Login Failed...")
    input("...")

