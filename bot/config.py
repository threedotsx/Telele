import os

import sqlite3
from sqlite3 import Error

token = "1575547724:AAF9mXtBUyOt4oH3l3xAfyA2an-6hCzYLvk"

TOKEN = token
about_path = 'https://github.com/olkhovichs/groceryShop_TelegramBot/blob/master/README.md'
'''
def create_products_table():
    id = list()


    try:
        conn = sqlite3.connection('/Users/semenolhovic/Python_Projects/groceryShop/bot/sql/bot.db')
        cursor = conn.cursor()
        with conn:
            for i in range(1, 5):
                id.append(i)
                query = """
                INSERT INTO 'products'
                VALUES(?, ?)
                """, (id)
'''