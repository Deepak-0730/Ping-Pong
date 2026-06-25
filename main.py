import pygame

import random

pygame.init()

#set a Screen to display
screen=pygame.display.set_mode((800,600))

##paddle position gg
pad1x=-64
pad1y=300
pad2x=760
pad2y=300
speed1=0
speed2=0
#create a template for the font
template=pygame.font.SysFont(None,30)
left_won=template.render("right guy is Gay",True,(0,0,0))
right_won=template.render("left guy is Gay",True,(0,0,0))
#give name
pygame.display.set_caption("Ping Pong Game")

#position of ball
ballx=368
bally=268
ball_speedx=random.uniform(0,-0.55)
ball_speedy=random.uniform(0,0.5)

#load a ball
pong_ball=pygame.image.load('ping-pong.png')
#load a paddle
paddle_stick=pygame.image.load('stick.png')

#display stick
def paddle(x,y):
    screen.blit(paddle_stick,(x,y))


#displaying ball:
def ball(x,y):
    screen.blit(pong_ball,(x,y))


def gameover(a):
    screen.fill((255,0,0))
    if a==1:
        screen.blit(left_won,(340,240))
    else:
        screen.blit(right_won,(340,240))

#set an icon
game_icon=pygame.image.load('table-tennis.png')
pygame.display.set_icon(game_icon)

running=True

while running:
    screen.fill((40,40,40))
    for events in pygame.event.get():
        #exiting
        if events.type==pygame.QUIT:
            running=False
        elif events.type==pygame.KEYDOWN:
            if events.key==pygame.K_UP:
                speed1=0.5
            elif events.key==pygame.K_LEFT:
                speed1=-0.5
            elif events.key==pygame.K_RIGHT:
                speed2=0.5
            elif events.key==pygame.K_DOWN:
                speed2=-0.5
        elif events.type==pygame.KEYUP:
            if events.key==pygame.K_UP or events.key==pygame.K_LEFT:
                speed1=0
            elif events.key==pygame.K_DOWN or events.key==pygame.K_RIGHT:
                speed2=0

    #diplaying a ball

    ballx+=ball_speedx
    bally+=ball_speedy
    #adding boundaries
    if bally<0:
        ball_speedy=abs(ball_speedy)
    if bally>560:
        ball_speedy=-abs(ball_speedy)
    if ballx<0:
        if bally>pad1y and bally<pad1y+64:
            ball_speedx=abs(ball_speedx)
        else:
            gameover(0)
    if ballx>760:
        if bally>pad2y and bally<pad2y+64:
            ball_speedx=-abs(ball_speedx)
        else:
            gameover(1)
    ball(ballx,bally)
    

    #display paddle
    pad1y+=speed1
    pad2y+=speed2
    paddle(pad1x,pad1y)
    paddle(pad2x,pad2y)

    #just a compulsory screen refresh command
    pygame.display.update()


pygame.quit()