import pandas as pd 
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus

db_password = quote_plus(os.environ["mysql_password"])
connection_url = f"mysql+mysqlconnector://root:{db_password}@127.0.0.1:3306/olist"
# mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database>

engine = create_engine(
    connection_url
)
# 
table_names = [
'olist_customers','olist_orders','olist_order_payments','olist_products','olist_sellers','olist_order_items'
]
# D:\LLM_Projects\Text_SQL_LLM_System\dataset\preprocessed_data
for i in range(len(table_names)):
    pth = f"D:/LLM_Projects/Text_SQL_LLM_System/dataset/preprocessed_data/{table_names[i]}.csv"
    df = pd.read_csv(pth)
    df.to_sql(
        table_names[i],
        engine,
        if_exists="append",
        index=False
    )
print("Data Loaded sucessfully")


