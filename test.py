from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI as necessary
db = client['mydatabase']  # Replace with your database name
collection = db['books']  # Replace with your collection name

# Function to generate a fake book
def generate_fake_book():
    total_copies = random.randint(1, 100)
    available_copies = random.randint(0, total_copies)  # Ensure available copies <= total copies
    return {
        "title": fake.catch_phrase(),
        "author": fake.name(),
        "isbn": fake.isbn13(),
        "publishedDate": datetime.strptime(str(fake.date_between(start_date='-10y', end_date='today')), "%Y-%m-%d"),
        "totalCopies": total_copies,
        "availableCopies": available_copies,
        "genre": random.choice(['Fiction', 'Non-Fiction', 'Science', 'Fantasy', 'Mystery', 'Romance'])
    }

# Insert 1000 fake books into the collection
books_to_insert = [generate_fake_book() for _ in range(1000)]
collection.insert_many(books_to_insert)

print("1000 fake books inserted successfully!")
