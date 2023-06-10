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
bacground = pygame.image.load("pixelartground2.png")
bacground = pygame.transform.scale(bacground,(641,641))
X = 0
g =0
n = 0
bb = 1
tl = 30
bobrlist = []
lastChanges2 = time.time()
lastChanges4 = time.time()
lastChanges5 = time.time()
pygame.mixer.init()
pygame.mixer.music.load("Download-_4_.mp3")
pygame.mixer.music.play(-1)
sd1 = pygame.mixer.Sound("_hammering.wav_")
sd2 = pygame.mixer.Sound("_count_down.wav_")
sd3 = pygame.mixer.Sound("583699913672e65.mp3")
sd4 = pygame.mixer.Sound("fc31ca320b0edd3.mp3")
bobrlist.append(Yama(50 , 50 , 100 , 100 , "pixelartbobr2.png" , 0))
Run = True
while Run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if time.time() - lastChanges5 > 0.5 :
                lastChanges5 = time.time()
                sd1.play()
                x,y = pygame.mouse.get_pos()
                if bobrlist[0].rect.collidepoint(x , y):
                    g += 1
                else :
                    g -= 1


    scoreText = pygame.font.Font(None , 48).render("рахунок: "+ str(g), True , (0,0,0))
    timeText = pygame.font.Font(None, 48).render("часу лишилося: " + str(tl), True, (0, 0, 0))


    if time.time() - lastChanges4 > 1 :
        lastChanges4 = time.time()
        tl -= 1

    if time.time() - lastChanges2 > 1:
        ax = random.randint(1, 3)*200 - 120
        ay = random.randint(1, 3)*200 - 150
        bobrlist.append(Yama(ax, ay, 100, 100, "pixelartbobr2.png", 0))
        bobrlist.pop(0)
        lastChanges2 = time.time()

    if g < 0 or tl < 0 :
        screen.fill((255, 0, 0))
        bacground = pygame.image.load("pixelartlose.png")
        bacground = pygame.transform.scale(bacground, (641, 641))
        screen.blit(bacground, [0, 0])
        screen.blit(scoreText, [300, 300])
        pygame.display.flip()
        sd3.play(1)
        time.sleep(5)
        Run = False

    if g > 19 :
        screen.fill((0, 255, 0))
        bacground = pygame.image.load("pixelartwin.png")
        bacground = pygame.transform.scale(bacground, (641, 641))
        screen.blit(bacground, [0, 0])
        pygame.display.flip()
        sd4.play(1)
        time.sleep(5)
        Run = False



    screen.blit(bacground, [0, 0])
    bobrlist[0].render(screen)
    screen.blit(scoreText,[400 , 10])
    screen.blit(timeText, [50, 10])


    pygame.display.flip()

    fps.tick(60)
