import React, { useState } from 'react';

function AddBookForm() {
    // State to track form inputs
    const [bookTitle, setBookTitle] = useState('');
    const [bookAuthor, setBookAuthor] = useState('');
    const [bookPrice, setBookPrice] = useState('')
    const [bookPublishedDate, setBookPublishedDate] = useState('')

    // Handlers for input changes
    const handleTitleChange = (event) => setBookTitle(event.target.value); 
    const handleAuthorChange = (event) => setBookAuthor(event.target.value);
    const handlePriceChange = (event) => setBookPrice(event.target.value);
    const handlePublishedDateChange = (event) => setBookPublishedDate(event.target.value);

    // Form submission handler
    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent page reload
        console.log(`Title: ${bookTitle}, Author: ${bookAuthor}, Price: ${bookPrice}, Published Date: ${bookPublishedDate}`);

        const newBook = { title: bookTitle, author: bookAuthor, price: bookPrice, published_date: bookPublishedDate };
        try {
            const response = await fetch('http://localhost:5000/books', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(newBook),
            });
            const data = await response.json();
            console.log('Book added:', data);
          } catch (error) {
            console.error('Error adding book:', error);
        }
        
        // reset form
        setBookTitle('')
        setBookAuthor('')
        setBookPrice('')
        setBookPublishedDate('')
    };
        

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Book Title:</label>
                <input
                    type="text"
                    value={bookTitle}
                    onChange={handleTitleChange}
                    placeholder="Enter the book title"
                />
            </div>
            <div>
                <label>Book Author:</label>
                <input
                    type="text"
                    value={bookAuthor}
                    onChange={handleAuthorChange}
                    placeholder="Enter the book author"
                />
            </div>
            <div>
                <label>Book Price:</label>
                <input
                    type="number"
                    step='0.01'
                    value={bookPrice}
                    onChange={handlePriceChange}
                    placeholder="Enter the book price"
                />
            </div>
            <div>
                <label>Book Published Date:</label>
                <input
                    type="text"
                    value={bookPublishedDate}
                    onChange={handlePublishedDateChange}
                    placeholder="Enter the book publication date"
                />
            </div>
            <button type="submit">Add Book</button>
        </form>
    );
}

export default AddBookForm;