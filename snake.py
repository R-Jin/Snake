import random

class Dot:

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def updateCoords(self, c):
        [self.x, self.y] = [c[0], c[1]]

    def getCoords(self):
        return [self.x, self.y]
    
class Food(Dot):
    def __init__(self, x, y):
        super().__init__(x, y)

    def updateToNewCoord(self, gridSize, snake):
        x = [x for x in range(gridSize)]
        y = [y for y in range(gridSize)]

        for part in snake.getParts():
            if part.getCoords()[0] in x:
                x.remove(part.getCoords()[0])

            if part.getCoords()[1] in y:
                y.remove(part.getCoords()[1])
        

        self.x = random.choice(x)
        self.y = random.choice(y)

class Snake:
    
    def __init__(self):
        self.parts = [Dot(25, 25)]
        self.speed = 1
        self.dir = (1, 0)
        self.size = 1

    def getSize(self):
        return self.size

    def getLastPart(self):
        return self.parts[-1]
    
    def getDir(self):
        return self.dir
    
    def changeDir(self, dir):
        self.dir = dir

    def getHead(self):
        return self.parts[0]
    
    def getSize(self):
        return self.size

    def getSpeed(self):
        return self.speed
    
    def getParts(self):
        return self.parts

    def grow(self, oldC):
        newSnakePart = Dot(oldC[0], oldC[1])
        self.parts.append(newSnakePart)
        self.size += 1

    def updateSnake(self, grow):
        newC = [self.getHead().getCoords()[0] + self.dir[0], self.getHead().getCoords()[1] + self.dir[1]]
        oldC = self.getHead().getCoords()
        self.getHead().updateCoords(newC)
        for part in self.parts[1:]:
            newC = oldC
            oldC = part.getCoords()
            part.updateCoords(newC)
        if grow:
            self.grow(oldC)
    