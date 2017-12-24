import math
import sys,  os
from dxfwrite import DXFEngine as dxf


#  версия 0.1 скелет первого объекта коробка
#  версия 0.2 объекты модели в разных сло
#  версия 0.3 model boxv
#  версия 0.4 model boxv
#  версия 0.5 smallbo# 
#  версия 0.6 smallbo top
#  версия 0.7 clear class

#  функции для дуг
def angle (x1, y1, x2, y2, x3, y3, x4, y4):
    a = math.degrees(math.atan((y2 - y1)/(x2 - x1)) - math.atan((y4 - y3)/(x4 - x3)))# math.degrees
    return a
def sqr(arg):
    return arg * arg


def center( x1,  y1,  x2,  y2,  x3,  y3):
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))
    if G == 0:
        exit
    Cx = (D * E - B * F) / G
    Cy = (A * F - C * E) / G
    return Cx, Cy

def rotate( x0,  y0,  alpha,  x,  y,  x1 = 0,  y1 = 0):
    #  координаты после вращения
    x1 = (x - x0) * math.cos(alpha) - (y - y0) * math.sin(alpha) + x0
    y1 = (x - x0) * math.sin(alpha) + (y - y0) * math.cos(alpha) + y0
    return x1 , y1
# ----------------------------------------------------------
#  box simply версия 0.2 испавлена высота боковой стенки
class box:

    width = 100
    height = 100
    deep = 100
    thickness = 4.0
    clearance = 0.2

    info1 = 'чертёж простого ящика'
    info2 = 'генерация трёх чертежей'
    info3 = 'стенки дублируются'
    info4 = ' '
    info5 = ' '

    # ~ infield = 50.0 # поле между сегментами рисунка горизонтальная
    # ~ hinfield = 50.0 # поле между сегментами рисунка вертикальная
    # ~ wfreza = 0.01
    r1x = 0
    r1y = 0
    r1w = 1
    r1h = 1

    r102x = 0
    r102y = 0
    r102w = 1
    r102h = 1

    r203x = 0
    r203y = 0
    r203w = 1
    r320h = 1

    # def __init__(self):
        # self.wpanel = w
        # self.hpanel = h
    def compute (self): #  ширина поля рисунка


        # ~ передняя стерка
        # ~ self.r1x = lf                                       #  левое поле
        # ~ self.r1y = bf                   #  высота панели - верхнее поле -полфрезы- высота
        self.r1w = self.width #  (ширина панели - левое поле - правое поле -  вн. поле) / 2
        self.r1h = self.height #  ширина - левое поле - правое поле - фреза - фреза /2-вн.поле

        # ~ боковая стенка
        # self.r2x = self.r1x + self.hinfield + self.r1w
        # self.r2y = self.r1y
        self.r102w = self.deep - (self.thickness * 2.0)
        self.r102h =  self.height
        # ~ верхняя стенка
        # self.r2x = self.r1x + self.hinfield + self.r1w
        # self.r2y = self.r1y
        # self.r2w = self.r1w
        self.r203w = self.deep
        self.r203h =  self.width
        # self.r203h =  self.r1h

 # рисунок H-91 версия 0.1
