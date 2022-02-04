class Dish: 

    def __init__(self, title, price= 0) -> None:
        self.title = title
        self.price = price
        self.description = ""
        self.ingredients = ""
    

class Drink: 
    def __init__(self, title, hot= False, price= 0, alcohol = False) -> None:
        self.title = title
        self.hot = hot
        self.price = price 
        self.alcohol = alcohol
        self.description = ""

class Menu: 

    def __init__(self) -> None: 
        self.list_dish = []
        self.list_drinks = []

    def show_menu_dishes(self):
        for dish in self.list_dish:
            print(f" - {dish.title} --> {dish.price} €")

    def show_menu_drinks(self):
        for drink in self.list_drinks:
            print(f" - {drink.title} --> {drink.price} €")

class Order: 
    pass

class Customer: 
    pass


#########################################################
# Create Instances 
# Food 
pizza_1 = Dish("Pizza Tunfish", 3)
pizza_2 = Dish("Pizza Margeritta", 4)
pizza_3 = Dish("Pizza Fungi", 5)

# Drinks
drink_1 = Drink("Black Tea", True, 2, False)
drink_2 = Drink("Green Tea", True, 2, False)
drink_3 = Drink("Fanta Tea", False, 3, False)



# Create Restaurant Menu
menu_1 = Menu()
menu_1.list_dish.append(pizza_1)
menu_1.list_dish.append(pizza_2)
menu_1.list_dish.append(pizza_3)


menu_1.list_drinks.append(drink_1)
menu_1.list_drinks.append(drink_2)
menu_1.list_drinks.append(drink_3)

# Show Restaurant Menu
menu_1.show_menu_dishes()
menu_1.show_menu_drinks()
            
        