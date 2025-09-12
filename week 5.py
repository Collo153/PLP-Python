# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"



class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   
        self.os = os
        self.storage = storage
        self.__battery = 100  

    # Method
    def install_app(self, app_name):
        return f"Installing {app_name} on {self.device_info()}..."

    def use_battery(self, amount):
        if amount < self.__battery:
            self.__battery -= amount
            return f"Battery left: {self.__battery}%"
        else:
            return "Battery too low! Please charge."

    def check_battery(self):
        return f"Battery level: {self.__battery}%"


# Creating objects
phone1 = Smartphone("Samsung", "S23", "Android", "256GB")
phone2 = Smartphone("Apple", "iPhone 15", "iOS", "128GB")

print(phone1.device_info())
print(phone1.install_app("WhatsApp"))
print(phone1.use_battery(30))
print(phone1.check_battery())

print(phone2.device_info())
