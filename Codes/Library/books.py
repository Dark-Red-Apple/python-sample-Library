#Author:Alma, 2019
#Book class
import json
import uuid 
from db_conn import db_conn as db

class c_books:
   def __init__(self):
      self.format = ''
   
   def build_sample_books(self,file_name):
      conn=db()
      cursor = conn.cursor()
   
      with open (file_name,'r') as myfile:
         default_books = json.load(myfile)
      for book in default_books['books'] :
         cursor.execute('insert into books(author,name,summary,publish_date,number_of_copies,Is_available)values("%s","%s","%s","%s","1","yes")'
                        %( book['author'],book['title'],book['description'],book['published']))
         
      conn.commit()
      conn.close()
      
   def add_book(self,book_info):
      conn = db()
      cursor = conn.cursor()
      cursor.execute('insert into books(author,name,summary,publish_date,number_of_copies,Is_available)values("%s","%s","%s","%s","1","%s")'
                     %(book_info['author'],book_info['title'],book_info['description'],book_info['year'],book_info['available']))
      conn.commit()
      conn.close()
      return('Done!!')
      
   def del_book(self,book_number):
      conn = db()
      cursor = conn.cursor()
      cursor.execute('delete from books where book_no=%s'%book_number)
      conn.commit()
      conn.close()
   
   def list_books(self,select_query):
      conn = db()
      cursor = conn.cursor()
      res=cursor.execute(select_query)
      res=res.fetchall()
      conn.close()
      return(res)
      
books=c_books()           

