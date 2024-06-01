import random
import pygame
pygame.init()
import time



screen=pygame.display.set_mode([1000,1000])
even_type=pygame.event.custom_type()
print(even_type)
pygame.time.set_timer(even_type,3000,3)
print(pygame.font.get_fonts())
font=pygame.font.SysFont("arial",30)
font_screen=font.render('font',True,[255,255,255])
screen.blit(font_screen,[250,250])
while True:
    time.sleep(1/60)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            font_screen=font.render('space',True,[255,255,255])
            screen.blit(font_screen, [random.randint(0,500), random.randint(0,500)])
        if event.type==pygame.KEYUP:
            font_screen = font.render(str(event.key), True, [random.randint(0,255), random.randint(0,255), random.randint(0,255)])
            screen.blit(font_screen, [random.randint(0, 1000), random.randint(0, 1000)])
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==pygame.BUTTON_LEFT:
                color=[0,255,0]
            if event.button==pygame.BUTTON_MIDDLE:
                color=[255,0,0]
            if event.button==pygame.BUTTON_RIGHT:
                color=[0,0,255]
            if event.button==pygame.BUTTON_WHEELUP:
                color=[0,255,255]
            if event.button==pygame.BUTTON_WHEELDOWN:
                color=[255,255,0]
            font_screen = font.render('mouse'+str(event.button), True, color)
            screen.blit(font_screen, event.pos)
        if event.type==pygame.MOUSEMOTION:
            if event.buttons[2]==1:
                pygame.draw.circle(screen, [255, 0, 0], event.pos, 20)
            if event.buttons[1]==1:
                pygame.draw.circle(screen, [255, 255, 0], event.pos, 15)
            if event.buttons[0]==1:
                pygame.draw.circle(screen, [0, 255, 255], event.pos, 10)
            print(event.buttons)
            pygame.draw.circle(screen,[255,255,255],event.pos,5)
        if event.type == even_type:
            screen.fill([0,0,0])
    pygame.display.flip()