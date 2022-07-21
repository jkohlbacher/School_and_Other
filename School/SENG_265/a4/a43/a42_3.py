import random

class GenRandom:

    def __init__(self):
        '''GenRandom Class'''
        pass

    def randomList(self,rangelow: int, rangehigh: int, amount: int):
        '''randomList method'''
        randomlist = []
        i = 0

        while i < amount:
            n = random.randint(rangelow,rangehigh)
            randomlist.append(n)
            i+=1

        return randomlist 
    
    def randomFloatList(self,rangelow: int, rangehigh: int, amount: int):
        '''randomFloatList method'''
        randomlist = []
        i = 0

        while i < amount:
            n = round(random.uniform(rangelow,rangehigh),1)
            randomlist.append(n)
            i+=1

        return randomlist



class ArtConfig(GenRandom): 

    def __init__(self, num_of_shapes: int):
        '''ArtConfig Class'''
        super().__init__()
        self.num_of_shapes = num_of_shapes

    def createLists(self):
        self.SHA = self.randomList(0,2,self.num_of_shapes)
        self.X = self.randomList(0,550,self.num_of_shapes)
        self.Y = self.randomList(0,300,self.num_of_shapes)
        self.RAD = self.randomList(0,100,self.num_of_shapes)
        self.W = self.randomList(0,100,self.num_of_shapes)
        self.H = self.randomList(0,100,self.num_of_shapes)
        self.R = self.randomList(0,255,self.num_of_shapes)
        self.G = self.randomList(0,255,self.num_of_shapes)
        self.B = self.randomList(0,255,self.num_of_shapes)
        self.OP = self.randomFloatList(0.0,1.0,self.num_of_shapes)




