# database.py
import psycopg2

# Establish and return a connection to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        dbname="bookstore",
        user="postgres",
        password="john3:16_!",
        host="localhost"
    )

# Get a connection then fetch all books from the PostgreSQL database
def get_all_books():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return books

# Add a book to the PostgreSQL database
def add_book(title, author, price, published_date):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)",
            (title, author, price, published_date),
    )
    connection.commit()
    cursor.close()
    connection.close()