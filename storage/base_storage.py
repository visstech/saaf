from abc import ABC, abstractmethod

class BaseStorage(ABC):
    """
    Abstract base class for all storage implementations in SAAF.

    Any storage system like:
    - SQLite
    - PostgreSQL
    - MongoDB
    - Vector Database

    must implement these methods.
    """

    @abstractmethod
    def save(self, *args, **kwargs):
        """
        Store data into the storage system.
        """
        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        """
        Retrieve data from the storage system.
        """
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Update existing data in the storage system.
        """
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        """
        Delete data from the storage system.
        """
        pass