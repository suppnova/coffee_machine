class Coffee():

    def __init__(self, name, price, supplies):
        self.supplies = {}
        self.name = name
        self.price = price
        for key, value in supplies.items():
            self.supplies[key] = value

class CoffeeMachine():
    supplies = {
    'water': 400,
    'milk': 540,
    'coffee': 120,
    'disposable_cups': 9,
    }

    money = 550

    coffee = [
        Coffee(
            'espresso',
            4,
            {
                'water': 250,
                'coffee': 16,
                'disposable_cups': 1
            }
        ),
        Coffee(
            'latte',
            7,
            {
                'water': 350,
                'milk': 75,
                'coffee': 20,
                'disposable_cups': 1
            }
        ),
        Coffee(
            'cappuchino',
            6,
            {
                'water': 200,
                'milk': 100,
                'coffee': 12,
                'disposable_cups': 1
            }
        ),
    ]

    def print_status(self):
        print('\nThe coffee machine has:'
        f'\n{self.supplies["water"]} of water'
        f'\n{self.supplies["milk"]} of milk'
        f'\n{self.supplies["coffee"]} of coffee beans'
        f'\n{self.supplies["disposable_cups"]} of disposable cups'
        f'\n${self.money} of money'
        )

    def ask_action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        return input()

    def buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        buy_request = input()
        if buy_request == 'back':
            return
        request_coffee = self.coffee[int(buy_request) - 1]
        if (
            self.check_supplies(request_coffee)
        ):
           self.make_coffee_by_supplies(request_coffee) 
        else:
            return
        
    def check_supplies(self, request_coffee):
        can_we_make_coffee = True
        for key_supply in request_coffee.supplies:
            if (
                request_coffee.supplies[key_supply] > self.supplies[key_supply]
            ):
                print(f'Sorry, not enough {key_supply}!')
                can_we_make_coffee = False
        return can_we_make_coffee

    def make_coffee_by_supplies(self, request_coffee):
        print('I have enough resources, making you a coffee!')
        self.money += request_coffee.price
        for key_supply in request_coffee.supplies:
            self.supplies[key_supply] -= request_coffee.supplies[key_supply]

    def fill(self):
        self.supplies['water'] += int(input('\nWrite how many ml of water do you want to add:\n'))
        self.supplies['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
        self.supplies['coffee'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.supplies['disposable_cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))

    def take_money(self):
        print(f'\nI gave you ${self.money}')
        self.money -= self.money

my_coffee_machine = CoffeeMachine()
while True:
    requested_action = my_coffee_machine.ask_action()
    if requested_action == 'exit':
        break
    elif requested_action == 'remaining':
        my_coffee_machine.print_status()
    elif requested_action == 'buy':
        my_coffee_machine.buy()
    elif requested_action == 'fill':
        my_coffee_machine.fill()
    elif requested_action == 'take':
        my_coffee_machine.take_money()
    print()