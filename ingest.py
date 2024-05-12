import pymongo
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


def connect(conn_str, db, coll):

    # Establish connection to MongoDB
    client = pymongo.MongoClient(conn_str)

    # Access database,
    db = client[db]

    # Access a specific collection in the database, replace 'your_collection' with your actual collection name
    collection = db[coll]
    
    return collection
    
def get_data(loc_state):
    
    print(loc_state)

    data =pd.DataFrame(list(collection.find({"location.state":loc_state}).limit(10)))
    return data
