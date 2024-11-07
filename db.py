
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['kiosco']  


productos_collection = db['productos']
