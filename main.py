import math, cmath
import pyxel
import threading


class App:
    def __init__(self):
        self.mondelbrotIterNum = 30
        self.mondelbrotScale   = 200
        self.mondelbrotThread = threading.Thread(target = self.drawMondelbrotSet, args = ...)
        self.width = 1281
        self.height = 721
        self.middle_pixel = [int(self.width/2), int(self.height/2)]
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)
        self.mondelbrotThread.start()

    def drawDoteOnPlot(self, x, y, scale = 70, color = 13):
        pyxel.pset(self.middle_pixel[0] + x * scale, self.middle_pixel[1] + y * scale, color)
        # pyxel.rect(self.middle_pixel[0] + x * scale - 2, self.middle_pixel[1] + y * scale - 2, 4, 4, color)

    def drawLineOnPlot(self, x1, y1, x2, y2, scale = 70, color = 13):
        x1 = self.middle_pixel[0] + x1 * scale
        y1 = self.middle_pixel[1] + y1 * scale
        x2 = self.middle_pixel[0] + x2 * scale
        y2 = self.middle_pixel[1] + y2 * scale
        pyxel.line(x1, y1, x2, y2, color)

    def drawMiddleLines(self):
        pyxel.rect(self.middle_pixel[0], 0, 1, self.height, 13)
        pyxel.rect(0, self.middle_pixel[1], self.width, 1, 13)

    def drawSin(self):
        prev_x = 0
        prev_y = 0
        x = 0
        y = 0
        for i in range(-30, 20):
            for j in range((i-1)*1, i*1): # to improve scale
                prev_x = x
                prev_y = y
                x = j / 1
                y = math.cos(math.degrees(x))
                # self.drawDoteOnPlot(x, y)
                if (prev_x != 0 and prev_y != 0):
                    self.drawLineOnPlot(x, y, prev_x, prev_y)

    def mondelbrotCheck(self, x, y, iterNum = 10):
        z = complex(0, 0)
        c = complex(x, y)
        for i in range(iterNum):
            try:
                z = z**2 + c
            except OverflowError:
                return False
        if not cmath.isnan(z):
            return True
        return False

    def drawMondelbrotSet(self):
        self.mondelbrotIterNum += 1
        self.biggestValue_X = self.middle_pixel[0]
        self.biggestValue_Y = self.middle_pixel[1]
        for x_sign, y_sign in zip((-1, 1, 1, -1), (-1, 1, -1, 1)):
            for x in range(self.biggestValue_X):
                for y in range(self.biggestValue_Y):
                    if self.mondelbrotCheck(x*x_sign / self.mondelbrotScale, y*y_sign / self.mondelbrotScale, self.mondelbrotIterNum):
                        self.drawDoteOnPlot(x*x_sign, y*y_sign, 1)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(0)
        # self.drawMiddleLines()
        # self.drawSin()
        self.drawMondelbrotSet()

App()
