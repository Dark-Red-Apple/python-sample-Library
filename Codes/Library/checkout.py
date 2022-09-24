#Author:Alma, 2019
#Book checkout
import datetime
from db_conn import db_conn as db

class c_checkout:
   def __init__(self):
      self.date=datetime.datetime.now()
   
   def update_checkout(self,checkout_number):
      conn = db()
      cursor = conn.cursor()
      cursor.execute('delete from checkout where checkout-no=%s'%checkout_number)
      onn.commit()
      conn.close()
      
   def del_checkout(self,checkout_info):
      conn = db()
      cursor = conn.cursor()
      cursor.execute('update checkout set returned_date="%s" where checkout_no=%s'%(checkout_info,customer_number))
      conn.commit()
      conn.close()

   def list_checkout(self,select_query):
      conn = db()
      cursor = conn.cursor()
      res=cursor.execute(select_query)
      res=res.fetchall()
      conn.close()
      return(res)
   
checkout=c_checkout()

            

