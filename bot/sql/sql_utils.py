import sqlite3
from sqlite3 import Error

def show_categories():
    try:
        conn = sqlite3.connect('bot.db')
        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM 'categories'
        """
        cursor.execute(query)
        categories = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories
    
def print_products(product_id):
    try:
        conn = sqlite3.connection('bot.db')
        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM 'products'
        WHERE 'parent_id' =:product_id
        """
        cursor.execute(query, {'product_id': product_id})
        products = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return products


