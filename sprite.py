import pygame as pg

class ImgSprite():
    """ Takes (x, y) and a LOADED pygame image   
        prebuilt rect load and draw function"""
    def __init__(self, coord, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    def cx(self, amount):
        self.rect.x += amount

    def cy(self, amount):
        self.rect.y += amount

    def draw(self, screen):
        screen.blit(self.image, (round(self.rect.x), round(self.rect.y)))

class DrawSprite:
    """ Sprite to manage rect and blitting of shapes
        can create rectangles and circles"""
    def __init__(self, coord, shape, width, length=0, color=(pg.Color("white"))):
        self.lx = coord[0]
        self.ly = coord[1]
        self.shape = shape
        self.width = width
        self.length = length
        self.color = color
        self.updateRect()

    def x(self):
        return self.lx

    def y(self):
        return self.ly

    def cx(self, amount):
        self.lx += amount
        self.updateRect()

    def cy(self, amount):
        self.ly += amount
        self.updateRect()

    def updateRect(self):
        if self.shape == "circle":
            self.rect = [self.lx, self.y, self.width, self.width]
        else:
            self.rect = [self.lx, self.y, self.width, self.length]

    def draw(self, screen):
        if self.shape == "rectangle" or self.shape == "rect":
            pg.draw.rect(screen, self.color, self.rect)
        elif self.shape == "circle":
            pg.draw.circle(screen, self.color, (round(
                self.rect[0]), round(self.rect[1])), round(self.rect[2]), round(self.rect[3]))
        else:
            print("error "  + self.shape + " is not valid shape to draw.")
            print("try 'rect', 'rectangle', or 'circle'")
            quit()
