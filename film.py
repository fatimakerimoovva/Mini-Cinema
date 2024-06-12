class Hours:
        
    def __init__(self,start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
    
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
    
  
        
class Film:
    def __init__(self,name, director, year, genre, duration, imdb, hours, price):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.imdb = imdb
        self.duration = duration
        self.hours = list(hours)
        self.price = price
        
    def show_info(self):
        hours = []
        for hour in self.hours:
            dic= {
                'start time':hour.start_time,
                'end time':hour.end_time,
            }
            hours.append(dic)
            
        
        return '''
        Name : {}
        Director : {}
        Year : {}
        Gerne : {}
        Duration : {}
        Imdb : {}
        Hours : {}
        Price : {}
        '''.format(self.name,self.director,self.year,self.genre,self.duration,self.imdb,hours,self.price)
    
    def year_info(self):
        try:
            if self.year < 2000:
                print("Old Category")
            elif self.year > 2000:
                print("New Category")
        except ValueError:
            print("Error du dostum")
        
    def duration_info(self):
        try:
            if self.duration > 120:
                print("Long Movie")
            elif self.duration < 120:
                print("Short Movie")
        except ValueError:
            print("Errordu dostumm")
    
    def rating_info(self):
        try:
            if 0 < self.imdb < 6:
                print("E")
            elif  6 <= self.imdb <7:
                print("D")
            elif  7 <= self.imdb <8:
                print("C")
            elif  7 <= self.imdb <9:
                print("B")
            elif  9 <= self.imdb <=10:
                print("A")
            else:
                print("Not Found")
        except  ValueError:
            print("ERRORRR!!!")
        
    
    
    
    

        
        
    
        
    


        

 

    