class smallbox:
    width = 100
    height = 100
    deep = 100
    thickness = 4.0
    clearance = 0.2

    info1 = 'чертёж малого корпуса'
    info2 = 'генерация трёх чертежей'
    info3 = 'стенки дублируются'
    info4 = 'на винтах'
    info5 = 'расчёт по внутреннему размер'

    # face side
    l1x = 0
    l1y = 0
    l1x1 = 0
    l1y1 = 0

    l2x = 0
    l2y = 0
    l2x1 = 0
    l2y1 = 0

    l3x = 0
    l3y = 0
    l3x1 = 0
    l3y1 = 0

    l4x = 0
    l4y = 0
    l4x1 = 0
    l4y1 = 0

    l5x = 0
    l5y = 0
    l5x1 = 0
    l5y1 = 0

    l6x = 0
    l6y = 0
    l6x1 = 0
    l6y1 = 0

    l7x = 0
    l7y = 0
    l7x1 = 0
    l7y1 = 0

    l8x = 0
    l8y = 0
    l8x1 = 0
    l8y1 = 0

    l9x = 0
    l9y = 0
    l9x1 = 0
    l9y1 = 0

    l10x = 0
    l10y = 0
    l10x1 = 0
    l10y1 = 0

    l11x = 0
    l11y = 0
    l11x1 = 0
    l11y1 = 0

    l12x = 0
    l12y = 0
    l12x1 = 0
    l12y1 = 0

    l13x = 0
    l13y = 0
    l13x1 = 0
    l13y1 = 0

    l14x = 0
    l14y = 0
    l14x1 = 0
    l4y1 = 0

    l15x = 0
    l15y = 0
    l15x1 = 0
    l15y1 = 0

    l16x = 0
    l16y = 0
    l16x1 = 0
    l16y1 = 0
    # top
    l101x = 0
    l101y = 0
    l101x1 = 1.0
    l101y1 = 1.0

    l102x = 0
    l102y = 0
    l102x1 = 1.0
    l102y1 = 1.0


    l103x = 0
    l103y = 0
    l103x1 = 1.0
    l103y1 = 1.0

    l104x = 0
    l104y = 0
    l104x1 = 1.0
    l104y1 = 1.0
    
    r101x = 0
    r101y = 0
    r101w = 1.0
    r101h = 1.0

    r102x = 0
    r102y = 0
    r102w = 1.0
    r102h = 1.0

    r103x = 0
    r103y = 0
    r103w = 1.0
    r103h = 1.0

    r104x = 0
    r104y = 0
    r104w = 1.0
    r104h = 1.0
        # dno
    r101x = 0
    r101y = 0
    r101w = 1.0
    r101h = 1.0

    r102x = 0
    r102y = 0
    r102w = 1.0
    r102h = 1.0

    r103x = 0
    r103y = 0
    r103w = 1.0
    r103h = 1.0

    r104x = 0
    r104y = 0
    r104w = 1.0
    r104h = 1.0

    r105x = 0
    r105y = 0
    r105w = 1.0
    r105h = 1.0

    r106x = 0
    r106y = 0
    r106w = 1.0
    r106h = 1.0

    r107x = 0
    r107y = 0
    r107w = 1.0
    r107h = 1.0

    r108x = 0
    r108y = 0
    r108w = 1.0
    r108h = 1.0

    r109x = 0
    r109y = 0
    r109w = 1.0
    r109h = 1.0
    
    arc101x = 0
    arc101y = 0
    arc101r = 30.0
    arc101sangle = 0.0
    arc101eangle = 90.0

    arc102x = 0
    arc12y = 0
    arc102r = 30.0
    arc102sangle = 90.0
    arc102eangle = 180.0

    arc103x = 0
    arc103y = 0
    arc103r = 30.0
    arc103sangle = 270.0
    arc103eangle = 360.0

    arc104x = 0
    arc104y = 0
    arc104r = 30.0
    arc104sangle = 180.0
    arc104eangle = 270.0

    c101x = 0
    c101y = 0
    c101r= 30.0

    c102x = 0
    c102y = 0
    c102r = 30.0

    c103x = 0
    c103y = 0
    c103r = 30.0

    c104x = 0
    c104y = 0
    c104r = 30.0
 # dno
    l151x = 0
    l151y = 0
    l151x1 = 1.0
    l151y1 = 1.0

    l152x = 0
    l152y = 0
    l152x1 = 1.0
    l152y1 = 1.0


    l153x = 0
    l153y = 0
    l153x1 = 1.0
    l153y1 = 1.0

    l154x = 0
    l154y = 0
    l154x1 = 1.0
    l154y1 = 1.0
    
    r151x = 0
    r151y = 0
    r151w = 1.0
    r151h = 1.0

    r152x = 0
    r152y = 0
    r152w = 1.0
    r152h = 1.0

    r153x = 0
    r153y = 0
    r153w = 1.0
    r153h = 1.0

    r154x = 0
    r154y = 0
    r154w = 1.0
    r154h = 1.0
        # dno
    r155x = 0
    r155y = 0
    r155w = 1.0
    r155h = 1.0

    r156x = 0
    r156y = 0
    r156w = 1.0
    r156h = 1.0

    r157x = 0
    r157y = 0
    r157w = 1.0
    r157h = 1.0

    r158x = 0
    r158y = 0
    r158w = 1.0
    r158h = 1.0
    
    arc151y = 0
    arc151r = 30.0
    arc151sangle = 0.0
    arc151eangle = 90.0

    arc152x = 0
    arc152y = 0
    arc152r = 30.0
    arc152sangle = 90.0
    arc152eangle = 180.0

    arc153x = 0
    arc153y = 0
    arc153r = 30.0
    arc153sangle = 270.0
    arc153eangle = 360.0

    arc154x = 0
    arc154y = 0
    arc154r = 30.0
    arc154sangle = 180.0
    arc154eangle = 270.0

    c151x = 0
    c151y = 0
    c151r = 30.0

    c152x = 0
    c152y = 0
    c152r = 30.0

    c153x = 0
    c153y = 0
    c153r = 30.0

    c154x = 0
    c154y = 0
    c154r = 30.0

