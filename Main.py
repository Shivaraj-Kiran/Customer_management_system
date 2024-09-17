import streamlit as st
import mysql.connector
import base64
import pandas as pd
import datetime

st.title("Customer Management System")
choice=st.sidebar.selectbox("Menu",("Home","Employee","HR","Aspirant"))


if (choice=="Home"):
    st.image("Happy.jpg")
    st.write("""Welcome to Our Company!

At my company, we believe that our employees are the heart and soul of our organization. As a team, we strive to create an environment where each individual is valued, supported, and empowered to thrive.

Our employees are not just workers; they are the driving force behind our success. From the talented developers crafting innovative solutions to the dedicated customer service representatives ensuring exceptional experiences, each member of our team plays a crucial role in delivering excellence to our clients and partners.

We recognize that our employees are our most valuable asset. That's why we invest in their growth, both personally and professionally. Through ongoing training, mentorship programs, and opportunities for advancement, we empower our team members to reach their full potential and achieve their career aspirations.

But it's not just about what our employees do; it's about who they are. We celebrate diversity and foster a culture of inclusivity, where every voice is heard, and every contribution is valued. Our team is made up of individuals from different backgrounds, cultures, and perspectives, coming together to collaborate, innovate, and make a difference.

At [Company Name], we are more than just colleagues; we are a family. We support each other through challenges, celebrate each other's successes, and work together towards our shared goals. Together, we are stronger, more resilient, and capable of accomplishing great things.

So, whether you're a current employee, a prospective team member, or a valued partner, we invite you to join us on this journey. Together, we'll continue to push boundaries, exceed expectations, and make a positive impact on the world.

Thank you for being a part of our [Company Name] family.

Sincerely,

Shivaraj Desai""")
elif(choice=="Employee"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    id1=st.text_input("Enter e-mail: ")
    password=st.text_input("Enter Password: ")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
        c=mydb.cursor()
        c.execute("select * from Employees")
        for r in c:
            if (r[3]==id1 and base64.urlsafe_b64decode(r[9]).decode()==password):
                st.session_state['login']=True
                break
        if (st.session_state['login']==False):
            st.subheader("Incorrect ID or password!")
    if (st.session_state['login']==True):
            st.subheader("Login Successful")
            choice_1=st.selectbox("Features",("None","View employee status","View Tasks assigned","Login to System"))
            if(choice_1=="View employee status"):
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                d=mydb1.cursor()
                d.execute("select * from Employees")
                l=[]
                for r1 in d:
                    l.append(r1)
                df=pd.DataFrame(data=l)
                st.dataframe(df)    
            elif(choice_1=="View Tasks assigned"):
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                d=mydb1.cursor()
                d.execute("select * from Tasks")
                l=[]
                for r1 in d:
                    l.append(r1)
                df=pd.DataFrame(data=l)
                st.dataframe(df)
            elif(choice_1=="Login to System"):
                emp_id1=st.text_input("Enter Employee_ID:")
                date1=str(datetime.datetime.today())[0:10]
                tm_in1=str(datetime.datetime.today())[10:]
                tm_out1=st.text_input("Enter time out for today:")
                btn2=st.button("Log-in")
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                d=mydb1.cursor()
                d.execute("select max(attendance_id) from Attendance")
                attendance_id1=str(datetime.datetime.today())[10:]
                if (btn2):
                    mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                    d=mydb1.cursor()                   
                    d.execute("Insert into Attendance values(%s,%s,%s,%s,%s)",(attendance_id1,emp_id1,date1,tm_in1,tm_out1))
                    mydb1.commit()
                    st.header("Login successfully")
                
elif(choice=="HR"):
    if 'HRlogin' not in st.session_state:
        st.session_state['HRlogin']=False
    id1=st.text_input("Enter e-mail: ")
    password=st.text_input("Enter Password: ")
    btn=st.button("HRLogin")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
        c=mydb.cursor()
        c.execute("select * from users")
        for r in c:
            if (r[0]==id1 and r[1]==password):
                st.session_state['HRlogin']=True
                break
        if (st.session_state['HRlogin']==False):
            st.subheader("Incorrect ID or password!")
    if (st.session_state['HRlogin']==True):
            st.subheader("Login Successful")
            choice_1=st.selectbox("Features",("None","View Employee skills","View Employee salaries"))
            if(choice_1=="View Employee skills"):
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                d=mydb1.cursor()
                d.execute("select a.employee_id,b.skill_name from EmployeeSkills a, Skills b where a.skill_id=b.skill_id")
                l=[]
                for r1 in d:
                    l.append(r1)
                df=pd.DataFrame(data=l)
                st.dataframe(df)
            elif(choice_1=="View Employee salaries"):
                mydb1=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
                d=mydb1.cursor()
                d.execute("SELECT * FROM Salaries")
                l=[]
                for r1 in d:
                    l.append(r1)
                df=pd.DataFrame(data=l)
                st.dataframe(df)
elif(choice=="Aspirant"):
    st.write("""Join Our Team: Empowering Excellence

    Welcome to [Company Name]! As we continue to grow and innovate, we are always on the lookout for talented individuals who share our passion for excellence and commitment to making a difference.

    At [Company Name], our employees are more than just workers; they are the backbone of our success. We believe in nurturing a culture of collaboration, creativity, and inclusivity, where every voice is heard, and every contribution is valued.

    Joining our team means becoming part of a dynamic and diverse community dedicated to pushing boundaries, challenging the status quo, and driving positive change in the world. Whether you're a seasoned professional or just starting your career journey, there's a place for you here at [Company Name].

    We offer more than just a job; we offer a rewarding career path filled with growth opportunities, professional development, and the chance to make a real impact. From cutting-edge technology projects to meaningful community initiatives, you'll have the chance to work on exciting projects that matter.

    At [Company Name], we believe in investing in our employees' success. That's why we provide ongoing training, mentorship programs, and support for continued learning and development. We empower our team members to unleash their full potential, pursue their passions, and achieve their career goals.

    But it's not just about work; it's about balance. We understand the importance of work-life balance and strive to create an environment where our employees can thrive both personally and professionally. From flexible work arrangements to wellness programs and employee benefits, we prioritize the well-being and happiness of our team members.

    So, if you're ready to take your career to the next level, we invite you to explore the opportunities available at [Company Name]. Join us on our journey to empower excellence and shape the future together.

    Together, we can achieve greatness.""")
    name1=st.text_input("Enter name: ")
    email1=st.text_input("Enter e-mail: ")
    phone_number1=st.text_input("Enter mobile number: ")
    resume_url1=st.text_input("Enter URL of resume: ")
    applied_position1=st.text_input("Enter position applied for: ")
    application_date1=str(datetime.datetime.today())[0:10]
    experience_years=st.text_input("Enter Experience years: ")
    btn=st.button("ALogin")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee1")
        c=mydb.cursor()
        c.execute("Insert into aspirant values(%s,%s,%s,%s,%s,%s,%s)",(name1,email1,phone_number1,resume_url1,applied_position1,application_date1,experience_years))
        mydb.commit()
        st.subheader("Applied Successfully.")