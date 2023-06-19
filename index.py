import pygame as pg
pg.init()

# -----CONSTANTS-----
# Window
DISPLAY_SIZE = (1024, 512)
BACKGROUND_COLOR = (76.5, 76.5, 76.5) # Color copied from tutorial



# -----CLASSES-----
# May be completely useless 
class Player: 
  size=8
  def __init__(self, coords: list[int], color: tuple[int, int, int]=(255, 255, 0)):
    self.rect = pg.Rect(coords[0], coords[1], self.size, self.size)
    self.surface = pg.Surface((self.size, self.size))
    self.color = color
    self.surface.fill(self.color)

  def handle_movement(self, keys):
    pass

  def render(self, surface: pg.Surface):
    surface.blit(self.surface, self.rect)
  

if __name__ == "__main__":

  keys = {
    ord("w"): False,
    ord("a"): False,
    ord("s"): False,
    ord("d"): False,
  }

  player = Player([300, 300])
  display_surface = pg.display.set_mode(DISPLAY_SIZE)

  game = True
  while game:
    display_surface.fill(BACKGROUND_COLOR)

    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
      if event.type in [pg.KEYDOWN, pg.KEYUP]:
        if event.key in keys:
          keys[event.key] = not pg.KEYUP

    player.render(display_surface)
    pg.display.update()
