import multiprocessing as mp
import pandas as pd
import time
from umongo import MongoHandler

# Takes a array/list and integer chunk_size as input 
# and returns generator objects of n lengths from that list
def chunks(array, chunk_size):
    for i in range(0, len(array), chunk_size):
        yield array[i:i + chunk_size]
    

def insert(chunk):
    # Define a client inside a function
    handler = MongoHandler(database_name='Test', 
                           collection_name='MultiThread')

    handler.insert_many(chunk)

if __name__ ==  '__main__':
    chunk_size = 10000

    # Reading a .csv file 
    df = pd.read_csv('random_table.csv')
    records = df.to_dict('records')

    # Pool object creation, sending data to mongo & measuring time
    start = time.time()

    pool = mp.Pool(processes=8)
    result = pool.map(insert, list(chunks(records, chunk_size)))
    pool.close()

    stop = time.time()

    print(f"Elapsed time: {stop-start} s")