class mobileshop():
    shop_name="AH Mobiles"
    Location="Chennai"
    Mobile_no=639385618299
    list_of_mobile=[]
    list_of_brand=set()
    list_of_color=set()
    list_of_price=set()
    
    def __init__(self,brand,model,color,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.price=price
        mobileshop.list_of_mobile.append(self)
        mobileshop.list_of_brand.add(brand)
        mobileshop.list_of_color.add(color)
        mobileshop.list_of_price.add(price)
        
    @classmethod
    def display_brand(cls):
        for brand in cls.list_of_brand:
            print(f'-------------------{brand}---------------')
            for mobile in cls.list_of_mobile:
                if mobile.brand==brand:
                    print("Model:",mobile.model)
                    print("color:",mobile.color)
                    print("price:",mobile.price)
                    print("_________________________________")
                
    @classmethod
    def display_color(cls):
        for color in cls.list_of_color:
            print(f'-------------------{color}---------------')
            for mobile in cls.list_of_mobile:
                if mobile.color==color:
                    print("Brand:",mobile.brand)
                    print("Model:",mobile.model)
                    print("price:",mobile.price)
                    print("_________________________________")
                
    @classmethod
    def display_price(cls):
        for price in cls.list_of_price:
            print(f'-------------------{price}---------------')
            for mobile in cls.list_of_mobile:
                if mobile.price==price:
                    print("Brand:",mobile.brand)
                    print("Model:",mobile.model)
                    print("color:",mobile.color)
                    print("_________________________________")
    
    @classmethod
    def one_brand(cls):
        print(cls.list_of_brand)
        user_brand=input("Enter u r brand:").lower()
        if user_brand in cls.list_of_brand:
            for mobile in cls.list_of_mobile:
                if mobile.brand.lower()==user_brand:
                    print("Model:",mobile.model)
                    print("color:",mobile.color)
                    print("price:",mobile.price)
                    print("_________________________________")
        else:
            print("no available")
                    
                
                
                
              
m1=mobileshop("samsung","A53","Black","120500")
m2=mobileshop("oppo","T3","red","120000")
m3=mobileshop("apple","15","green","90000")
m4=mobileshop("vivo","y30","blue","12000")
m5=mobileshop("redmi","10","Black","13000")
m6=mobileshop("Samsung","s22","white","10000")
m7=mobileshop("vivo","v30","yellow","12000")
m8=mobileshop("oppo","15","pink","20000")
m9=mobileshop("Samsung","s23","red","120000")
m10=mobileshop("Samsung","s24","Black","170000")
m11=mobileshop("realme","A53","white","620000")
m12=mobileshop("redmi","c53","Black","12000")
m13=mobileshop("apple","16pro","red","42000")
m14=mobileshop("Samsung","A53","gray","13000")
m15=mobileshop("vivo","v50","white","82000")


while True:
    print("\n1. Display by brand")
    print("2. Display by price range")
    print("3. Display by color")
    print("4. Exit")
    
    user_input = input("Enter your choice (1-4): ")
    
    if user_input == "1":
        mobileshop.one_brand()
    elif user_input == "2":
        mobileshop.display_price()
    elif user_input == "3":
        mobileshop.display_color()
    elif user_input == "4":
        print(" Thank you for visiting AH Mobile Shop!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")


















