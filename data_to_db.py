import mysql.connector
import os
db_password = os.environ['mysql_password']


MYSQL_CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":db_password,
    # "database":"mavenfuzzyfactory",
    "port":3306
    
}

conx = mysql.connector.connect(**MYSQL_CONFIG)

cursor = conx.cursor()

cursor.execute("""
            CREATE DATABASE IF NOT EXISTS olist
            DEFAULT CHARACTER SET utf8mb4
            COLLATE utf8mb4_unicode_ci          
               """
               )
cursor.execute("USE olist")

create_customers = """
CREATE TABLE IF NOT EXISTS olist_customers(
customer_id VARCHAR(50) PRIMARY KEY,
customer_unique_id VARCHAR(50),
customer_zip_code_prefix INT,
customer_city VARCHAR(100),
customer_state CHAR(2)
) Engine=InnoDB
CHARSET = utf8mb4
COLLATE=utf8mb4_unicode_ci;
""" 

create_olist_products = """
CREATE TABLE IF NOT EXISTS olist_products (
    product_id VARCHAR(50) NOT NULL,
    product_category_name VARCHAR(100),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g DECIMAL(10,2),
    product_length_cm DECIMAL(10,2),
    product_height_cm DECIMAL(10,2),
    product_width_cm DECIMAL(10,2),

    PRIMARY KEY (product_id)
) ENGINE=InnoDB
CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
""" 
create_olist_orders = """
CREATE TABLE IF NOT EXISTS olist_orders (
    order_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    order_status VARCHAR(20),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,

    PRIMARY KEY (order_id), 
    FOREIGN KEY (customer_id)
        REFERENCES olist_customers(customer_id)
) ENGINE=InnoDB
CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
"""


create_olist_sellers = """
CREATE TABLE IF NOT EXISTS olist_sellers (
    seller_id VARCHAR(50) NOT NULL,
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state CHAR(2),

    PRIMARY KEY (seller_id)
) ENGINE=InnoDB
CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
"""

create_olist_order_payments = """
CREATE TABLE IF NOT EXISTS olist_order_payments (
    order_id VARCHAR(50) NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type VARCHAR(30),
    payment_installments INT,
    payment_value DECIMAL(10,2),

    PRIMARY KEY (order_id, payment_sequential),

    FOREIGN KEY (order_id)
        REFERENCES olist_orders(order_id)
) ENGINE=InnoDB
CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
"""

create_order_items = """
CREATE TABLE IF NOT EXISTS olist_order_items(
    order_id VARCHAR(50) NOT NULL,
    order_item_id INT NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    seller_id VARCHAR(50) NOT NULL,
    shipping_limit_date DATETIME,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),

    PRIMARY KEY (order_id, order_item_id),

    FOREIGN KEY (order_id)
        REFERENCES olist_orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES olist_products(product_id),
    FOREIGN KEY (seller_id)
        REFERENCES olist_sellers(seller_id)
) ENGINE=InnoDB
CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

"""
tables = [
create_customers,
create_olist_orders,
create_olist_products,
create_olist_sellers,
create_olist_order_payments,
create_order_items
]

for table_sql in tables:
    cursor.execute(table_sql)

conx.commit() # permanently saves all changes made to a database during the current transaction
