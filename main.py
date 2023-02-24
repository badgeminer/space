import pygame, sys
from pygame.locals import QUIT



pygame.init()

scr = pygame.display.set_mode((400, 300))
csr = None
csrOff = 9

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

class itm:
   def __init__(self,tex,off=9):
     self.tex = tex
     self.off = off

class menu:
  def __init__(self,menus:list[itm]):
    self.menus = []
    I = 0
    for i in menus:
      r = i.tex.get_rect()
      r.top = 5+(I*18)
      r.left = 5
      self.menus.append((r,i))
      I += 1
  def draw(self,scr):
    for i in self.menus:
      scr.blit(i[1].tex,i[0])
  def click(self,pos):
    global csr,csrOff
    for i in self.menus:
      if i[0].collidepoint(pos):
        csr = i[1].tex
        csrOff = i[1].off
        return True
    return False





pygame.display.set_caption('Hello World!')
a = pygame.image.load("a.png")
p = pygame.image.load("p.png")
e = pygame.image.load("e.png")
powere = pygame.image.load("Pe.png")
f = pygame.image.load("f.png")
w = pygame.image.load("w.png")
j = pygame.image.load("j.png")
o = pygame.image.load("o.png")
prism = pygame.image.load("prism.png")
er = e.get_rect()

m = menu([
  itm(a),
  itm(f),
  itm(w),
  itm(j),
  itm(o),
  itm(e),
  itm(powere),
  itm(prism,7)
])

csr = e
g = pygame.sprite.Group()
csrS = Block(csr,(0,0))

draw = pygame.sprite.LayeredUpdates(csrS)

while True:
    k_b = pygame.key.get_pressed()
    scr.fill((0,0,0))
    draw.draw(scr)
    m.draw(scr)
    mp = pygame.mouse.get_pos()
    csrS.rect.center = mp
    if k_b[pygame.K_LSHIFT]:
      c = pygame.sprite.spritecollideany(csrS,g)
      if c:
        csrS.rect.center = (c.rect.centerx,c.rect.centery + csrOff)
      else:
        csrS.rect.center = (0,0)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if not m.click(event.pos):
            s = Block(csr,csrS.rect.center)
            g.add(s)
            draw.add(s)
            draw.move_to_back(s)
          else:
            csrS.image = csr

            
    pygame.display.update()