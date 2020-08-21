import pygame
pygame.font.init()
def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        if letter != ' ':
            yield tmp
class DynamicText():
    # syntax: t = DynamicText(string, (int, int), pygame.font.Font(string, int),{int}, {int}, {int}, {(int, int, int)})
    # Scrolling text and auto new line(prevent text going off screen) functionality
    # Ex: t = DynamicText("hello, World!", (500, 500))
    #     While True:
    #       t.update()
    #       t.draw(screen)
    #
    # Text can still blit off screen if the charlimit is too high or if charlimit is reached but no space is found.
    # Example of possible off screen blits:
    # string = "IamAveryLongStringIamAveryLongStringIamAveryLongStringIamAveryLongStringIamAveryLongString"
    # self.charlimit = 2
    # self.splitText(string)
    # print(len(self.text))
    #
    # Output:
    #  1
    def __init__(self, text, pos, font = pygame.font.Font(None, 25), delay = 3, offset = 50, charlimit = 75, color = (0, 128, 0)):
        self.font = font
        self.text = []
        self.done = []
        #self._gen = text_generator(text)
        self.index = 0
        self.rendered = [""]
        self.pos = pos
        self.delay = delay
        self.delayticks = delay
        self.offset = offset
        self.charlimit = charlimit
        self.color = color
        self.splitText(text)
        self._gen = [text_generator(self.text[0])]
        for x in range(0, len(self.text)):
            self.rendered.append(self.font.render("", True, self.color)) 
        self.update()

    def splitText(self, text):
        #Counts characters until it reaches charlimit and then continues until a space (so words aren't cut off)
        count = 0
        index = 0
        self.text.append("")
        for letter in text:
            count += 1
            self.text[index] += letter
            if (count >= self.charlimit and letter == " "):
                count = 0
                index += 1
                self.text.append("")

    def update(self):
        self.delayticks += 1
        if self.delayticks >= self.delay:
            self.delayticks = 0
            #print(self.index)
            try: 
                if self.index <= len(self.text)-1:
                    self.rendered[self.index] = self.font.render(next(self._gen[self.index]), True, self.color)
            except StopIteration: 
                try:
                    self.index += 1
                    self._gen.append(text_generator(self.text[self.index]))
                except:
                    pass
            
                    

    def draw(self, screen):
        for x in range(0, len(self._gen)):
            screen.blit(self.rendered[x], (self.pos[0], self.pos[1]+x*self.offset))