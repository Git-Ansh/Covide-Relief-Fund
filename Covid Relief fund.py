def cr():
    import sys
    import datetime
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n***Namaste!***")
    print("***Covid Relief Fund***")
    print("In these challenging times, when everybody is struggling to maintain their work-life balance, many citizens of our nation are deprived of basic necessities of life. We have taken upon the responsibility to aid those in need, and we need your help.\n**********************************************")
    x=int(input("1. Donor/Admin Login\n2. New Donor Sign Up\nEnter your choice(1/2): "))
    if x==1:
        while True:
            count=0
            f=open("usrnm.txt","r+")
            k=f.read()
            res=k.split("\n")
            fi=open("passwords.txt","r+")
            ki=fi.read()
            resl=ki.split("\n")
            combined=zip(res,resl)
            valdict={}
            for keys, value in combined:
                    valdict[keys]=value
            username=input("username: ")
            if username not in valdict:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("This is not a valid username, input username again!")
                continue
            else:
                pass
            while True:
                if count==3:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("too many failed attempts, You have been restricted")
                    sys.exit()
                password=input("password: ")
                if username in valdict and password in valdict:
                    pass
                elif password!= valdict[username]:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("Password is not valid. ")
                    print(f"username: {username}")
                    count+=1
                    continue
                elif password== valdict[username]:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("LOGIN SUCCESSFUL")
                    print(f"WELCOME {username} ")
                    while True:
                        if username!='admin':
                            print("Donor Functionalities: ")
                            print("1. Donate necessities\n2. View your donations\n3. Exit")
                            m=int(input("Choose a functionality(1/2/3): "))
                            while True:
                                if m==1:
                                    n=datetime.datetime.now()
                                    dt=n.strftime("%Y-%m-%d %H:%M:%S")
                                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                    print("*****Donate necessities*****")
                                    item=input("Enter item name: ")
                                    qt=input("Enter quantity: ")
                                    print("...Success!")
                                    k=open(f"{username}.txt","a+")
                                    k.write("\nItem name: ")
                                    k.write(item)
                                    k.write("\n")
                                    k.write("Quantity: ")
                                    k.write(qt)
                                    k.write("\n")
                                    k.write("Date and Time: ")
                                    k.write(dt)
                                    k.write("\n")                        
                                    k.close()
                                    o=open("admin.txt","a+")
                                    o.write("Donor name: ")
                                    o.write(username)
                                    o.write("\n")
                                    o.write("Donation category: ")
                                    o.write("Basic necessities")
                                    o.write("\n")
                                    o.write("Item name: ")
                                    o.write(item)
                                    o.write("\n")
                                    o.write("Quantity: ")
                                    o.write(qt)
                                    o.write("\n")
                                    o.write("Date and Time: ")
                                    o.write(dt)
                                    o.write("\n")                        
                                    o.close()
                                    u=input("Do you wish to donate more items?(y/n): ")
                                    if u=='y':
                                        pass
                                    if u=='n':
                                        sys.exit()
                                if m==2:
                                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYour donations:")
                                    y=open(f"{username}.txt","r+")
                                    t=y.read()                                                                                            
                                    print(t)                                                    
                                    g=input("Do you wish to continue or exit?(c/e): ")
                                    if g=='c':
                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    if g=='e':
                                        sys.exit()
                                if m==3:
                                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHave a nice day!")
                                    sys.exit()
                        else:
                            print("Admin Funtionalities: ")
                            print("1. View charity itmes\n2. View individual charity\n3. Exit")
                            n=int(input("Choose a functionality(1/2/3): "))
                            if n==1:
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                f=open("admin.txt","r+")
                                p=f.read()
                                print(p)
                                f.close()
                            if n==2:
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIndividual donor search")
                                z=input("Enter the name of the Donor: ")
                                f=open(f"{z}.txt","r+")
                                r=f.read()
                                print("\n\n******View Individual Charity******")
                                print("This is the charity record of",z)
                                print(r)
                            if n==3:
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHave a nice day!")
                                sys.exit()            
    if x==2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNew Donor Sign Up:")
        fl=open("usrnm.txt","a+")
        f=open("usrnm.txt","r+")
        k=f.read()
        res=k.split("\n")
        fi=open("passwords.txt","a+")
        ki=fi.read()
        resl=ki.split("\n")
        while True:
            username=input("Enter new username: ")
            if username in k:
                print("Username already exists")
                continue
            else:
                f.write(username)
                f.write("\n")
                break
        while True:
            password=input("Enter new password: ")
            if len(password)<=6:
                print("Password too short")
                continue
            else:
                while True:
                    cp=input("Confirm password: ")
                    if cp==password:
                        fi.write(password)
                        fi.write("\n")
                        print("Account Saved successfully")
                        f.close()
                        fl.close()
                        fi.close()
                        cr()
                    else:
                        print("passwords do not match please reconfirm password")
                        continue
cr()


