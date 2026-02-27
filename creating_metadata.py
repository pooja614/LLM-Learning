import mysql.connector
import os
import json

db_password = os.environ['mysql_password']


MYSQL_CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":db_password,
    "database":"olist",
    "port":3306
    
}

def normalize_type(db_type:str) -> str:
    return db_type.split("(")[0].upper()




conx = mysql.connector.connect(**MYSQL_CONFIG)

cursor = conx.cursor()

cursor.execute("SHOW TABLES")
table_list = cursor.fetchall()
metadata = []

for (table_name,) in table_list:
    cursor.execute(f"DESCRIBE {table_name}")
    desc = cursor.fetchall()
    
    for col_desc in desc:
        metadata.append({
            "table": table_name,
            "column": col_desc[0],
            "type":normalize_type(col_desc[1]),
            "description":col_desc[3]
        })

path = "D:/LLM_Projects/Text_SQL_LLM_System/metadata/"
with open(path + 'schema_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)





# [
#   {
#     "table": "orders",
#     "column": "order_id",
#     "type": "INT",
#     "description": "Unique identifier for each order"
#   },
#   {
#     "table": "orders",
#     "column": "order_date",
#     "type": "DATETIME",
#     "description": "Date and time when the order was placed"
#   },
#   {
#     "table": "orders",
#     "column": "customer_id",
#     "type": "INT",
#     "description": "References customers.customer_id to link an order to a customer"
#   },
#   {
#     "table": "customers",
#     "column": "customer_id",
#     "type": "INT",
#     "description": "Unique identifier for each customer"
#   },
#   {
#     "table": "customers",
#     "column": "country",
#     "type": "VARCHAR",
#     "description": "Country where the customer is located"
#   }

# ]
