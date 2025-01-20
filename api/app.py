from flask import Flask, jsonify, request, redirect, render_template
from flask_cors import CORS
#import sys      # importing database.py

#sys.path.insert(1, 'C:\\Users\\Sydney\\Desktop\\Projects\\bookstore\\database') # caution: path[0] is reserved for script path (or '' in REPL)
import database

app = Flask(__name__)
CORS(app)   # Enable CORS for all routes

# root directory
@app.route('/')
def home():
    return "Welcome to the Bookstore API"

# display all book entries
@app.route('/books', methods=['GET'])
def get_books():
    books = database.get_all_books()
    return jsonify(books)

# create a book entry
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    
    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    published_date = data.get('published_date')
    
    if not all([title, author, price, published_date]):
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        database.add_book(title, author, price, published_date)
        return jsonify({"message": "Book added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data
        book_title = request.form['bookTitle']
        author = request.form['author']
        
        # Process form data (e.g., store it in the database)
        # For now, we'll just print it to the console
        print(f"Book Title: {book_title}, Author: {author}")
        
        # Redirect to a different page after submission (optional)
        return redirect('/book_list')  # Redirect to the book list page (adjust as needed)
    
    return render_template('add_book.html')  # Render the form page when the user accesses this route

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)