import json
import sqlite3
import os
from saaf.models.memory import Memory
from saaf.storage.base_storage import BaseStorage
from saaf.config.settings import DATABASE_PATH


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
        self.initialize()

    def initialize(self):
        """
        Initialize database connection
        and create required tables.
        """

        folder = os.path.dirname(DATABASE_PATH)

        if folder:
            os.makedirs(
                folder,
                exist_ok=True
            )
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
        
        

    def save(self, memory: Memory):
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
            value = getattr(memory, field)
            if value is None:
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
                memory.user_id,
                memory.memory_key
            )
        )


        existing = cursor.fetchone()


        json_value = json.dumps(
                memory.memory_value
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
                    memory.memory_type,
                    memory.importance,
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
                    memory.user_id,
                    memory.memory_key,
                    json_value,
                    memory.memory_type,
                    memory.importance
                )
            )


        self.connection.commit()

        return cursor.lastrowid


    def get(self,user_id: str,memory_key: str) -> Memory | None:
        """
        Retrieve memory from SQLite.
        """

        query = """
        SELECT
            user_id,
            memory_key,
            memory_value,
            memory_type,
            importance,
            created_at,
            updated_at

        FROM memories

        WHERE user_id = ?
        AND memory_key = ?
        """

        cursor = self.connection.cursor()

        cursor.execute(
            query,
            (
                user_id,
                memory_key
            )
        )

        result = cursor.fetchone()


        if result is None:
            return None


        return Memory(
                    user_id=result[0],
                    memory_key=result[1],
                    memory_value=json.loads(result[2]),
                    memory_type=result[3],
                    importance=result[4]
                    )


    def update(self, memory: Memory) -> bool:
        """
        Update an existing memory.
        """

        required_fields = [
            "user_id",
            "memory_key",
            "memory_value",
            "memory_type",
            "importance"
        ]

        for field in required_fields:
            value = getattr(memory, field)
            if value is None:
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
                memory.user_id,
                memory.memory_key
            )
        )


        result = cursor.fetchone()


        if result is None:
            raise ValueError(
                "Memory does not exist."
            )


        update_query = """
        UPDATE memories

        SET memory_value = ?,
            memory_type = ?,
            importance = ?,
            updated_at = CURRENT_TIMESTAMP

        WHERE user_id = ?
        AND memory_key = ?
        """


        cursor.execute(
            update_query,
            (
                json.dumps(memory.memory_value),
                memory.memory_type,
                memory.importance,
                memory.user_id,
                memory.memory_key
            )
        )


        self.connection.commit()


        return True


    def delete(self,user_id: str,memory_key: str) -> bool:
        """
        Delete an existing memory.
        """

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
                user_id,
                memory_key
            )
        )

        result = cursor.fetchone()


        if result is None:
            raise ValueError(
                "Memory does not exist."
            )


        delete_query = """
        DELETE FROM memories
        WHERE user_id = ?
        AND memory_key = ?
        """


        cursor.execute(
            delete_query,
            (
                user_id,
                memory_key
            )
        )


        self.connection.commit()


        return True