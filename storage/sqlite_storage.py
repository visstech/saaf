import json
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
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, memory_key)
        )
        """

        cursor = self.connection.cursor()

        cursor.execute(query)

        self.connection.commit()
        
        

    def save(self, memory):
        """
        Insert new memory or update existing memory.
        """

        required_fields = [
            "user_id",
            "memory_key",
            "memory_value",
            "memory_type",
            "importance"
        ]

        for field in required_fields:
            if field not in memory:
                raise ValueError(
                    f"{field} is missing."
                )


        check_query = """
        SELECT id
        FROM memories
        WHERE user_id = ?
        AND memory_key = ?
        """


        cursor = self.connection.cursor()


        cursor.execute(
            check_query,
            (
                memory["user_id"],
                memory["memory_key"]
            )
        )


        existing = cursor.fetchone()


        json_value = json.dumps(
            memory["memory_value"]
        )


        if existing:

            update_query = """
            UPDATE memories

            SET memory_value = ?,
                memory_type = ?,
                importance = ?,
                updated_at = CURRENT_TIMESTAMP

            WHERE id = ?
            """


            cursor.execute(
                update_query,
                (
                    json_value,
                    memory["memory_type"],
                    memory["importance"],
                    existing[0]
                )
            )


        else:

            insert_query = """
            INSERT INTO memories
            (
                user_id,
                memory_key,
                memory_value,
                memory_type,
                importance
            )

            VALUES (?, ?, ?, ?, ?)
            """


            cursor.execute(
                insert_query,
                (
                    memory["user_id"],
                    memory["memory_key"],
                    json_value,
                    memory["memory_type"],
                    memory["importance"]
                )
            )


        self.connection.commit()

        return cursor.lastrowid


    def get(self, *args, **kwargs):
        pass


    def update(self, *args, **kwargs):
        pass


    def delete(self, *args, **kwargs):
        pass