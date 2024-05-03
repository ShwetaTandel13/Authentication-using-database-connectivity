#Authentication using OOPS and database connectivity
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="abc@123",database="student")
cur=conn.cursor()

class Authentication:
    def registration(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="abc@123",database="student")
        self.cur=self.conn.cursor()
        id=int(input('Enter id:'))
        username=input('Enter username:')
        userpass=int(input('Enter userpass:'))
        if (len(str(userpass))>=8):
            query='insert into student(id,name,password)values(%s,%s,%s)'
            values=(id,username,userpass)
            self.cur.execute(query,values)
            print('user register successfully')
            self.conn.commit()
        else:
            print('your passsword should be 8 digit')
            

    def login(self):
        count=3
        while count>0:
            username=input('Enter username:')
            userpass=int(input('Enter userpassword:'))
            query='select *from student where name=%s and password=%s'
            values=(username,userpass)
            self.cur.execute(query,values)
            data=self.cur.fetchone()
            if data:
                print('Login Successfull')
                break
            else:
                count-=1
                print('Invallid username and password')
                print('you have only attempt',count,'left')
        if count==0:
                print('your id not maching record so your acount is blocked')
                choice=int(input('Enter your choice 1 for forgot password and 2 for exit'))
                if choice==1:
                    print('your password must contain at least 8 digits,first letter is always capital,must contain specialsymbol')
                    name=input('Enter name:')
                    newpassword=int(input('Enter new password:')) 
                    #if len(str(newpin))<=8 and str(newpin[0].upper):
                    if (len(str(newpassword))>=8):
                        print('passsword change successfully')
                        query='update student set password=%s where name=%s'
                        values=(newpassword,name)
                        self.cur.execute(query,values)
                        self.conn.commit()
                        
                    else:
                        print('your passsword should be 8 digit')
                else:
                    print('Thank you')
        else:
            print('Thank you')


    def exit(self):
        print('thank you')
    

    def conn_close(self):
        self.cur.close()
        self.conn.close()
a=Authentication()
while True:
    print('1.registration')
    print('2.login')
    print('3.Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        a.registration()
    elif choice==2:
        a.login()
    elif choice==3:
        a.exit()
        a.conn_close()
        print('Exit')
        break
    else:
        print('Invallid Choice')

