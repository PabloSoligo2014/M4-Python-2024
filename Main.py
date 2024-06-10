#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''

#import random
from tkinter import Tk, Canvas
from random import randrange



class Figure():
    _posx = 0
    _posy = 0
    _canvas = None
    
    def __init__(self, x, y, canvas):
        self._posx      = x
        self._posy      = y
        self._canvas    = canvas
        
    def draw(self):
        raise NotImplementedError()
    
class Shape(Figure):
    _color = "white"
    pass

    def set_color(self, color):
        self._color = color


class Polygon(Shape):
    _sides = []
    
    def __init__(self, x, y, sides, canvas):
        super(Polygon, self).__init__(x, y, canvas)
        self._sides = sides
    
    
    

class Triangle(Polygon):
    
    def __init__(self, x, y, sides, canvas):
        #Debe cheaquear que la suma de dos lados nunca
        #superen al otro
        for i in range(len(sides)):
            ev = sides[i]
            if (ev>=(sum(sides)-ev)):
                raise Exception("Un lado es mas grande que los otros dos")
        
        super(Triangle, self).__init__(x, y, sides, canvas)
    
    def draw(self):
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        
        A = (0, 0)
        B = (c, 0)
        hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
        dx = (b**2 - hc**2)**0.5
        if abs((c - dx)**2 + hc**2 - a**2) > 0.01: dx = -dx # dx has two solutions
        C = (dx, hc)

        # move away from topleft, scale up a bit, convert to int
        A = (A[0]+self._posx, A[1]+self._posy)
        B = (B[0]+self._posx, B[1]+self._posy)
        C = (C[0]+self._posx, C[1]+self._posy)
        coords = [int((x)) for x in A+B+C]
            
        self._canvas.create_polygon(*coords, outline='black', fill=self._color)
    
    
    
    
class Rectangle(Polygon):
    
    
    def draw(self):
        self._canvas.create_rectangle(self._posx, self._posy, self._posx+self._sides[0], self._posy+self._sides[1], fill=self._color)
    

class Circle(Shape):
       
    _radio = 0
    
    def __init__(self, x, y, radio, canvas):
        super(Circle, self).__init__(x, y, canvas)
        self._radio = radio
        
    def draw(self):
        x0 = self._posx - self._radio
        y0 = self._posy - self._radio
        x1 = self._posx + self._radio
        y1 = self._posy + self._radio
        return self._canvas.create_oval(x0, y0, x1, y1, fill=self._color)
    
    
def createFigures():
    
    figures = []
    for i in range(10):
        #No es necesario importar modulo porque las clases estan en el mismo 
        #modulo
        
        rr = randrange(0,3)
        fig = None
        if rr==0:
            fig = Circle(randrange(0, WIDTHWINDOW), randrange(0, HEIGHTWINDOW), randrange(50,100), w)
        elif rr==1:
            fig = Rectangle( randrange(0, WIDTHWINDOW), randrange(0, HEIGHTWINDOW), [randrange(30,100), randrange(10,50)], w)
        else:
            fig = Triangle(randrange(0, HEIGHTWINDOW), randrange(0, HEIGHTWINDOW), [150,216,100], w)
            
        figures.append(fig)
    
    figures[randrange(0, len(figures))].set_color('red')
    
    return figures


if __name__ == '__main__':
    
    WIDTHWINDOW     = 1000
    HEIGHTWINDOW    = 700
    
    master = Tk()

    w = Canvas(master, width=WIDTHWINDOW, height=HEIGHTWINDOW)
    w.pack()

    
    figures = createFigures()
    
        
    for fig in figures:
        fig.draw()
        
        
    
    master.mainloop()
    
    #canvas = Canvas()
    #canvas.pack(fill=BOTH, expand=1)
    #canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)