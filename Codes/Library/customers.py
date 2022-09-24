#Author:Alma, 2019
#Customers class
import datetime
from db_conn import db_conn as db
import time

class c_customers:
   def __init__(self):
      self.date = datetime.datetime.now()
   
   def register(self,customer_info):
      t = datetime.datetime.now().timetuple()
      time_d=time.mktime(t)
      conn=db()
      cursor = conn.cursor()
      cursor.execute('insert into customers(first_name,last_name,birth_date,gender,date_of_registration)values("%s","%s","%s","%s","%s")'
                     %(customer_info[0],customer_info[1],customer_info[2],customer_info[3],self.date))
      conn.commit()
      conn.close()
      return ("Done!!")
   
   def last_inserted_id(self):
      conn=db()
      cursor = conn.cursor()
      return(cursor.lastrowid)
      conn.commit()
      conn.close()
      
   def checkout_books(self,customer_no,books):
      
      conn = db()
      cursor = conn.cursor()
      count = self.list_customers('Select COUNT(*) from customers where customer_no="%d"'%(int(customer_no)))[0][0]
      if (not count):
         return ("Customer with id %s does not exist!"%customer_no)
      for book in books:
         cursor.execute('Select checkout_no from checkout where book_no="%s"'%(int(book)))
         if(not cursor.fetchall()):
            cursor.execute('insert into checkout(customer_no,book_no,checkout_Date)values("%d","%d","%s")'
                           %(int(customer_no),int(book),self.date))
            conn.commit()
            conn.close()
         else:
            return("The book number %s is already borrowed!"%book)
      return("Done!!")

   def return_books(self,books):
      conn = db()
      cursor = conn.cursor()
      for book in books:
         cursor.execute('Select checkout_no from checkout where book_no="%s" and returned_date is null'%(int(book)))
         if (cursor.fetchall()):
            cursor.execute('update checkout set returned_date="%s" where book_no="%s"'%(self.date,book))
            conn.commit()
            conn.close()
         else:
            return("the book number %s is already returned for this checkout->"%book)
      return("Done!!")
      
   def del_customer(self,customer_number):
      conn = db()
      cursor = conn.cursor()
      cursor.execute('delete from customers where customer_no=%s'%customer_number)
      conn.commit()
      conn.close()  

   def list_customers(self,select_query):
      conn = db()
      cursor = conn.cursor()
      res=cursor.execute(select_query)
      res=res.fetchall()
      conn.close()
      return(res)
   
customers=c_customers()
            

