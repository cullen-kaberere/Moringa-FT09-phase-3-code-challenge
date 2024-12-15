from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Add sample authors
    author1_id = Author.create(cursor, "John Doe")
    author2_id = Author.create(cursor, "Jane Smith")
    author3_id = Author.create(cursor, "Cullen")  # New Author

    # Add sample magazines
    magazine1_id = Magazine.create(cursor, "Tech Weekly", "Technology")
    magazine2_id = Magazine.create(cursor, "Health Today", "Health")
    magazine3_id = Magazine.create(cursor, "Kenya Daily", "Current Affairs")  

    # Add sample articles
    article1_id = Article.create(cursor, "AI in 2024", "An overview of AI advancements.", author1_id, magazine1_id)
    article2_id = Article.create(cursor, "Healthy Living", "Tips for a healthier life.", author2_id, magazine2_id)
    article3_id = Article.create(cursor, "Demos in Kenya", "An analysis of recent political demonstrations.", author3_id, magazine3_id)  

    conn.commit()

    # Fetch and display the data
    print("\nAuthors:")
    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nMagazines:")
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nArticles:")
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    conn.close()

if __name__ == "__main__":
    main()
