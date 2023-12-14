from pymongo import MongoClient
from pymongo.server_api import ServerApi


class ClientFactory:

    def get_client(self):
        return MongoClient(
            'mongodb+srv://gmanzini:FiBkHYUbIG69ihx0@cluster0.r7ixqty.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
