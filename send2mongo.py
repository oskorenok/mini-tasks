import pandas as pd
import time
from umongo import MongoHandler

if __name__ ==  '__main__':

    # Reading a .csv file 
    df = pd.read_csv('random_table.csv')
    records = df.to_dict('records')

    handler = MongoHandler(database_name='Test', 
                           collection_name='SingleThread')

    # Sending data to mongo & measuring time
    start = time.time()

    handler.insert_many(records)
    
    stop = time.time()
    print(f"Elapsed time: {stop-start} s")