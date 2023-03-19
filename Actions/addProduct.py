from DB import createDB 


def addProduct(name, product , amount, spending, price):
    newProduct = (product , amount, spending, price)
    add = f"INSERT OR REPLACE INTO {name} VALUES(?, ?, ?, ?);"
    createDB.curMain.execute(add, newProduct)