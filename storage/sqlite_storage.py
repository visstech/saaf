import sqlite3

from storage.base_storage import BaseStorage
from config.settings import DATABASE_PATH


class SQLiteStorage(BaseStorage):
    """
    SQLite implementation of SAAF storage.

    Responsible for:
    - Database connection
    - Table initialization
    - CRUD operations
    """

    def __init__(self):
        self.connection = None


    def initialize(self):
        """
        Initialize database connection
        and create required tables.
        """

        self.connection = sqlite3.connect(
            DATABASE_PATH
        )

        self.create_tables()


    def create_tables(self):
        """
        Create memory table.
        """

        query = """
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            memory_key TEXT NOT NULL,
            memory_value TEXT NOT NULL,
            memory_type TEXT,
            importance INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        self.connection.commit()
    def save(self, *args, **kwargs):
        pass


    def get(self, *args, **kwargs):
        pass


    def update(self, *args, **kwargs):
        pass


    def delete(self, *args, **kwargs):
        pass