import time
class Timer:
    def __init__(self, speedLimit = 2.5, targetFPS = 60, allowSlowDown=False, slowDownLimit = .8):
        self.oldTime = time.time()
        self.currentTime  = self.oldTime
        self.frameRate = 0
        self.speedLimit = speedLimit
        self.targetFPS = targetFPS
        self.allowSlowDown = allowSlowDown
        self.slowDownLimit = slowDownLimit
        self.speedMultiplier = 1

    def update(self):
        self.currentTime = time.time()
        dif = self.currentTime-self.oldTime
        if(dif != 0):
            self.frameRate = 1/(self.currentTime-self.oldTime)
            self.speedMultiplier = self.targetFPS/self.frameRate
            self.oldTime = self.currentTime
        if (self.speedMultiplier > self.speedLimit):
            self.speedMultiplier = self.speedLimit
        elif (self.allowSlowDown == False and self.speedMultiplier < 1):
            self.speedMultiplier = 1
        elif (self.allowSlowDown == True and self.speedMultiplier < 1):
            if (not(self.speedMultiplier >= self.slowDownLimit)):
                self.speedMultiplier = self.slowDownLimit
        return self.speedMultiplier