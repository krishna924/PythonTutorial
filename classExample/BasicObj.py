# Oops Concepts

class Cars(object):

    def __init__(self, make, model):
        self.carmake = make
        self.carmodel = model

o1 = Cars('bmw', '530i')
o2 = Cars('Merc', 'C300')

print(o1.carmake + o1.carmodel)
print(o2.carmodel + o2.carmake)