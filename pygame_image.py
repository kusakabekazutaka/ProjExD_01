import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img1=[bg_img,pg.transform.flip(bg_img,True,False)]*2

    kokaton_img=pg.image.load("ex01/fig/3.png")
    kokaton_img=pg.transform.flip(kokaton_img,True,False)
    kokaton_img1=[kokaton_img,pg.transform.rotozoom(kokaton_img,10,1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr%1600
        for i in range(4):
            screen.blit(bg_img1[i],[1600*i-x,0])
        screen.blit(kokaton_img1[tmr%100//50], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()