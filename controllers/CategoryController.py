from flask import jsonify, request
from models.CategoryModel import Category

def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

def get_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(category.to_dict())

def add_category():
    new_category_data = request.get_json()
    new_category = Category(name=new_category_data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully!', 'category': new_category.to_dict()})

def update_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    updated_data = request.get_json()
    category.name = updated_data.get('name', category.name)
    db.session.commit()
    return jsonify({'message': 'Category updated successfully!', 'category': category.to_dict()})

def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})