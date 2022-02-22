class SnakePart:

    def __init__(self, x, y, dir): 
        self.x = x
        self.y = y
        self.size = 1
        self.dir = dir

    def getDir(self):
        return self.dir

    def changeDir(self, dir):
        self.dir = dir

    def updateCoords(self, dir):
        """ Retarded method fix later """
        [self.x, self.y] = [self.x + dir[0], self.y + dir[1]]

    def newCoord(self, coord):
        [self.x, self.y] = [coord[0], coord[1]]

    def getCoords(self):
        return [self.x, self.y]


class Snake:
    
    def __init__(self):
        self.parts = [SnakePart(25, 25, [1,0])]
        self.size = 0 
        self.speed = 1
        self.prevCoords = None
        self.prevDir = None

    def getSize(self):
        return self.size
    
    def changeDir(self, dir):
        self.parts[0].changeDir(dir)

    def getParts(self):
        return self.parts

    def getHead(self):
        return self.parts[0]

    def getHeadDir(self):                   #[1,0] = east [-1,0] = west [0, -1] = south [0, 1] = north 
        return self.getHead().getDir()

    def getSpeed(self):
        return self.speed

    def grow(self):
        self.size += 1
        newX = self.prevCoords[0]
        newY = self.prevCoords[1]
        self.parts.append(SnakePart(newX, newY, self.prevDir))

    def updateSnake(self):
        self.prevDir = self.getHead().getDir()
        self.prevCoords = self.getHead().getCoords()
        self.getHead().updateCoords(self.getHeadDir())
        for part in self.parts[1:]:
            part.updateCoords(self.prevDir)
            self.prevDir = part.getDir()
            self.prevCoords = part.getCoords()

  