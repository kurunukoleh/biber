import pygame
import  random
import  time
pygame.init()
class Yama:
     def __init__(self , x , y , w , h , filename , bebobr):
         self.x = x
         self.y = y
         self.w = w
         self.h= h
         self.filename = filename
         self.bebobr = bebobr
         self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
         self.image = pygame.image.load(filename)
         self.image = pygame.transform.scale(self.image, (w , h ))


     def render(self, screen):
        #pygame.draw.rect(screen, (0,0,0), self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])

     def imageload(self , filename):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,(self.w , self.h))

fps =pygame.time.Clock()
screen = pygame.display.set_mode((641,641))
bacground = pygame.image.load("pixil-frame-0 (19).png")
bacground = pygame.transform.scale(bacground,(641,641))
X = 0
g =0
n = 0
bb = 1
Yamlist = []
lastChanges = time.time()
pygame.mixer.init()
pygame.mixer.music.load("Download-_4_.mp3")
pygame.mixer.music.play(-1)
sd1 = pygame.mixer.Sound("_hammering.wav_")
sd2 = pygame.mixer.Sound("_count_down.wav_")
for i in range (3):
    Yamlist.append(Yama( 50 +  X , 50 , 100 , 100 ,"pixelartyama.png" , 0))
    X += 200

X = 0
for i in range (3):
    Yamlist.append(Yama( 50 +  X , 250 , 100 , 100 ,"pixelartyama.png" , 0))
    X += 200

X = 0
for i in range (3):
    Yamlist.append(Yama( 50 +  X , 450 , 100 , 100 ,"pixelartyama.png" , 0))
    X += 200

Run = True
while Run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            sd1.play()
            x,y = pygame.mouse.get_pos()
            for i in range(9):
                if Yamlist[i].rect.collidepoint(x , y):

                    if Yamlist[i].bebobr == 1:
                        Yamlist[i].imageload("pixelartbobr.png")
                        n = random.randint(0, 8)
                        Yamlist[i].bebobr = 0
                        g += 1
                        lastChanges = time.time()

                    if Yamlist[i].bebobr == 0:
                        Yamlist[i].imageload("")
                        n = random.randint(0, 8)
                        lastChanges = time.time()
                        g -= 1


        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(8):
                Yamlist[i].imageload("pixelartyama.png")
                Yamlist[i].bebobr = 0


    scoreText = pygame.font.Font(None , 48).render("рахунок: "+ str(g), True , (150,0,150))

    if time.time() - lastChanges > 1:
        n = random.randint(0, 8)
        lastChanges = time.time()
    for i in range(8):
        if n == i:
            Yamlist[i].imageload("pixelartbobr.png")
            Yamlist[i].bebobr = 1
        else:
            Yamlist[i].imageload("pixelartyama.png")
            Yamlist[i].bebobr = 0

    screen.blit(bacground, [0, 0])
    for i in range (9):
        Yamlist[i].render(screen)

    screen.blit(scoreText,[300 , 10])


    pygame.display.flip()

    fps.tick(60)

