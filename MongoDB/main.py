
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, ConfigurationError, InvalidName



from appdata_mongodb import *
from seed import *

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f'{error}'
        except IndexError as error:
            return f'{error}'
        except KeyError as error:
            return f'{error}'
        except ServerSelectionTimeoutError:
            return f'{error}'
        except OperationFailure as error:
            return f'{error}'
        except ConfigurationError as error:
            return f'{error}'
        except InvalidName as error:
            return f'{error}'
        except Exception as error:
            return f'{error}'
        finally:
            pass
    return inner


@input_error
def connect_DB(func):
    def wrapper(cats_collection, *args, **kwargs):
        with MongoClient(URI, server_api=ServerApi('1')) as client:
        # Create a new client and connect to the server
            db = client.get_database('ds02')
            cats_collection = db.get_collection('cats')
            # #client.admin.command('ping')
            # # Send a ping to confirm a successful connection
            return func(cats_collection, *args, **kwargs)
    return wrapper

@input_error
@connect_DB
def insert_documents(cats_collection: Collection, data):
    for item in data:
        result_one = cats_collection.insert_one(item)

@input_error
@connect_DB
def read_all_documents(cats_collection: Collection):
    data = cats_collection.find({})
    return tuple(data)

@input_error
@connect_DB
def read_one_document(cats_collection: Collection, nick_name):
    data = cats_collection.find_one({'name':nick_name})
    return data

@input_error
@connect_DB
def update_age_document(cats_collection: Collection, nick_name:str, age: int):
    data = cats_collection.update_one({'name': nick_name}, {'$set': {'age': age}})
    # data = read_one_document('', nick_name)
    return data

@input_error
@connect_DB
def update_features_document(cats_collection: Collection, nick_name:str, features: str):
    data = cats_collection.update_one({'name': nick_name}, {'$addToSet': {'features': features}})
    # data = read_one_document('', nick_name)
    return data
@input_error
@connect_DB
def delete_document(cats_collection: Collection, nick_name:str):
    data = cats_collection.delete_one({'name': nick_name})
    # data = read_one_document('', nick_name)
    return data

@input_error
@connect_DB
def delete_documents(cats_collection: Collection):
    data = cats_collection.delete_many({})
    # data = read_one_document('', nick_name)
    return data

@input_error
def get_list(nick_name: str):
    if len(nick_name) > 0:
        return read_one_document('', nick_name)
    return read_all_documents('')

@input_error
def update_age(nick_name: str, age: str):
    if len(nick_name) > 0 and len(age) > 0:
        return update_age_document('', nick_name, int(age))
    return 'Щось завадило оновленню.'

def menu():
    while True:
        command, *param = input('Введіть команду:').lower().split(' ')
        match command:
            case 'get':
                nick_name = input("Введіть ім'я улюбленця або залишти пустим:")
                print(get_list(nick_name))
            case 'exit':
                break
            case 'update_age':
                nick_name, age = input("Введіть ім'я та вік улюбленця через пробіл:").split(' ')
                print(update_age(nick_name, age))
            case 'add_features':
                nick_name, features = input("Введіть ім'я та нову фічу улюбленця через пробіл:").split(' ')
                print(update_features_document('', nick_name, features))
            case 'delete_cat':
                nick_name = input("Введіть ім'я улюбленця для видалення:")
                print(delete_document('', nick_name))
            case 'delete_all':
                print("Видалення записыв розпочато.")
                print(delete_documents(""))
            case _:
                pass

if __name__ == "__main__":
    delete_documents('')
    data  = generate_fake_data(50)
    insert_documents('', data)
    menu()