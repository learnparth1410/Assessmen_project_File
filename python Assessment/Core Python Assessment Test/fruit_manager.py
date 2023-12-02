import json

class FruitManager:
    STOCK_FILE = "fruit_stock.json"

    @staticmethod
    def load_stock():
        try:
            with open(FruitManager.STOCK_FILE,'r') as file:
                stock = json.load(file)
        except FileNotFoundError:
            stock = {}
        return stock
    

    @staticmethod
    def save_stock(stock):
        with open(FruitManager.STOCK_FILE,'w') as file:
            json.dump(stock,file)

    
    @staticmethod
    def add_fruit_stock(fruit,quantity):
        stock = FruitManager.load_stock()
        stock[fruit] = stock.get(fruit,0) + quantity
        FruitManager.save_stock(stock)

    
    @staticmethod
    def view_fruit_stock():
        stock = FruitManager.load_stock()
        print("\nFruit stock:")
        for fruit,quantity in stock.items():
            print(f"{fruit}:{quantity}")
        print("")

    @staticmethod
    def update_fruit_stock(fruit,new_quantity):
        stock = FruitManager.load_stock()
        stock[fruit] = new_quantity
        FruitManager.save_stock(stock)


FruitManager.add_fruit_stock("apple", 10)
FruitManager.view_fruit_stock()
FruitManager.update_fruit_stock("apple", 20)
FruitManager.view_fruit_stock()



    
