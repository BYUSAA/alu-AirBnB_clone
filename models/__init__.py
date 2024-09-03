from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

def get_storage():
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        return DBStorage()
    else:
        return FileStorage()

storage = get_storage()
storage.reload()
