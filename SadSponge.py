from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def drawCircle(r=0.1,xc=0,yc=0,circonst=GL_POLYGON,circol=[1,1,1],thetastart=0,thetaend=2*pi):
    glBegin(circonst)
    for theta in np.arange(thetastart,thetaend,0.0001):
        x=r *cos(theta)
        y=r *sin(theta)
        glColor3f(circol[0],circol[1],circol[2])
        glVertex(x+xc,y+yc)

    glEnd()

def drawnet(xstep,ystep):
    glBegin(GL_LINES)
    for i in np.arange(-1,1,ystep):
        glColor3f(1,0,0)
        glVertex(-1,i)
        glVertex(1,i)

    for i in np.arange(-1, 1, xstep):
        glColor3f(1, 0, 0)
        glVertex(i, -1)
        glVertex(i, 1)

    glEnd()
def drawrect(pnts,rectcol):
    glBegin(GL_POLYGON)
    glColor3f(rectcol[0],rectcol[1],rectcol[2])
    glVertex(pnts[0],pnts[1])
    glVertex(pnts[2],pnts[3])
    glVertex(pnts[4],pnts[5])
    glVertex(pnts[6],pnts[7])

    glEnd()

def drawsinwave(start,end,shift):

    glBegin(GL_LINE_STRIP)
    glColor3f(0,0,0)
    for x in np.arange(start,end,0.00001):
        y=0.01*sin(50*x)+shift
        glVertex(x,y)
    glEnd()

def draw():

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

#inside coloring
    drawrect([0.49, 0.69, -0.49, 0.69, -0.49, -0.29, 0.49, -0.29], [1, 1, 0])
    drawrect([0.495, -0.405, -0.495, -0.405, -0.495, -0.495, 0.495, -0.495], [0.8, 0.4, 0.1])
#draw body
    drawsinwave(-0.5,0.5,0.7)
    glRotate(90, 0, 0, 1)
    drawsinwave(-0.3,0.7,0.5)
    glRotate(-90, 0, 0, 1)
    glRotate(-90,0,0,1)
    drawsinwave(-0.7, 0.3, 0.5)
    glRotate(90, 0, 0, 1)
    drawsinwave(-0.5,0.5,-0.3)

    drawsinwave(-0.49,0.49,0.69)
    glRotate(90, 0, 0, 1)
    drawsinwave(-0.29,0.69,0.49)
    glRotate(-90, 0, 0, 1)
    glRotate(-90,0,0,1)
    drawsinwave(-0.69, 0.29, 0.49)
    glRotate(90, 0, 0, 1)
    drawsinwave(-0.49,0.49,-0.29)

#draw pants
    glBegin(GL_LINE_STRIP)
    glColor3f(0,0,0)
    glVertex(0.5,-0.3)
    glVertex(0.5,-0.5)
    glVertex(-0.5,-0.5)
    glVertex(-0.5,-0.3)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(0.5,-0.4)
    glVertex(-0.5,-0.4)
    glEnd()
#draw eyes

    drawCircle(0.15,0.16,0.4,GL_LINE_LOOP,[0,0,0])
    drawCircle(0.15,-0.16,0.4,GL_LINE_LOOP,[0,0,0])
    drawCircle(0.14, 0.16, 0.4, GL_POLYGON, [1, 1, 1])
    drawCircle(0.14, -0.16, 0.4, GL_POLYGON, [1, 1, 1])
    drawCircle(0.07, 0.16, 0.4, GL_POLYGON, [0.1, 0.5, 1])
    drawCircle(0.07, -0.16, 0.4, GL_POLYGON, [0.1, 0.5, 1])
    drawCircle(0.03, 0.16, 0.4, GL_POLYGON, [0, 0, 0])
    drawCircle(0.03, -0.16, 0.4, GL_POLYGON, [0, 0, 0])
    drawCircle(0.08, 0.16, 0.4, GL_LINE_LOOP, [0, 0, 0])
    drawCircle(0.08, -0.16, 0.4, GL_LINE_LOOP, [0, 0, 0])
#draw mouth

    glBegin(GL_LINE_STRIP)
    glColor3f(0,0,0)
    for x in np.arange(-0.3,0.3,0.00001):
        y=-(x**2)
        glVertex(x,y)
    glEnd()

#draw cloth
    drawrect([0.45,-0.43,0.45,-0.45,0.3,-0.45,0.3,-0.43],[0,0,0])
    drawrect([0.25, -0.43, 0.25, -0.45, 0.1, -0.45, 0.1, -0.43], [0, 0, 0])
    drawrect([-0.25,-0.43, -0.25, -0.45, -0.1, -0.45, -0.1, -0.43], [0, 0, 0])
    drawrect([-0.45, -0.43, -0.45, -0.45, -0.3, -0.45, -0.3, -0.43], [0, 0, 0])

