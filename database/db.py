from tinydb import TinyDB, Query
from tinydb.database import Document
from pprint import pprint
import json
import os 
User = Query()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(BASE_DIR)
os.makedirs(DATABASE_DIR, exist_ok=True)

db1=TinyDB('database/users.json', indent=4)
db2=TinyDB('database/large_data.json', indent=4)

users     = db1.table('Users')
stage     = db1.table('Stage')
index     = db1.table('Index')

def get(table=None, user_id=None, dictionary_type=None, uniq_id=None):

    # if table == "stage":
    #     return stage.get(doc_id=user_id)
    # if uniq_id != None:
    #     print(uniq_id)
    #     uniq_id = int(uniq_id)
    #     return db2.search(Query().uniq_id == uniq_id)
    if table == "users":
        if user_id == None:
            return users.all()
        else:
            return users.get(doc_id=user_id) 
    elif table == "index":
        return index.get(doc_id=user_id)
    
    elif table == "dictionary":
        tip = Query()
        # if user_id != None:
        #     return db2.search(tip.user_id == user_id)
        
        # elif user_id==None and dictionary_type == None:
        #     pprint(db2.all())
        #     return db2.all()
        if dictionary_type != None:
            return db2.search(tip.dictionary_type == dictionary_type)

def insert(table, data, user_id=None, dictionary_type=None):

    file_mapping = {
        "Essential1": os.path.join(DATABASE_DIR, 'essential1.json'),
        "Essential2": os.path.join(DATABASE_DIR, 'essential2.json'),
        "ELS": os.path.join(DATABASE_DIR, 'els.json')
    }
    
    if table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "index":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index.insert(doc)

    elif table == "Essential1" or table == "Essential2" or table == "ELS":
        file_path = file_mapping.get(table)
    
    if not file_path:
        raise ValueError(f"Jadval nomi noto‘g‘ri: {table}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return f"{file_path} ga ma'lumot saqlandi!"
       
def upd(table, data, user_id=None, product=None):
    # if table == "stage":
    #     stage.update(data, doc_ids=[user_id])
    
    if table == "index":
        index.update(data, doc_ids=[user_id])
    # if table == "dictionary":
    #     user_ids = int(get(table="index", user_id=user_id)["edit_doc"])
    #     print(user_ids)
    #     db2.update(data, doc_ids=[user_ids])
    #     print(db2)
