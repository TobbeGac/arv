
import fordon

class Personbil:

    def __init__(self, fabrikat, color, bagagevolym):
        self.bagagevolym = bagagevolym
        self.fabrikat = fabrikat
        self.color = color
    

    def setBagageVolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def getBagageVolym(self):
        return self.bagagevolym
    
    def print_fordon(self):
        print(self.fabrikat+ " Färg: " +self.color+ ", Bagagevolym" +str(self.bagagevolym)+ " L")