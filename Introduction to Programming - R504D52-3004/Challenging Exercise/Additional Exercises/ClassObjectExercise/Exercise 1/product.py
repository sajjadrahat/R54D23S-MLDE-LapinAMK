class Product:
    product_id_starter = 0
    def __init__(self, name=None, category=None, price=0.0, campaign=None):
        self.id = Product.product_id_starter+1
        self.name = name
        self.category = category
        self.price = price
        self.campaign = campaign

        # Increase product ID by 1
        Product.product_id_starter+=1

    def print_info(self):
        if self.campaign:
            print(f"{self.category}: {self.name} (ID:{self.id}) - {self.price}€ [CAMPAIGN PRICE]")
        else:
            print(f"{self.category}: {self.name} (ID:{self.id}) - {self.price}€")
    
    def get_price(self):
        if self.campaign:
            # 10% Discount
            return self.price * 0.9  
        return self.price