#    def __init__(self):
 #       self.wpanel = w
  #      self.hpanel = h

    def compute (self): #  ширина поля рисунка

        #  контур
        # self.l1x = lf #  левое поле
        # self.r1y = bf #  высота панели - верхнее поле -полфрезы- высота
        # self.l1x1 = self.height
        self.l1y1 = self.height
        
        #self.l2x = self.l1x
        self.l2y = self.l1y1
        self.l2x1 = ((self.deep - (self.thickness * 2.0))/2.0) - self.thickness
        self.l2y1 = self.height

        self.l3x = self.l2x1
        self.l3y = self.l2y1
        self.l3x1 = self.l3x
        self.l3y1 = self.l3y + self.thickness
 
        self.l4x = self.l3x1
        self.l4y = self.l3y1
        self.l4x1 = self.l3x + (self.thickness * 2.0)
        self.l4y1 = self.l3y

        self.l5x = self.l4x1
        self.l5y = self.l4y1
        self.l5x1 = self.l5x
        self.l5y1 = self.height
        
        self.l6x = self.l5x1
        self.l6y = self.l5y1
        self.l6x1 = self.deep - (self.thickness  * 2.0)
        self.l6y1 = self.height#  левый нижний
        
        self.l7x = self.l6x1
        self.l7y = self.l6x1
        self.l7x1 = self.l6x
        # self.l7y1 = self.height
        
        self.l8x = self.l7x1
        self.l8y = self.l7y1
        self.l8x1 =((self.deep - (self.thickness * 2.0)) -((self.deep - (self.thickness * 2.0)) / 4.0)) - (self.thickness *2.0)

       # self.l8y1 = self.height
        self.l9x = self.l8x1
        self.l9y = self.l8y1
        self.l9x1 = self.l9x
        self.l9y1 = -(self.thickness)
        
        self.l10x = self.l9x1
        self.l10y = self.l9y1
        self.l10x1 = self.l9x - (self.thickness  * 2.0)
        # self.l10y1 = self.l10y
        
        self.l11x = self.l10x1
        self.l11y = self.l10y1
        self.l11x1 = self.l11x
        # self.l11y1 = self.height#  левый нижний

        self.l12x = self.l11x1
        self.l12y = self.l11y1
        self.l12x1 = ((self.deep - (self.thickness * 2.0)) / 4.0 ) + (self.thickness *2.0)
        # self.l12y1 = -(self.thickness)#  левый нижний
        
        self.l13x = self.l12x1
        self.l13y = self.l12y1
        self.l13x1 = self.l13x# - (self.thickness* * 2.0)
        # self.l13y1 = self.l13y#  левый нижний
        
        self.l14x = self.l13x1
        self.l14y = self.l13y1
        self.l14x1 = self.l14y - (self.thickness  * 2.0)
        self.l14y1 = self.height#  левый нижний
        
        self.l15x = self.l14x1
        self.l15y = self.l14y1
        self.l15x1 = self.l15x# deep - (self.thickness* * 2.0)
        # self.l15y1 = self.height#  левый нижний
        
        self.l16x = self.l5x1
        self.l16y = self.l5y1
        # self.l16x1 = self.deep - (self.thickness* * 2.0)
        # self.l16y1 = self.height#  левый нижний

         # top
        self.arc101x = self.thickness
        self.arc101y = self.thickness
        self.arc101r = self.thickness
        
        self.c101x = self.thickness
        self.c101y = self.thickness
        self.c101r = self.thickness / 2.0

        # self.l101x = self.r4x + 20.0
        self.l101y = self.thickness

        # self.l101x1 = self.r4x + self.r4w - 20.0
        self.l101y1 = self.thickness + self.width

        self.r101x = self.thickness - (self.thickness / 2.0) - self.clearance
        self.r101y = (self.thickness * 2.0) + (self.thickness / 2.0) + (self.width / 2.0) - self.clearance
        self.r101w =  self.thickness  +  (self.clearance * 2.0)
        self.r101h =  (self.thickness * 2.0) + (self.clearance * 2.0)
        
        # l-t angle
        self.arc102x = self.arc101x
        self.arc102y = (self.arc101y + self.width) - self.thickness
        self.arc102r = self.thickness
        
        self.c102x = self.arc102x
        self.c102y = self.arc102y
        self.c102r = self.thickness / 2.0

        self.l102x = self.arc102x
        self.l102y = self.width + self.thickness

        self.l102x1 = self.deep + self.thickness
        self.l102y1 = self.l102y

        self.r102x =(self.thickness * 2.0) + (self.thickness / 2.0) + (self.deep / 2.0) - self.clearance
        self.r102y = self.width - (self.thickness / 2.0) - self.clearance
        self.r102w = (self.thickness * 2.0) + (self.clearance * 2.0)
        self.r102h = self.thickness  +  (self.clearance * 2.0)
        #r-t angle
        self.arc103x = self.thickness + self.deep
        self.arc103y = self.arc102y
        self.arc103r = self.arc102r
        
        self.c103x = self.arc103x
        self.c103y = self.arc103y
        self.c103r = self.thickness / 2.0

        self.l103x = self.deep + self.thickness
        self.l103y = self.arc103y

        self.l103x1 = self.l103x 
        self.l103y1 = self.arc101y

        self.r103x = self.thickness - (self.thickness / 2.0) - self.clearance
        self.r103y = (self.thickness * 2.0) + (self.thickness / 2.0) + (self.width / 2.0) - self.clearance
        self.r103w =  self.thickness  +  (self.clearance * 2.0)
        self.r103h =  (self.thickness * 2.0) + (self.clearance * 2.0)