#draw legs

    drawrect([0.26, -0.49, 0.26, -0.54, 0.04, -0.54, 0.04, -0.49], [ 0,0, 0])
    drawrect([-0.26, -0.49, -0.26, -0.54, -0.04, -0.54, -0.04, -0.49], [0, 0, 0])

    drawrect([0.25,-0.5,0.25,-0.53,0.05,-0.53,0.05,-0.5],[0.8, 0.4, 0.1])
    drawrect([-0.25, -0.5, -0.25, -0.53, -0.05, -0.53, -0.05, -0.5], [0.8, 0.4, 0.1])

    drawrect([0.13,-0.53,0.17,-0.53,0.17,-0.8,0.13,-0.8],[0,0,0])
    drawrect([-0.13, -0.53, -0.17, -0.53, -0.17, -0.8, -0.13, -0.8], [0, 0, 0])

    drawrect([0.14, -0.54, 0.16, -0.54, 0.16, -0.65, 0.14, -0.65], [1, 1, 0])
    drawrect([-0.14, -0.54, -0.16, -0.54, -0.16, -0.65, -0.14, -0.65], [1, 1, 0])


    drawrect([0.14, -0.66, 0.16, -0.66, 0.16, -0.68, 0.14, -0.68], [1, 1, 1])
    drawrect([-0.14, -0.66, -0.16, -0.66, -0.16, -0.68, -0.14, -0.68], [1, 1, 1])

    drawrect([0.14, -0.68, 0.16, -0.68, 0.16, -0.7, 0.14, -0.7], [0, 0, 1])
    drawrect([-0.14, -0.68, -0.16, -0.68, -0.16, -0.7, -0.14, -0.7], [0, 0, 1])

    drawrect([0.14, -0.7, 0.16, -0.7, 0.16, -0.72, 0.14, -0.72], [1, 1, 1])
    drawrect([-0.14, -0.7, -0.16, -0.7, -0.16, -0.72, -0.14, -0.72], [1, 1, 1])

    drawrect([0.14, -0.72, 0.16, -0.72, 0.16, -0.74, 0.14, -0.74], [1, 0, 0])
    drawrect([-0.14, -0.72, -0.16, -0.72, -0.16, -0.74, -0.14, -0.74], [1, 0, 0])

    drawrect([0.14, -0.74, 0.16, -0.74, 0.16, -0.8, 0.14, -0.8], [1, 1, 1])
    drawrect([-0.14, -0.74, -0.16, -0.74, -0.16, -0.8, -0.14, -0.8], [1, 1, 1])


    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  20*(( x - 0.15) ** 2)-0.95
        if y<-0.8:
         glVertex(x,y)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  20*(( x +0.15) ** 2)-0.95
        if y<-0.8:
         glVertex(x,y)

    glEnd()

    drawCircle(0.05,0.15,-0.85,GL_POLYGON,[0.1,0.1,0.1])
    drawCircle(0.05, -0.15, -0.85, GL_POLYGON, [0.1, 0.1, 0.1])

#draw eyelashes
    drawrect([0.16, 0.55, 0.17, 0.55, 0.17, 0.6, 0.16, 0.6], [0, 0, 0])
    drawrect([0.22, 0.53, 0.23, 0.53, 0.3, 0.59, 0.31, 0.59], [0, 0, 0])
    drawrect([0.1, 0.53, 0.11, 0.53, 0.03, 0.59, 0.04, 0.59], [0, 0, 0])

    drawrect([-0.16, 0.55, -0.17, 0.55, -0.17, 0.6, -0.16, 0.6], [0, 0, 0])
    drawrect([-0.22, 0.53, -0.23, 0.53,- 0.3, 0.59, -0.31, 0.59], [0, 0, 0])
    drawrect([-0.1, 0.53, -0.11, 0.53, -0.03, 0.59, -0.04, 0.59], [0, 0, 0])


#draw nose
    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 0)
    for y in np.arange(-0.3, 0.3, 0.00001):
        x = ((( ( 9*y )-  2)) ** 2)-0.2
        if x<0.05:
         glVertex(x, y)
    glEnd()

#draw teeth
    drawrect([0.05,-0.0025,0.17,-0.0225,0.17,-0.05,0.05,-0.05],[0,0,0])
    drawrect([-0.05, -0.0025, -0.17, -0.0225, -0.17, -0.05, -0.05, -0.05], [0, 0, 0])

    drawrect([0.06, -0.0125, 0.16, -0.0325, 0.16, -0.04, 0.06, -0.04], [1, 1, 1])
    drawrect([-0.06, -0.0125, -0.16,-0.0325, -0.16, -0.04, -0.06, -0.04], [1, 1, 1])

