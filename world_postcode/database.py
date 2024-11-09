import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Connected to database {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print(f"Connection to database {self.db_name} closed")

# Example usage
if __name__ == "__main__":
    db = Database("example.db")
    db.connect()
    db.close()