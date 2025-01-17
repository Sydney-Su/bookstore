from flask import Flask, jsonify
from flask_cors import CORS
#import sys      # importing database.py

#sys.path.insert(1, 'C:\\Users\\Sydney\\Desktop\\Projects\\bookstore\\database') # caution: path[0] is reserved for script path (or '' in REPL)
import database
print(database.get_all_books())
app = Flask(__name__)
CORS(app)   # Enable CORS for all routes

print("Functions available in database:", dir(database))

@app.route('/')
def home():
    return "Welcome to the Bookstore API"

@app.route('/books', methods=['GET'])
def get_books():
    books = database.get_all_books()
    return jsonify(books)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)