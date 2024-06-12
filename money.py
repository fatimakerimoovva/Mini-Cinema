from film import Film


class Money:
    def __init__(self,current_money):
        self.current_money = current_money
    
    def get_money(self):
        return self.current_money
    
    def set_money(self,film):
        if self.current_money > film.price:
            current_money = self.current_money - film.price
            print(f"Siz bilet aldiniz. Qalan pulunuz {current_money} Azn")
        else:
            exit("yeteri qeder pulun yoxdu fakir")
            
    
        
        
        
  
        
        
        

            
        
        
    

    