import json
from sys import exit
from models.product import Product
from models.user import User
from utils.printers import print_menu

while True:
    print_menu()
    
    tanlov = int(input("tanlang : "))
    if tanlov == 1:
        User.create_user()

    elif tanlov == 2:
        products = Product.loads_product()

        for product in products:
            print(product)
            
        print("Sotib olmoqchi bo'lgan mahsulotingiz narxi qanchadan yuqori bo'lishi kerak! \n")
        Product.filter_price()

        product_tanlang = int(input("Sotib olmoqchi bo'lgan mahsulotingiz ID sini kiriting: \n"))

        for product in products:
            if product.id == product_tanlang:
                if product.quantity > 0:
                    product.quantity -= 1
                else:
                    print("Bu mahsulot tugagan!")

        product_dicts = [p.to_dict() for p in products]

        with open("database/products.json", 'w', encoding="utf-8") as jsonfile:
            json.dump(product_dicts, jsonfile, ensure_ascii=False, indent=4)

    elif tanlov == 0:
        exit(0)