import fordon

class Lastbil:

    def __init__(self, fabrikat, color, flakvolym):
        self.flakvolym = flakvolym
        self.fabrikat = fabrikat
        self.color = color
    

    def setFlakVolym(self, flakvolym):
        self.flakvolym = flakvolym

    def getFlakVolym(self):
        return self.flakvolym
    
    def print_fordon(self):
        print(self.fabrikat+ " Färg: " +self.color+ ", flakvolym" +str(self.flakvolym)+ " L")