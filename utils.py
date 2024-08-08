


import psycopg2

from models import Book

def conn_db(fun):
    
    def wrap(*arg, **kwarg):
        with psycopg2.connect("dbname=test user=postgres host=localhost port=5432 password=20072604sh") as conn:
            cur = conn.cursor()
            fun(cur,*arg, **kwarg)
            
    return wrap



@conn_db
def all_books(cur):
    
    # Execute a query
    cur.execute("SELECT * FROM books")

    # Retrieve query results
    records = cur.fetchall()
    for i in records:
        book = Book(*i)
        print(book)

@conn_db
def get_book_by_id(cur, id):
    cur.execute(f"SELECT * FROM books where id={id}") 
    book = cur.fetchone()
    print(Book(*book))






