import pygame, sys
from pygame.locals import QUIT



pygame.init()

scr = pygame.display.set_mode((400, 300))
csr = None

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, img,xy):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = img

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.center = xy


class menu:
  def __init__(self,menus:list[pygame.Surface]):
    self.menus = []
    I = 0
    for i in menus:
      r = i.get_rect()
      r.top = 5+(I*18)
      r.left = 5
      self.menus.append((r,i))
      I += 1
  def draw(self,scr):
    for i in self.menus:
      scr.blit(i[1],i[0])
  def click(self,pos):
    global csr
    for i in self.menus:
      if i[0].collidepoint(pos):
        csr = i[1]
        return True
    return False




pygame.display.set_caption('Hello World!')
a = pygame.image.load("a.png")
p = pygame.image.load("p.png")
e = pygame.image.load("e.png")
f = pygame.image.load("f.png")
er = e.get_rect()

m = menu([a,f,e])

csr = e
g = pygame.sprite.Group()
csrS = Block(csr,(0,0))
while True:
    k_b = pygame.key.get_pressed()
    scr.fill((0,0,0))
    g.draw(scr)
    m.draw(scr)
    mp = pygame.mouse.get_pos()
    er.center = mp
    if k_b[pygame.K_LALT]:
      c = pygame.sprite.spritecollideany(csrS,g)
      if c:
        er.centerx = c.rect.centerx
        er.centery = c.rect.centery + 14
        
    scr.blit(csr,er)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if not m.click(event.pos):
            g.add(Block(csr,event.pos))
    pygame.display.update()