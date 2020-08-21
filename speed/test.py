import time
import speedcoeff

x = speedcoeff.Timer(10, 60, True)

while True:
    coeff = x.update()
    print(x.frameRate) ##printing is super slow 
    print(coeff)
    time.sleep(1/30) #simulate 30 fps