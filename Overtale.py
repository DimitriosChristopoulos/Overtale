#importing what the program needs
from pygame import *
from random import *
from math import *

#making a screen
size=width,height=800,600
screen=display.set_mode(size)

#making basic colors
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#initializing font
font.init()
comicSansFont=font.SysFont("Consolas",30)#loading comic sans font

#initializing sounds
mixer.init()
musicChannel=mixer.Channel(0)#making a mixer
sansTalking=mixer.Sound("Sound/intro.mp3")

#opening text files
introText=open("Text/intro text.txt","r")#opening intro slides' text
slideTexts=introText.readlines()#getting a list of each line(slide) of dialogue

#defining functions
def drawSlides(text,picture):#defining a function that draws intro slides
    screen.blit(picture,(100,100))#blitting the picture for the slide
    fx=100#font x position
    fy=410#font y position
    count=0#a counter that is used to make sure that the audio doesnt get cut off
    for char in text:#for the character in the text
        print(char)
        if count%6==0:#making sure that the sound doesnt cut itself off too early
            musicChannel.play(sansTalking)#play the audio
        count+=1#increase the count by 1
        if char=="~":#if the character is "~", this means that the program needs to start a new line. This is in the text files so that we can use .readlines() more easily, as we can fit everything that should be said in one text box in one line
            fx=100
            fy+=30
        else:
            inc=0#increment so that letters appear 1 by 1, also reseting it so that the increment only increases for pauses
            count+=1#counter increases by 1
            if char=="." or char==",":#if the character is punctuation
                inc=300#increase the amount of time the program waits after displaying the letter
            char=comicSansFont.render(char,True,WHITE)#render the character
            screen.blit(char,(fx,fy))#blit the font at font x and font y
            display.flip()#show everything
            time.wait(55+inc)#wait so that letters show 1 by 1
            fx+=15#move the next character 13 pixels over
    time.wait(1000)#at the end of the slide, wait 1000 millaseconds
    screen.fill(BLACK)#fill the screen with black color so that the next slide doesnt overlap

def drawPictures(picture):#defining function that will blit the picture of the slides
    screen.blit(picture,(100,100))#blit the picture
    display.flip()
    time.wait(2000)#wait so that they user can see the picture
    screen.fill(BLACK)#fill the screen with black color so that the next slide doesnt overlap
    
for i in range(6):
    drawSlides(slideTexts[i],image.load("Pictures/Intro slides/intro"+str(i+1)+".jpg"))#draw the slides 1 through 6, adding 1 because the for loop starts at 0 and ends at 5
   
for i in range(4):
    drawPictures(image.load("Pictures/Intro slides/intro"+str(i+7)+".jpg"))#drawing the pictures 7 through 9,adding 7 because the pictures are labeled in the folder in order of the slides

intro11=image.load("Pictures/Intro Slides/intro112.jpg")#loading final image, this does not get a function because it is simpler to just do it without one, as it is only one picture
screen.blit(intro11,(100,-527))#blit the picture at 100,-627, as the picture is 924 tall, and we only want to show the bottom 297 pixels at this point so it matches the other pictures
display.flip()
time.wait(1500)#wait 1500 millaseconds
for i in range(528):
    screen.blit(intro11,(100,-527+i))#draw the picture 1 pixel lower
    draw.rect(screen,BLACK,(100,397,540,400))#draw a rect below the picture so that when it starts coming down you only see 297 vertical pixels of picture
    display.flip()#show all this
time.wait(1000)
###merge with shivan's code at this point
    
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

quit()