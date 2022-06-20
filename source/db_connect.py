#%%
from mysql.connector import connect, Error
from decouple import config
from datetime import date
import pandas as pd
#%%

try:
    with connect(
        host=config('dbhost'),
        user=config('dbusername'),
        password=config("dbpassword"),
        database=config('database'),

    ) as connection:
          sql_query = pd.read_sql_query ('''
                              SELECT * FROM wp_fluentform_submissions WHERE form_id = 9
                               ''', connection)

          df = pd.DataFrame(sql_query)
          print (df)
          print(connection)
except Error as e:
    print(e)