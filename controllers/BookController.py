from flask import jsonify, request
from models.BookModel import Book
from models.CategoryModel import Category

def get_books():
    books = Book.query.all()
    books_with_categories = []

    for book in books:
        category = Category.query.get(book.category_id)
        books_with_categories.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'category_name': category.name if category else "No Category"
        })

    response = {
        'status': 'success',
        'data': {
            'books': books_with_categories
        },
        'message': 'Books retrieved successfully'
    }

    return jsonify(response), 200

# Get a single book with category name

def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'status': 'error', 'message': 'Book not found'}), 404

    category = Category.query.get(book.category_id)

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'category_name': category.name if category else "No Category"
    }

    response = {
        'status': 'success',
        'data': {
            'book': book_data
        },
        'message': 'Book retrieved successfully'
    }

    return jsonify(response), 200




    # Add a new book (POST)
def add_book():
    new_book_data = request.get_json()

    new_book = Book(
        title=new_book_data['title'],
        author=new_book_data['author'],
        description=new_book_data.get('description', ''),
        category_id=new_book_data['category_id']  # Menghubungkan books dengan category
    )

    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!', 'book': new_book.to_dict()}), 201

# Update a book (PUT)

def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    updated_data = request.get_json()
    book.title = updated_data.get('title', book.title)
    book.author = updated_data.get('author', book.author)
    book.year = updated_data.get('year', book.year)
    book.category_id = updated_data.get('category_id', book.category_id)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully!', 'book': book.to_dict()})

# Update a book (PATCH)

def patch_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    updated_data = request.get_json()

    # Perbarui hanya jika data tersebut diberikan
    if 'title' in updated_data:
        book.title = updated_data['title']
    if 'author' in updated_data:
        book.author = updated_data['author']
    if 'year' in updated_data:
        book.year = updated_data['year']
    if 'category_id' in updated_data:
        # Pastikan kategori ada sebelum meng-update
        category = Category.query.get(updated_data['category_id'])
        if category:
            book.category_id = updated_data['category_id']
        else:
            return jsonify({'error': 'Category not found'}), 404
        

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted successfully!'})
