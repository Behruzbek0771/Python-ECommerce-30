from datetime import datetime
import json


class Product:
    
    def __init__(
            self,
            id,
            name,
            description,
            price,
            quantity,
            category,
            brand,
            in_stock,
            created_at,
            updated_at,
        ) -> None:
        
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category
        self.brand = brand
        self.in_stock = in_stock
        self.created_at = created_at
        self.updated_at = updated_at
        
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "price":self.price,
            "quantity":self.quantity,
            "category":self.category,
            "brand":self.brand,
            "in_stock":self.in_stock,
            "created_at":self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "updated_at":self.updated_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        
    @classmethod
    def from_dict(cls, data:dict):
        data = cls(
            id = data['id'],
            name = data['name'],
            description = data['description'],
            price = data['price'],
            quantity = data['quantity'],
            category = data['category'],
            brand = data['brand'],
            in_stock = data['in_stock'],
            created_at = datetime.strptime(data['created_at'],"%Y-%m-%dT%H:%M:%SZ"),
            updated_at =  datetime.strptime(data['updated_at'],"%Y-%m-%dT%H:%M:%SZ"),
        )
        
        return data
    
    @classmethod
    def loads_product(cls):
        with open("database/products.json",'r',encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
            product = []
            for item in data:
                product.append(cls.from_dict(item))
            
            return product
        
    @classmethod
    def filter_price(cls):
        price = float(input("enter price : "))
        products = cls.loads_product() 
        for product in products:
            if product.price > price:
                print(product)
                
    
    def __str__(self):
        return f"{self.id}-id  {self.name}  {self.price} so'm"