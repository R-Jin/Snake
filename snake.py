class SnakePart:

    def init(self, x, y, dir): 
        self.x = x
        self.y = y
        self.size = 1
        self.dir = dir

    def getDir(self):
        return self.dir

    def changeDir(self, dir):
        self.dir = dir

    def updateCoords(self, dir):
        (self.x, self.y) += dir 

    def getCoords(self):
        return (self.x, self.y)


class Snake:
    def init(self):
        self.parts = [SnakePart(300, 300, (1,0))] # Initialize the first part of the body
        self.size = 0 

    def getSize(self):
        return self.size

    def getHead(self):
        return self.part[0]

    def getDir(self):
        self.getHead().getDir()

    def grow(self):
        self.size += 1
        self.parts.append(SnakePart())

    def updateSnake(self):
        self.getHead().updateCoords(self.getDir())
        prevDir = self.getDir()

        for part in self.parts:
            part.updateCoords(prevDir)
            #fortsätt här

    def draw(self):
        pass