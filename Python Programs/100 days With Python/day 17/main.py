class Car :
    def __init__(self,seats,transmission,fuel):
        self.seats = seats
        self.transmission = transmission
        self.fuel = fuel
        
    def print_att(self):
        print (f"""
The car has {self.seats}
the car has {self.transmission}
the runs on {self.fuel}""")
        

i10 = Car(4,"Manual","Petrol")
i10.print_att()
