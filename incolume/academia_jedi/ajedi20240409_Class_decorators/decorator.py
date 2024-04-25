class Accolade:
    def __init__(self, function):
        self.function = function

    def __call__(self, name):
        # Adding Excellency before name
        name = 'Excellency ' + name
        self.function(name)
        # Saluting after the name
        print(f'Thanks {name} for gracing the occasion')
