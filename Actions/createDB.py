import sqlite3


def createDb(name: str = ''):
    conMain = sqlite3.connect(f'{name}.db')
    curMain = conMain.cursor()
    
    createMain = f'CREATE TABLE IF NOT EXISTS {name}(product TEXT UNIQUE, amount INT, spending INT, price INT);'
    create = f'CREATE TABLE IF NOT EXISTS {name}_sales(id INT PRIMARY KEY, product TEXT, amount INT, price INT, date timestamp);'
    
    curMain.execute(createMain)
    curMain.execute(create)