#draw hands
    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 0)
    for x in np.arange(0.5, 0.7, 0.00001):
        y = (-( (2*x)-0.5) ** 2)+0.3
        if y>-0.2:
         glVertex(x, y)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 0)
    for x in np.arange(-0.5, -0.7, -0.00001):
        y = (-( (2*x)+0.5) ** 2)+0.3
        if y>-0.2:
         glVertex(x, y)
    glEnd()

    drawCircle(0.05,0.55,-0.2,GL_LINE_STRIP,[0,0,0],-pi,0)
    drawCircle(0.05, -0.55, -0.2, GL_LINE_STRIP, [0, 0, 0], -pi, 0)

    drawrect([0.54, -0.25, 0.56, -0.25, 0.58, -0.4, 0.56, -0.4], [0, 0, 0])
    drawrect([-0.54, -0.25, -0.56, -0.25, -0.58, -0.4, -0.56, -0.4], [0, 0, 0])

    drawrect([0.545, -0.255, 0.555, -0.255, 0.575, -0.39, 0.565, -0.395], [1, 1, 0])
    drawrect([-0.545, -0.255, -0.555, -0.255, -0.575, -0.39, -0.565, -0.395], [1, 1, 0])

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  55*(( x - 0.57) ** 2)-0.6
        if y<-0.38:
         glVertex(x,y)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  100*(( x - 0.57) ** 2)-0.59
        if y<-0.39:
         glVertex(x,y)

    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  55*(( x + 0.57) ** 2)-0.6
        if y<-0.38:
         glVertex(x,y)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)
    for x in np.arange(-0.9, 0.9, 0.00001):
        y =  100*(( x + 0.57) ** 2)-0.59
        if y<-0.39:
         glVertex(x,y)

    glEnd()



#draw Tie
    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 0)
    glVertex(0.05, -0.3)
    glVertex(0.1,-0.35)
    glVertex(0.15, -0.3)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 0)
    glVertex(-0.05, -0.3)
    glVertex(-0.1, -0.35)
    glVertex(-0.15, -0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex(0.05, -0.3)
    glVertex(0.03, -0.35)
    glVertex(-0.03, -0.35)
    glVertex(-0.05, -0.3)

    glEnd()

    glBegin(GL_POLYGON)
    glVertex(0.03, -0.35)
    glVertex(0.06, -0.45)
    glVertex(0,-0.49)
    glVertex(-0.06, -0.45)
    glVertex(-0.03, -0.35)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.9, 0, 0)
    glVertex(0.04, -0.31)
    glVertex(0.02, -0.35)
    glVertex(-0.02, -0.35)
    glVertex(-0.04, -0.31)

    glEnd()

    glBegin(GL_POLYGON)
    glVertex(0.02, -0.35)
    glVertex(0.05, -0.44)
    glVertex(0,-0.48)
    glVertex(-0.05, -0.44)
    glVertex(-0.02, -0.35)
    glEnd()

#draw face details
    drawCircle(0.1,0.3,0.1,GL_POLYGON,[0.7,0.9,0.1])
    drawCircle(0.1, -0.3, 0.1, GL_POLYGON, [0.7, 0.9, 0.1])
    drawCircle(0.05, 0.4, 0.55, GL_POLYGON, [0.7, 0.9, 0.1])
    drawCircle(0.05, -0.4, 0.55, GL_POLYGON, [0.7, 0.9, 0.1])
    drawCircle(0.08, 0.4,- 0.2, GL_POLYGON, [0.7, 0.9, 0.1])
    drawCircle(0.08, -0.4,- 0.2, GL_POLYGON, [0.7, 0.9, 0.1])

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(0.32,-0.08)
    glVertex(0.28,-0.12)

    glVertex(-0.32, -0.08)
    glVertex(-0.28, -0.12)
    glEnd()

    drawCircle(0.03,0.11,0.44,GL_POLYGON,[0.9,0.9,0.9])
    drawCircle(0.02,0.2,0.36,GL_POLYGON,[0.9,0.9,0.9])

    drawCircle(0.03, -0.11, 0.44, GL_POLYGON, [0.9, 0.9, 0.9])
    drawCircle(0.02, -0.2, 0.36, GL_POLYGON, [0.9, 0.9, 0.9])

    #drawnet(0.1,0.1)

#draw tears
    drawrect([0.14,0.33,0.17,0.33,0.17,0.05,0.14,0.05],[0.1,0.7,1])
    drawCircle(0.015, 0.155, 0.05, GL_POLYGON, [0.1,0.7,1], -pi, 0)

    drawrect([-0.14, 0.33,- 0.17, 0.33, -0.17, 0.27,- 0.14, 0.27], [0.1, 0.7, 1])
    drawCircle(0.015, -0.155, 0.27, GL_POLYGON, [0.1, 0.7, 1], -pi, 0)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow("first program")
glutDisplayFunc(draw)
glutMainLoop()


