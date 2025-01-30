# Migrations script for database setup (migrations.py)
import mysql.connector

def create_tables():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="irctc_db"
    )
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            role ENUM('admin', 'user') NOT NULL DEFAULT 'user'
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trains (
            id INT AUTO_INCREMENT PRIMARY KEY,
            train_name VARCHAR(100) NOT NULL,
            source VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            total_seats INT NOT NULL,
            available_seats INT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            train_id INT NOT NULL,
            seat_count INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (train_id) REFERENCES trains(id)
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
