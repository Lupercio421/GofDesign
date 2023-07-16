from datetime import datetime

class Random8(object):
    def __init__(self):
        self.set_seed(datetime.now().microsecond % 255 + 1)
    
    def set_seed(self, value):
        self.seed = value
    
    def random(self):
        self.seed, carry = divmod(self.seed, 2)
        if carry:
            self.seed ^= 0xb8
        return self.seed
    
_instance = Random8()

random = _instance.random
set_seed = _instance.set_seed
print(random)

#This pattern is usually not appropriate for a class whose constructor creates files, reads a database configuration, opens sockets, or that in general will inflict side effects on the program importing them.

#Prebound Methods pattern is an elegant way to make the stateful behavior of a class instance available up at a module’s global level.
#“Explicit is better than implicit” — and materializing the stack of names as real code will better support human readers, language servers, and even venerable old grep.