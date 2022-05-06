from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Connect Flask to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Attach Flask app to database
db = SQLAlchemy(app)


# Creation of Project Objects
class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    created_by = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, nullable=False)
    updated_by = db.Column(db.Text, nullable=False)

    def __init__(self, id, project_id, category_id, name, description, amount,
                 created_at, created_by, updated_at, updated_by):
        self.id = id
        self.project_id = project_id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by

    def json(self):
        expense_entry = {
            "id": self.id,
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "amount": self.amount,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "updated_at": self.updated_at,
            "updated_by": self.updated_by
        }
        return expense_entry
