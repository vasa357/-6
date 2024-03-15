
class On_sand:
    def message_handler(self):
        return "Ліс виглядає піщаний."

class On_swamp:
    def message_handler(self):
        return "Ліс виглядає болотистий."

class Pine_and_Leafed:
    def message_handler(self):
        return "Ліс поєднує сосен і листяні дерев."

class Taiga:
    def __init__(self):
        self.handler = On_sand() 

    def call_handler(self):
        return self.handler.message_handler()

class Shifted:
    def __init__(self):
        self.handler = On_swamp() 

    def call_handler(self):
        return self.handler.message_handler()

taiga_forest = Taiga()
shifted_forest = Shifted()

print("Message from Taiga:", taiga_forest.call_handler())  
print("Message from Shifted:", shifted_forest.call_handler()) 
