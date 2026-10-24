import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# cur.execute("CREATE DATABASE DjangoORM")
# print("database created")
# cur.execute('''CREATE table employee( 
#               id int primary key auto_increment,
#             name varchar(20),
#             designation varchar (30),
#             salary decimal(10,2)
#         )''')
# print("table created")


class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols !="":
                cols+=','
                placeholder+=','
            cols+=col   
            placeholder+='%s'       
        values=tuple(kwargs.values())
        print(f"insert into employee ({cols}) values ({placeholder}),{values}")
        query=f"insert into employee({cols}) values({placeholder})"
        print(query)
        cur.execute(query,values)
        conn.commit()



    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())

    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            print(f"update employee set {key}={kwargs.get(key)} where id={args[0]}")
            cur.execute(f"update employee set {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
    def delete (self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
        conn.commit()

    def filter(self,*args,**kwargs):  
    
        for key in kwargs:
            cur.execute(f"select * from eemployee where {key}='{kwargs.get[key]}'")
            print(cur.fetchall())

employee=Employee()

while True:
    print("1.create employee")
    print("2.list all employee")
    print("3.Employee detail view")
    print("4.update employee")
    print("5.delete employee")
    print("6.filter")
    print("7.Exit")

    choice =int(input("enter your choice:"))

    if choice==1:
        name=input("Enter the name:")
        design=input("Enter ypur designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=design,salary=salary)

    elif choice==2:
        
        employee.list() 

    elif choice==3: 
        print("")
        id=int(input('enter the employee id:'))  
        employee.retrieve(id=id)
    elif choice==4:
        id=int(input("enter the id of employee:"))
        print("update")
        print("1.update employee Name")
        print("2.update employee designation")
        print("3.update employee salary")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the new name:")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("enter the new destination:")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=int(input("enter the new salary:"))
            employee.update(id,salary=salary)
        else:
            print("invalid choice")            

    elif choice==5:
        id=int(input("enter the employee id:"))
        employee.delete(id)

    elif choice==6:
        print("filter options")
        print("1.filter by name:")
        print("2.filter by designation:")
        print("3.filter by salary:")
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the name")
            employee.filter(name=name)
        elif choice==2:
            desig=(input("enter the designation"))
            employee.filter(designation=desig)   
        elif choice==3:
            salary=float(input("enter the salary:")) 
                  


        employee.filter()
    elif choice==7:
        print("Thank you")
        break    

    else:
        print("invalid choice")

        


conn.close()        








