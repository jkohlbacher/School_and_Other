#!/usr/bin/env python3
'''Assignment 4 Part 2'''
print(__doc__)

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
        self.SHA = self.randomList(0,3,self.num_of_shapes)
        self.X = self.randomList(0,550,self.num_of_shapes)
        self.Y = self.randomList(0,300,self.num_of_shapes)
        self.RAD = self.randomList(0,100,self.num_of_shapes)
        self.RX = self.randomList(10,30,self.num_of_shapes)
        self.RY = self.randomList(10,30,self.num_of_shapes)
        self.W = self.randomList(0,100,self.num_of_shapes)
        self.H = self.randomList(0,100,self.num_of_shapes)
        self.R = self.randomList(0,255,self.num_of_shapes)
        self.G = self.randomList(0,255,self.num_of_shapes)
        self.B = self.randomList(0,255,self.num_of_shapes)
        self.OP = self.randomFloatList(0.0,1.0,self.num_of_shapes)

    def printLists(self):
        
        print(f'{"CNT":>5} {"SHA":>5} {"X":>5} {"Y":>5} {"RAD":>5} {"RX":>5} {"RY":>5} {"W":>5} {"H":>5} {"R":>5} {"G":>5} {"B":>5} {"OP":>5}')

        for x in range(0,self.num_of_shapes):
            print(f'{x:>5} {self.SHA[x]:>5} {self.X[x]:>5} {self.Y[x]:>5} {self.RAD[x]:>5} {self.RX[x]:>5} {self.RY[x]:>5} {self.W[x]:>5} {self.H[x]:>5} {self.R[x]:>5} {self.G[x]:>5} {self.B[x]:>5} {self.OP[x]:>5}')


def main():
    '''main method'''
    Art = ArtConfig(10)
    Art.createLists()
    Art.printLists()
    

if __name__ == '__main__':
    main()