class drawmodel: #  версия 0.4 окружности
    # namefile = 'NO-0000'
    # pathsave = ''
    model = 'box'
    width = 100
    height = 100
    deep = 100
    thickness = 6
    clearance = 0.2
    def drawfigure(self):
        #  cretae file

        filename = 'model.dxf'
        drawing = dxf.drawing(filename)
        #  создаём объект
        nameobj=self.model
        nameobj=nameobj.replace('-', '')
        nameobj = nameobj.lower()
        # print (nameobj)
        figureobj = globals().get(nameobj)()
        #  подготавливаем объект ПЕРЕДАЁМ ПАРАМЕТРЫ
        figureobj.width = float(self.width)
        figureobj.height = float(self.height)
        figureobj.deep = float(self.deep)
        figureobj.thickness = float(self.thickness)
        # figureobj.bf = float(self.bf)
        if hasattr(figureobj,  'clearance'):#  есть атрибут отступ,  для псевдофрезы
        #     figureobj.wfreza = self.wfreza
            figureobj.clearance  = float(self.clearance)
        # if hasattr(figureobj,  'findent'):#  есть атрибут отступ,  для псевдофрезы
        #     figureobj.findent = self.findent
        # figureobj.infield = self.infield
        # figureobj.hinfield = self.hinfield
        # print(dir(figureobj))
        # figureobj.compute(self)
        # draw83.findent = float(findent.get()) #  задаём остут для псевдофрезы
        # print ('make object')
        figureobj.compute()# float(self.lf),  float(self.tf),  float(self.rf),  float(self.bf) )
        # print (getattr(figureobj, 'r1x'))

        # # прям для псевдофрезы
        # if hasattr(figureobj,  'pfr1x'):#  есть прямоугольник 24
            # рисум прямоугольник псевдофрезы
           #  pfrect1 = dxf.rectangle((figureobj.pfr1x, figureobj.pfr1y),  figureobj.pfr1w,  figureobj.pfr1h,  color=7)
           #  drawing.add(pfrect1)
        # if hasattr(figureobj,  'pfr2x'):#  есть прямоугольник 24
            # рисум прямоугольник псевдофрезы
           #  pfrect2 = dxf.rectangle((figureobj.pfr2x, figureobj.pfr2y),  figureobj.pfr2w,  figureobj.pfr2h,  color=7)
           #  drawing.add(pfrect2)
        # if hasattr(figureobj,  'pfr3x'):#  есть прямоугольник 24
            # рисум прямоугольник псевдофрезы
            # pfrect3 = dxf.rectangle((figureobj.pfr3x, figureobj.pfr3y),  figureobj.pfr3w,  figureobj.pfr3h,  color=7)
            # drawing.add(pfrect3)

            #  print ('kalevka')
            # kalevka1line = dxf.line( (self.lf,  0),  ( self.lf,  self.hpanel ) )# первая линия
            # kalevka2line = dxf.line( (self.wpanel - self.rf,  0), ( self.wpanel - self.rf,  self.hpanel) )#  вторая линия
            # drawing.add(kalevka1line)
            # drawing.add(kalevka2line)
        # фигуры прередней \ заней стенки
        #  обработка линий в цикле
        for X in range(1, 99):
            drawing.add_layer('FACE-ANFACE',color=1, linetype = 'SOLID')
            # vt = ('l%dx' % X)
            #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):#  есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'FACE-ANFACE')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):#  есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'FACE-ANFACE')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):#  есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'FACE-ANFACE')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):#  есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line( (lx,  ly),  (lx1,  ly1), layer = 'FACE-ANFACE')
                drawing.add(linecyc)
                # line = dxf.line((1.2,  3.7),  (5.5,  9.7),  layer='LINES')

        # фигура правой левой стенки
        for X in range(100, 199):
            drawing.add_layer('SIDER-SIDEL', color=7, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):#  есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh,  color=7, layer = 'SIDER-SIDEL')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):#  есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'SIDER-SIDEL')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):#  есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'SIDER-SIDEL')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):#  есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line( (lx,  ly),  (lx1,  ly1), layer = 'SIDER-SIDE')
                drawing.add(linecyc)
                # line = dxf.line((1.2,  3.7),  (5.5,  9.7),  layer='LINES')
        ## фигура крышки  и днa
        for X in range(200,  299):
            drawing.add_layer('TOP-BOTTOM',color=3, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):#  есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'TOP-BOTTOM')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):#  есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'TOP-BOTTOM')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):#  есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'TOP-BOTTOM')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):#  есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line( (lx,  ly),  (lx1,  ly1), layer = 'TOP-BOTTOM')
                drawing.add(linecyc)
#   записываем в файл
        drawing.save()
