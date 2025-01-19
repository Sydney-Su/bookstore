## **1/15/2025**
- Created repository on GitHub
- Used git to clone repository onto VS Code
- Created a new virtual environment and activated it
- Installed flask
- Installed PostgreSQL
- Created a rough database and tables, tested inserting and selecting data

```bash
psql -U postgres -d bookstore -f database/seed_data.sql
psql -U postgres -d bookstore
```

## **1/16/2025**

- Added some basic API endpoints
- Installed Node.js and spent a long time figuring out how to set up a simple working front end to connect to my working backend

```jsx
npx create-react-app my-app
```

- Learned that you run backend and frontend on two different ports during development
- Learned CORS (cross-origin resource sharing) - allows frontend to communicate to backend on different ports without issues

```jsx
front end: from my-react-bookstore folder → npm start
back end: from api folder → flask run
activate virtual environment: .\venv\Scripts\activate
```

## 1/18/2025

- Added a way for users to add books to the library through a form and button
- Sent book data from front end (React) to back end (Flask) and then added to the database (PostgreSQL)
- Spend wayyy too long debugging this

```python
BAD (need parentheses around inserted values and comma at end):
cursor.execute(
        "INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)",
            title, author, price, published_date
)

GOOD:
cursor.execute(
        "INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)",
            (title, author, price, published_date),
)
```