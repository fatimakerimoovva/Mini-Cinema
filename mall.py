from datetime import datetime

class Mall:
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count
        
    def working_time(self):
        current_hour = datetime.now().hour
        opening_hour = 0
        closing_hour = 23
        
        if current_hour >= opening_hour and current_hour <= closing_hour:
            print("Mall is open")
        else:
            exit("Mall baglidir.")
    
    
    def information(self):
        print(f"Location : {self.location}")
        print(f"Floor : {self.floor}")
        print(f"Halls : {self.hall_count}")
        
class Ganclik(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
        
        
class Deniz(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)


class Iyirmisekkiz(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
        
class ParkBulvar(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
        
class Amburan(Mall):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
        
        

mallganclik = Ganclik("Ganclik", 4, 6)
mall28 = Iyirmisekkiz("28may", 5, 8)
mallparkbulvar = ParkBulvar("Sahil", 5, 5)
mallamburan = Amburan("Bilgeh", 3, 5)
malldeniz = Deniz("Bulvar", 7, 9)
