
def signal(f):
     def wrapper():
          f()
     return wrapper
class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def addPassenger(self, name):
        if self.availableSeats():
                self.passengers.append(name)
                print(name + " "+ "added successfully")
                return True
        print(name + "  was not added because there are no available seats")

    def availableSeats(self):
        return self.capacity- len(self.passengers)
    
@signal
def sing():
     print("I am tired")

plane = flight(4)
passengers = ["Eddy", "Diomede", "bartazare", "Eurica", "Samantha"]

for person in passengers:
     plane.addPassenger(person)


plane.availableSeats()

sing()





    