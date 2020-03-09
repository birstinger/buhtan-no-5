from pymongo import MongoClient
import ssl
import os
from dotenv import load_dotenv



# This should be used to connect to the database remotely
# username and password should be called externally
# Variable references:
# info --Dict object
# tb -- String Object
# curr -- Dict Object
# new_data -- Dict Object

# connects to the mongo atlas
def connector():
    env_path = os.path.abspath(os.path.dirname(__file__))
    location = os.path.join(env_path, '.env')
    load_dotenv(dotenv_path=location)
    client = MongoClient(
        "mongodb+srv://Engine:qhcFrP65n8joJvso@cluster0-v76zg.mongodb.net/test?retryWrites=true&w=majority", ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE)#MongoClient(os.getenv('MongoURL'))
    db = client["StudyStore"]
    return db
# returns the whole database name "StudyStore"


# deletes JSON in collection tb based on info
def delete(tb, info):
    connect = connector()[tb]
    connect.delete_many(info)
 # no return 

# Updates a JSON that was already store in the database
# curr is the JSON in database 
# new_data is new JSON waiting to be stored in the database
def edit(tb, curr, new_data):
    connect = connector()[tb]
    connect.update_many(curr, new_data)
 # no return

#Gets a JSON in collection tb in database based on info
def get(tb, info):
    connect = connector()
    locate = connect[tb]
    check = locate.find(info)
    return check
# return list of dicts based off info

#Post info into the database in the collection tb
def post(tb, info):
    connect = connector()
    locate = connect[tb]
    if isinstance(info, list):
        locate.insert_many(info)
    else:
        locate.insert_one(info)


def filtered(tb, info):
    filler = get(tb, info)
    search = filler.sort(info, 1)
    return search
# returns list of dicts based off info that is sorted


if __name__ == '__main__':
    connector()
    poster = {"id": 0, "Name": "Hey", "credits": 234, "Researcher": True}
    edits = {"$set": {"Name": "Canyon 123"}}
    find = {"Name": "Canyon 123"}
    delete = {"Name": {"$regex": "^H"}}

    post("Users", poster)
    edit("Users", poster, edits)
    time = get("Users", find)
