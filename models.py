"""
class: box, smallbox
version 0.10
"""
# import os
import math
# import sys
from dxfwrite import DXFEngine as dxf

version__ = "$ 0.10 dos for modules and classes $"

#  версия 0.1 скелет первого объекта коробка
#  версия 0.2 объекты модели в разных сло
#  версия 0.3 model boxv
#  версия 0.4 model boxv
#  версия 0.5 smallbo#
#  версия 0.6 smallbo top

#  версия 0.7 clear class
#  версия 0.8 one layer - one detal
#  версия 0.9 smallbox FACE, BOTTOM
#  версия 0.9 smallbox FACE, BOTTOM
#  версия 0.10 doc for a class
#  версия 0.11 табурет
#  версия 0.11.1 табурет царга
#  версия 0.12 исправление ошибок
#  версия 0.13 справление ошибок ножки табурута

#  функции для дуг


def angle(x1, y1, x2, y2, x3, y3, x4, y4):
    a = math.degrees(math.atan((y2 - y1) / (x2 - x1)) - math.atan((y4 - y3) / (x4 - x3)))  # math.degrees
    return a


def sqr(arg):
    return arg * arg


def center(x1,  y1,  x2,  y2,  x3,  y3):
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


def rotate(x0,  y0,  alpha,  x,  y,  x1 = 0,  y1 = 0):
    #  координаты после вращения
    x1 = (x - x0) * math.cos(alpha) - (y - y0) * math.sin(alpha) + x0
    y1 = (x - x0) * math.sin(alpha) + (y - y0) * math.cos(alpha) + y0
    return x1, y1
# ----------------------------------------------------------
#  box simply версия 0.2 испавлена высота боковой стенки


class box:
    """
    calculated a simple box
    """
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
    infoimage = 'box.jpeg'
    # правая стенка
    r1x = 0
    r1y = 0
    r1w = 1
    r1h = 1

    # верхняя стенка
    r102x = 0
    r102y = 0
    r102w = 1
    r102h = 1

    # передняя стенка
    r203x = 0
    r203y = 0
    r203w = 1
    r320h = 1

    def compute(self):  # ширина поля рисунка

        #  правая стерка
        self.r1w = self.width  # (ширина панели - левое поле - правое поле -  вн. поле) / 2
        self.r1h = self.height  # ширина - левое поле - правое поле - фреза - фреза /2-вн.поле

        # верхняя стенка
        self.r102w = self.deep - (self.thickness * 2.0)
        self.r102h = self.height
        # передняя стенка
        self.r203w = self.deep
        self.r203h = self.width
        # self.r203h =  self.r1h


class taburet:
    """
    табурет
    """
    width = 350
    height = 300
    deep = 240
    thickness = 4.0
    clearance = 0.2

    info1 = 'табурет'
    info2 = 'малый, ширина: 350'
    info3 = 'высота: 300'
    info4 = 'глубина: 240'
    info5 = 'расчёт по внешним размерам'

    infoimage = 'taburet.jpeg'
    # rigth side nogka
    r1x = 0
    r1y = 0
    r1w = 1
    r1h = 1

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
    l14y1 = 0

    l15x = 0
    l15y = 0
    l15x1 = 0
    l15y1 = 0

    l16x = 0
    l16y = 0
    l16x1 = 0
    l16y1 = 0

    arc1x = 0
    arc1y = 0
    arc1r = 30.0
    arc1sangle = 180.0
    arc1eangle = 270.0

    arc2x = 0
    arc2y = 0
    arc2r = 25.0
    arc2sangle = 90.0
    arc2eangle = 270.0

    arc3x = 0
    arc3y = 0
    arc3r = 30.0
    arc3sangle = 90.0
    arc3eangle = 180.0

    # top figure kryshka
    l101x = 0
    l101y = 0
    l101x1 = 0
    l101y1 = 0

    l102x = 0
    l102y = 0
    l102x1 = 0
    l102y1 = 0

    l103x = 0
    l103y = 0
    l103x1 = 0
    l103y1 = 0

    l104x = 0
    l104y = 0
    l104x1 = 0
    l104y1 = 0

    r101x = 0
    r101y = 0
    r101w = 0
    r101h = 0

    r102x = 0
    r102y = 0
    r102w = 0
    r102h = 0

    r103x = 0
    r103y = 0
    r103w = 0
    r103h = 0

    r104x = 0
    r104y = 0
    r104w = 0
    r104h = 0

    r105x = 0
    r105y = 0
    r105w = 0
    r105h = 0

    r106x = 0
    r106y = 0
    r106w = 0
    r106h = 0

    r107x = 0
    r107y = 0
    r107w = 0
    r107h = 0

    arc101x = 0
    arc101y = 0
    arc101r = 30.0
    arc101sangle = 180.0
    arc101eangle = 270.0

    arc102x = 0
    arc12y = 0
    arc102r = 30.0
    arc102sangle = 90.0
    arc102eangle = 180.0

    arc103x = 0
    arc103y = 0
    arc103r = 30.0
    arc103sangle = 0.0
    arc103eangle = 90.0

    arc104x = 0
    arc104y = 0
    arc104r = 30.0
    arc104sangle = 270.0
    arc104eangle = 360.0

    # carga
    l201x = 0
    l201y = 0
    l201x1 = 0
    l201y1 = 0

    l202x = 0
    l202y = 0
    l202x1 = 0
    l202y1 = 0

    l203x = 0
    l203y = 0
    l203x1 = 0
    l203y1 = 0

    l204x = 0
    l204y = 0
    l204x1 = 0
    l204y1 = 0

    l205x = 0
    l205y = 0
    l205x1 = 0
    l205y1 = 0

    l206x = 0
    l206y = 0
    l206x1 = 0
    l206y1 = 0

    l207x = 0
    l207y = 0
    l207x1 = 0
    l207y1 = 0

    l208x = 0
    l208y = 0
    l208x1 = 0
    l208y1 = 0

    l209x = 0
    l209y = 0
    l209x1 = 0
    l209y1 = 0

    l210x = 0
    l210y = 0
    l210x1 = 0
    l210y1 = 0

    l211x = 0
    l211y = 0
    l211x1 = 0
    l211y1 = 0

    l212x = 0
    l212y = 0
    l212x1 = 0
    l212y1 = 0

    def compute(self):  # ширина поля рисунка
        # top крышка
        self.arc101x = self.thickness
        self.arc101y = self.thickness
        self.arc101r = self.thickness

        # self.l101x = self.r4x + 20.0
        self.l101y = self.thickness

        # self.l101x1 = self.r4x + self.r4w - 20.0
        self.l101y1 = self.deep - self.thickness
        # l-t angle
        self.arc102x = self.arc101x
        self.arc102y = self.arc101y + (self.deep - (self.thickness * 2.0))
        self.arc102r = self.thickness

        self.l102x = self.thickness
        self.l102y = self.deep
        self.l102x1 = self.width - self.thickness
        self.l102y1 = self.l102y

        # r-t angle
        self.arc103x = self.width - self.thickness
        self.arc103y = self.arc102y
        self.arc103r = self.arc102r

        self.l103x = self.width
        self.l103y = self.l101y1

        self.l103x1 = self.l103x
        self.l103y1 = self.l101y

        # r-b angle
        self.arc104x = self.arc103x
        self.arc104y = self.arc101y
        self.arc104r = self.arc101r

        self.l104x = self.l102x1
        # self.l104y = self.l102x
        self.l104x1 = self.l102x
        # self.l104y1 = self.l102x

        self.r101x = 20.0 - self.clearance
        self.r101y = 20.0 - self.clearance
        self.r101w = self.thickness + (self.clearance * 2.0)
        self.r101h = (self.thickness * 2.0) + (self.clearance * 2.0)

        self.r102x = self.r101x  # ((self.deep / 2.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r102y = (self.deep / 2.0) - (self.thickness * 1.5) - self.clearance
        self.r102w = self.thickness + (self.clearance * 2.0)
        self.r102h = (self.thickness * 3.0) + (self.clearance * 2.0)

        self.r103x = self.r101x  # - (self.thickness / 2.0) - self.clearance
        self.r103y = self.deep - 20.0 - (self.thickness * 2.0) - self.clearance
        self.r103w = self.r101w
        self.r103h = self.r101h

        self.r104x = (self.width / 2.0) - (self.thickness * 2.0) - self.clearance
        self.r104y = (self.deep / 2.0) - (self.thickness / 2.0) - self.clearance
        self.r104w = (self.thickness * 4.0) + (self.clearance * 2.0)
        self.r104h = self.thickness + (self.clearance * 2.0)

        self.r105x = self.width - 20.0 - self.thickness - self.clearance
        self.r105y = self.r101y
        self.r105w = self.r101w
        self.r105h = self.r101h

        self.r106x = self.r105x
        self.r106y = self.r102y
        self.r106w = self.r102w
        self.r106h = self.r102h

        self.r107x = self.r105x
        self.r107y = self.r103y
        self.r107w = self.r103w
        self.r107h = self.r103h

        # ножка
        # self.l2y = self.l1y1
        self.l1x1 = self.l1x  # deep / 2.0) - self.thickness
        self.l1y1 = self.thickness * 2.0

        self.l2x = self.l1x1
        self.l2y = self.l1y1
        self.l2x1 = self.thickness / 2.0  # self.l1x#deep / 2.0) - self.thickness
        self.l2y1 = self.l2y

        self.l3x = self.l2x1
        self.l3y = self.l2y1
        self.l3x1 = self.l3x
        self.l3y1 = self.l3y + (((self.deep - 40.0) - (self.thickness * 7.0)) / 2.0)

        self.l4x = self.l3x1
        self.l4y = self.l3y1
        # self.l4x1 = self.l3x + (self.thickness * 2.0)
        self.l4y1 = self.l4y

        self.l5x = self.l4x1
        self.l5y = self.l4y1
        self.l5x1 = self.l5x
        self.l5y1 = self.l5y + (self.thickness * 3.0)

        self.l6x = self.l5x1
        self.l6y = self.l5y1
        self.l6x1 = self.l6x + (self.thickness / 2.0)
        self.l6y1 = self.l6y  # левый нижний

        self.l7x = self.l6x1
        self.l7y = self.l6y1
        self.l7x1 = self.l2x1
        self.l7y1 = self.l7y + (((self.deep - 40.0) - (self.thickness * 7.0)) / 2.0)

        self.l8x = self.l7x1
        self.l8y = self.l7y1
        # self.l8x1 = self.l8x
        self.l8y1 = self.l8y  # - (self.thickness / 2.0)

        self.l9x = self.l8x1
        self.l9y = self.l8y1
        self.l9x1 = self.l9x
        self.l9y1 = self.l9y + (self.thickness * 2.0)

        self.l10x = self.l9x1
        self.l10y = self.l9y1
        self.l10x1 = (self.l9x - self.thickness) + 50.0
        self.l10y1 = self.l10y

        p1x = self.l10x1
        p1y = self.l10y1
        p2x = ((self.height - 100.0) / 2.0) + (self.thickness / 2.0) + 50.0
        p2y = (self.l10y1 - 20.0)
        p3x = (self.height - 50.0) + (self.thickness / 2.0)
        p3y = p1y
        # print (p1x, p1y, p2x,p2y, p3x, p3y)

        self.arc1x, self.arc1y = center(p1x, p1y, p2x, p2y, p3x, p3y)
        self.arc1r = math.sqrt(sqr(self.arc1x - p1x) + sqr(self.arc1y - p1y))
        # print (self.arc1y)
        alpha = angle(self.arc1x, self.arc1y, p1x, p1y, self.arc1x, self.arc1y, p3x, p3y)
        # print (alpha)
        self.arc1sangle = 270.0 - ((180.0 - alpha) / 2.0)
        self.arc1eangle = 270.0 + ((180.0 - alpha) / 2.0)

        self.l11x = p3x
        self.l11y = self.l10y1
        self.l11x1 = self.height - (self.thickness / 2.0)
        self.l11y1 = self.l9y1  # левый нижний

        self.l12x = self.l11x1
        self.l12y = self.l11y1
        self.l12x1 = self.l12x
        self.l12y1 = self.l12y - ((self.l12y - 50.0) / 2.0)  # левый нижний

        self.arc2x = self.l12x
        self.arc2y = self.l12y / 2.0

        self.l13x = self.l12x1
        self.l13y = (self.l11y1 - 50.0) / 2.0
        self.l13x1 = self.l13x  # - (self.thickness* * 2.0)
        # self.l13y1 = self.l10y#  левый нижний

        self.l14x = self.l11x1
        # self.l14y = self.l11y1
        self.l14x1 = self.l11x
        # self.l14y1 = self.l14y#  левый нижний
        p1x = self.l11x
        p1y = 0
        p2x = ((self.height - 100.0) / 2.0) + (self.thickness / 2.0) + 50.0
        p2y = 20.0
        p3x = self.l10x1
        p3y = 0
        # print (p1x, p1y, p2x,p2y, p3x, p3y)
        self.arc3x, self.arc3y = center(p1x, p1y, p2x, p2y, p3x, p3y)
        self.arc3r = math.sqrt(sqr(self.arc3x - p1x) + sqr(self.arc3y - p1y))
        # print (self.arc1y)
        alpha = angle(self.arc3x, self.arc3y, p1x, p1y, self.arc3x, self.arc3y, p3x, p3y)
        # print (alpha)
        self.arc3sangle = 90.0 - ((180 - alpha) / 2.0)
        self.arc3eangle = 90.0 + ((180 - alpha) / 2.0)

        self.l15x = self.l10x1
        # self.l15y = p1y
        # self.l15x1 = self.l15x# deep - (self.thickness* * 2.0)
        # self.l15y1 = self.height#  левый нижний
        self.r1x = (120.0 + (self.thickness / 2.0)) - (self.thickness * 2.0) - self.clearance  # корректирование вычисления
        print("r1x=", self.r1x)
        self.r1y = (self.l10y / 2.0) - (self.thickness / 2.0) - self.clearance
        self.r1w = (self.thickness * 2.0) + (self.clearance * 2.0)
        self.r1h = self.thickness + (self.clearance * 2.0)

        # передняя сторон царга-----------------------------------------------
        self.l201y1 = self.thickness * 2.0

        self.l202y = self.l201y1
        self.l202x1 = (self.thickness / 2.0)
        self.l202y1 = self.l202y

        self.l203x = self.l202x1
        self.l203y = self.l202y1
        self.l203x1 = self.l203x
        self.l203y1 = 120.0

        self.l204x = self.l203x1
        self.l204y = self.l203y1
        self.l204x1 = self.l204x + ((self.width - 40.0 - (self.thickness * 6.0)) / 2.0)
        self.l204y1 = self.l204y

        self.l205x = self.l204x1
        self.l205y = self.l204y1
        self.l205x1 = self.l205x
        self.l205y1 = self.l205y + (self.thickness / 2.0)

        self.l206x = self.l205x1
        self.l206y = self.l205y1
        self.l206x1 = self.l206x + (self.thickness * 4.0)
        self.l206y1 = self.l206y  # левый нижний

        self.l207x = self.l206x1
        self.l207y = self.l206y1
        self.l207x1 = self.l207x
        self.l207y1 = self.l205y

        self.l208x = self.l207x1
        self.l208y = self.l207y1
        self.l208x1 = self.l208x + ((self.width - 40.0 - (self.thickness * 6.0)) / 2.0)
        self.l208y1 = self.l208y

        self.l209x = self.l208x1
        self.l209y = self.l203y1
        self.l209x1 = self.l209x
        self.l209y1 = self.l203y

        self.l210x = self.l209x1
        self.l210y = self.l209y1
        self.l210x1 = self.l210x + (self.thickness / 2.0)
        self.l210y1 = self.l210y

        self.l211x = self.l210x1
        self.l211y = self.l210y1
        self.l211x1 = self.l211x
        # self.l211y1 = self.height#  левый нижний

        self.l212x = self.l211x1
        self.l212y = self.l211y1
        # self.l212x1 = (self.width / 4.0) + self.thickness
        # self.l212y1 = -(self.thickness)#  левый нижний


class smallbox:
    """
    ящик на шипах
    """
    width = 100
    height = 100
    deep = 100
    thickness = 4.0
    clearance = 0.2

    info1 = 'чертёж малого корпуса'
    info2 = 'генерация трёх чертежей'
    info3 = 'стенки дублируются'
    info4 = 'на винтах и шипах'
    info5 = 'расчёт по внутреннему размеру'

    infoimage = 'smallbox.jpeg'
    # rigth side
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
    # top figure
    l101x = 0
    l101y = 0
    l101x1 = 0
    l101y1 = 0

    l102x = 0
    l102y = 0
    l102x1 = 0
    l102y1 = 0

    l103x = 0
    l103y = 0
    l103x1 = 0
    l103y1 = 0

    l104x = 0
    l104y = 0
    l104x1 = 0
    l104y1 = 0

    r101x = 0
    r101y = 0
    r101w = 0
    r101h = 0

    r102x = 0
    r102y = 0
    r102w = 0
    r102h = 0

    r103x = 0
    r103y = 0
    r103w = 0
    r103h = 0

    r104x = 0
    r104y = 0
    r104w = 0
    r104h = 0

    arc101x = 0
    arc101y = 0
    arc101r = 30.0
    arc101sangle = 180.0
    arc101eangle = 270.0

    arc102x = 0
    arc12y = 0
    arc102r = 30.0
    arc102sangle = 90.0
    arc102eangle = 180.0

    arc103x = 0
    arc103y = 0
    arc103r = 30.0
    arc103sangle = 0.0
    arc103eangle = 90.0

    arc104x = 0
    arc104y = 0
    arc104r = 30.0
    arc104sangle = 270.0
    arc104eangle = 360.0

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

    c101x = 0
    c101y = 0
    c101r = 30.0

    c102x = 0
    c102y = 0
    c102r = 30.0

    c103x = 0
    c103y = 0
    c103r = 30.0

    c104x = 0
    c104y = 0
    c104r = 30.0
    # figure dno
    l151x = 0
    l151y = 0
    l151x1 = 0
    l151y1 = 0

    l152x = 0
    l152y = 0
    l152x1 = 0
    l152y1 = 0

    l153x = 0
    l153y = 0
    l153x1 = 0
    l153y1 = 0

    l154x = 0
    l154y = 0
    l154x1 = 0
    l154y1 = 0

    r151x = 0
    r151y = 0
    r151w = 0
    r151h = 0

    r152x = 0
    r152y = 0
    r152w = 0
    r152h = 0

    r153x = 0
    r153y = 0
    r153w = 0
    r153h = 0

    r154x = 0
    r154y = 0
    r154w = 0
    r154h = 0

    r155x = 0
    r155y = 0
    r155w = 0
    r155h = 0

    r156x = 0
    r156y = 0
    r156w = 0
    r156h = 0

    r157x = 0
    r157y = 0
    r157w = 0
    r157h = 0

    r158x = 0
    r158y = 0
    r158w = 0
    r158h = 0

    arc151y = 0
    arc151r = 30.0
    arc151sangle = 180.0
    arc151eangle = 270.0

    arc152x = 0
    arc152y = 0
    arc152r = 30.0
    arc152sangle = 90.0
    arc152eangle = 180.0

    arc153x = 0
    arc153y = 0
    arc153r = 30.0
    arc153sangle = 0.0
    arc153eangle = 90.0

    arc154x = 0
    arc154y = 0
    arc154r = 30.0
    arc154sangle = 270.0
    arc154eangle = 360.0

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
    # face side
    l201x = 0
    l201y = 0
    l201x1 = 0
    l201y1 = 0

    l202x = 0
    l202y = 0
    l202x1 = 0
    l202y1 = 0

    l203x = 0
    l203y = 0
    l203x1 = 0
    l203y1 = 0

    l204x = 0
    l204y = 0
    l204x1 = 0
    l204y1 = 0

    l205x = 0
    l205y = 0
    l205x1 = 0
    l205y1 = 0

    l206x = 0
    l206y = 0
    l206x1 = 0
    l206y1 = 0

    l207x = 0
    l207y = 0
    l207x1 = 0
    l207y1 = 0

    l208x = 0
    l208y = 0
    l208x1 = 0
    l208y1 = 0

    l209x = 0
    l209y = 0
    l209x1 = 0
    l209y1 = 0

    l210x = 0
    l210y = 0
    l210x1 = 0
    l210y1 = 0

    l211x = 0
    l211y = 0
    l211x1 = 0
    l211y1 = 0

    l212x = 0
    l212y = 0
    l212x1 = 0
    l212y1 = 0

    l213x = 0
    l213y = 0
    l213x1 = 0
    l213y1 = 0

    l214x = 0
    l214y = 0
    l214x1 = 0
    l24y1 = 0

    l215x = 0
    l215y = 0
    l215x1 = 0
    l215y1 = 0

    l216x = 0
    l216y = 0
    l216x1 = 0
    l216y1 = 0

    def compute(self):  # ширина поля рисунка

        # правая сторон
        self.l1y1 = self.height

        self.l2y = self.l1y1
        self.l2x1 = (self.deep / 2.0) - self.thickness
        self.l2y1 = self.height

        self.l3x = self.l2x1
        self.l3y = self.l2y1
        self.l3x1 = self.l3x
        self.l3y1 = self.l3y + self.thickness

        self.l4x = self.l3x1
        self.l4y = self.l3y1
        self.l4x1 = self.l3x + (self.thickness * 2.0)
        self.l4y1 = self.l4y

        self.l5x = self.l4x1
        self.l5y = self.l4y1
        self.l5x1 = self.l5x
        self.l5y1 = self.height

        self.l6x = self.l5x1
        self.l6y = self.l5y1
        self.l6x1 = self.deep
        self.l6y1 = self.height  # левый нижний

        self.l7x = self.l6x1
        self.l7y = self.l6y1
        self.l7x1 = self.l7x
        # self.l7y1 = self.height

        self.l8x = self.l7x1
        self.l8y = self.l7y1
        self.l8x1 = ((self.deep / 4.0) * 3.0) + self.thickness

        # self.l8y1 = self.height
        self.l9x = self.l8x1
        self.l9y = self.l8y1
        self.l9x1 = self.l9x
        self.l9y1 = -(self.thickness)

        self.l10x = self.l9x1
        self.l10y = self.l9y1
        self.l10x1 = self.l9x - (self.thickness * 2.0)
        self.l10y1 = self.l10y

        self.l11x = self.l10x1
        self.l11y = self.l10y1
        self.l11x1 = self.l11x
        # self.l11y1 = self.height#  левый нижний

        self.l12x = self.l11x1
        self.l12y = self.l11y1
        self.l12x1 = (self.deep / 4.0) + self.thickness
        # self.l12y1 = -(self.thickness)#  левый нижний

        self.l13x = self.l12x1
        self.l13y = self.l12y1
        self.l13x1 = self.l13x  # - (self.thickness* * 2.0)
        self.l13y1 = self.l10y  # левый нижний

        self.l14x = self.l13x1
        self.l14y = self.l13y1
        self.l14x1 = (self.deep / 4.0) - self.thickness
        self.l14y1 = self.l14y  # левый нижний

        self.l15x = self.l14x1
        self.l15y = self.l14y1
        self.l15x1 = self.l15x  # deep - (self.thickness* * 2.0)
        # self.l15y1 = self.height#  левый нижний

        self.l16x = self.l15x1
        self.l16y = self.l15y1
        # передняя сторон
        self.l201y1 = self.height

        self.l202y = self.l201y1
        self.l202x1 = (self.width / 2.0) - self.thickness
        self.l202y1 = self.height

        self.l203x = self.l202x1
        self.l203y = self.l202y1
        self.l203x1 = self.l203x
        self.l203y1 = self.l203y + self.thickness

        self.l204x = self.l203x1
        self.l204y = self.l203y1
        self.l204x1 = self.l203x + (self.thickness * 2.0)
        self.l204y1 = self.l204y

        self.l205x = self.l204x1
        self.l205y = self.l204y1
        self.l205x1 = self.l205x
        self.l205y1 = self.height

        self.l206x = self.l205x1
        self.l206y = self.l205y1
        self.l206x1 = self.width
        self.l206y1 = self.height  # левый нижний

        self.l207x = self.l206x1
        self.l207y = self.l206y1
        self.l207x1 = self.l207x
        # self.l207y1 = self.height

        self.l208x = self.l207x1
        self.l208y = self.l207y1
        self.l208x1 = ((self.width / 4.0) * 3.0) + self.thickness

        # self.l208y1 = self.height
        self.l209x = self.l208x1
        self.l209y = self.l208y1
        self.l209x1 = self.l209x
        self.l209y1 = -(self.thickness)

        self.l210x = self.l209x1
        self.l210y = self.l209y1
        self.l210x1 = self.l209x - (self.thickness * 2.0)
        self.l210y1 = self.l210y

        self.l211x = self.l210x1
        self.l211y = self.l210y1
        self.l211x1 = self.l211x
        # self.l211y1 = self.height#  левый нижний

        self.l212x = self.l211x1
        self.l212y = self.l211y1
        self.l212x1 = (self.width / 4.0) + self.thickness
        # self.l212y1 = -(self.thickness)#  левый нижний

        self.l213x = self.l212x1
        self.l213y = self.l212y1
        self.l213x1 = self.l213x  # - (self.thickness* * 2.0)
        self.l213y1 = self.l210y  # левый нижний

        self.l214x = self.l213x1
        self.l214y = self.l213y1
        self.l214x1 = (self.width / 4.0) - self.thickness
        self.l214y1 = self.l214y  # левый нижний

        self.l215x = self.l214x1
        self.l215y = self.l214y1
        self.l215x1 = self.l215x  # width - (self.thickness* * 2.0)
        # self.l215y1 = self.height#  левый нижний

        self.l216x = self.l215x1
        self.l216y = self.l215y1
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
        self.l101y1 = self.width + (self.thickness * 2.0)

        self.r101x = self.thickness - (self.thickness / 2.0) - self.clearance
        self.r101y = ((self.width / 2.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r101w = self.thickness + (self.clearance * 2.0)
        self.r101h = (self.thickness * 2.0) + (self.clearance * 2.0)

        # l-t angle
        self.arc102x = self.arc101x
        self.arc102y = self.arc101y + self.width + self.thickness
        self.arc102r = self.thickness

        self.c102x = self.arc102x
        self.c102y = self.arc102y
        self.c102r = self.thickness / 2.0

        self.l102x = self.arc102x
        self.l102y = self.width + (self.thickness * 3.0)

        self.l102x1 = self.deep + (self.thickness * 2.0)
        self.l102y1 = self.l102y

        self.r102x = ((self.deep / 2.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r102y = self.c102y - (self.thickness / 2.0) - self.clearance
        self.r102w = (self.thickness * 2.0) + (self.clearance * 2.0)
        self.r102h = self.thickness + (self.clearance * 2.0)
        # r-t angle
        self.arc103x = (self.thickness * 2.0) + self.deep
        self.arc103y = self.arc102y
        self.arc103r = self.arc102r

        self.c103x = self.arc103x
        self.c103y = self.arc103y
        self.c103r = self.thickness / 2.0

        self.l103x = self.deep + (self.thickness * 3.0)
        self.l103y = self.arc103y

        self.l103x1 = self.l103x
        self.l103y1 = self.arc101y

        self.r103x = self.c103x - (self.thickness / 2.0) - self.clearance
        self.r103y = self.r101y
        self.r103w = self.r101w
        self.r103h = self.r101h
        # r-b angle
        self.arc104x = self.arc103x
        self.arc104y = self.arc101y
        self.arc104r = self.arc101r

        self.c104x = self.arc104x
        self.c104y = self.arc104y
        self.c104r = self.thickness / 2.0

        self.l104x = self.l102x1
        self.l104x1 = self.l102x

        self.r104x = self.r102x
        self.r104y = (self.thickness / 2.0) - self.clearance
        self.r104w = self.r102w
        self.r104h = self.r102h
        # bottom -dno
        self.arc151x = self.thickness
        self.arc151y = self.thickness
        self.arc151r = self.thickness

        self.c151x = self.thickness
        self.c151y = self.thickness
        self.c151r = self.thickness / 2.0

        # self.l151x = self.r4x + 20.0
        self.l151y = self.thickness

        # self.l151x1 = self.r4x + self.r4w - 20.0
        self.l151y1 = self.width + (self.thickness * 2.0)

        self.r151x = self.thickness - (self.thickness / 2.0) - self.clearance
        self.r151y = ((self.width / 4.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r151w = self.thickness + (self.clearance * 2.0)
        self.r151h = (self.thickness * 2.0) + (self.clearance * 2.0)

        self.r152x = self.thickness - (self.thickness / 2.0) - self.clearance
        self.r152y = (((self.width / 4.0) * 3.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r152w = self.thickness + (self.clearance * 2.0)
        self.r152h = (self.thickness * 2.0) + (self.clearance * 2.0)

        # l-t angle
        self.arc152x = self.arc151x
        self.arc152y = self.arc151y + self.width + self.thickness
        self.arc152r = self.thickness

        self.c152x = self.arc152x
        self.c152y = self.arc152y
        self.c152r = self.thickness / 2.0

        self.l152x = self.arc152x
        self.l152y = self.width + (self.thickness * 3.0)

        self.l152x1 = self.deep + (self.thickness * 2.0)
        self.l152y1 = self.l152y

        self.r153x = ((self.deep / 4.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r153y = self.c152y - (self.thickness / 2.0) - self.clearance
        self.r153w = (self.thickness * 2.0) + (self.clearance * 2.0)
        self.r153h = self.thickness + (self.clearance * 2.0)

        self.r154x = (((self.deep / 4.0) * 3.0) - self.clearance - self.thickness) + ((self.thickness / 2.0) * 3.0)
        self.r154y = self.c152y - (self.thickness / 2.0) - self.clearance
        self.r154w = (self.thickness * 2.0) + (self.clearance * 2.0)
        self.r154h = self.thickness + (self.clearance * 2.0)
        # r-t angle
        self.arc153x = (self.thickness * 2.0) + self.deep
        self.arc153y = self.arc152y
        self.arc153r = self.arc152r

        self.c153x = self.arc153x
        self.c153y = self.arc153y
        self.c153r = self.thickness / 2.0

        self.l153x = self.deep + (self.thickness * 3.0)
        self.l153y = self.arc153y

        self.l153x1 = self.l153x
        self.l153y1 = self.arc151y

        self.r155x = self.c153x - (self.thickness / 2.0) - self.clearance
        self.r155y = self.r152y
        self.r155w = self.r151w
        self.r155h = self.r151h

        self.r156x = self.c153x - (self.thickness / 2.0) - self.clearance
        self.r156y = self.r151y
        self.r156w = self.r151w
        self.r156h = self.r151h
        # r-b angle
        self.arc154x = self.arc153x
        self.arc154y = self.arc151y
        self.arc154r = self.arc151r

        self.c154x = self.arc154x
        self.c154y = self.arc154y
        self.c154r = self.thickness / 2.0

        self.l154x = self.l152x1
        self.l154x1 = self.l152x

        self.r157x = self.r154x
        self.r157y = (self.thickness / 2.0) - self.clearance
        self.r157w = self.r154w
        self.r157h = self.r154h

        self.r158x = self.r153x
        self.r158y = (self.thickness / 2.0) - self.clearance
        self.r158w = self.r153w
        self.r158h = self.r153h


class drawmodel:  # версия 0.4 окружности
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
        nameobj = self.model
        nameobj = nameobj.replace('-', '')
        nameobj = nameobj.lower()
        # print (nameobj)
        figureobj = globals().get(nameobj)()
        #  подготавливаем объект ПЕРЕДАЁМ ПАРАМЕТРЫ
        figureobj.width = float(self.width)
        figureobj.height = float(self.height)
        figureobj.deep = float(self.deep)
        figureobj.thickness = float(self.thickness)

        if hasattr(figureobj, 'clearance'):  # есть атрибут отступ,  для псевдофрезы
            figureobj.clearance = float(self.clearance)

        figureobj.compute()  # float(self.lf),  float(self.tf),  float(self.rf),  float(self.bf) )
        # обработка линий в цикле
        for X in range(1, 49):
            drawing.add_layer('SIDER', color=1, linetype = 'SOLID')
            # vt = ('l%dx' % X)
            #  прямоугольникик в цикле
            if hasattr(figureobj, ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'SIDER')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'SIDER')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'SIDER')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'SIDER')
                drawing.add(linecyc)
                # line = dxf.line((1.2,  3.7),  (5.5,  9.7),  layer='LINES')

        #  чертим переднюю стенку
        for X in range(50, 99):
            drawing.add_layer('SIDEL', color=1, linetype = 'SOLID')
            # vt = ('l%dx' % X)
            #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'SIDEL')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'SIDEL')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'SIDEL')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'SIDEL')
                drawing.add(linecyc)
                # line = dxf.line((1.2,  3.7),  (5.5,  9.7),  layer='LINES')

        # фигура крышки
        for X in range(100, 149):
            drawing.add_layer('TOP', color=7, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh,  color=7, layer = 'TOP')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'TOP')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'TOP')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'TOP')
                drawing.add(linecyc)
        # фигура дно
        for X in range(150,  199):
            drawing.add_layer('BOTTOM', color=3, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'BOTTOM')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'BOTTOM')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'BOTTOM')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'BOTTOM')
                drawing.add(linecyc)
        # фигура  днa
        for X in range(200,  249):
            drawing.add_layer('FACE', color=3, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'FACE')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'FACE')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'FACE')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'FACE')
                drawing.add(linecyc)
        # фигура  днa
        for X in range(250,  299):
            drawing.add_layer('ANFACE', color=3, linetype = 'SOLID')
        # vt = ('l%dx' % X)
        #  прямоугольникик в цикле
            if hasattr(figureobj,  ('r%dx' % X)):  # есть прямоугольник
                rx = getattr(figureobj,  ('r%dx' % X))
                ry = getattr(figureobj,  ('r%dy' % X))
                rw = getattr(figureobj,  ('r%dw' % X))
                rh = getattr(figureobj,  ('r%dh' % X))
                rect = dxf.rectangle((rx,  ry),  rw,  rh, layer = 'ANFACE')
                drawing.add(rect)
            if hasattr(figureobj,  ('c%dx' % X)):  # есть окружность

                cx = getattr(figureobj,  ('c%dx' % X))
                cy = getattr(figureobj,  ('c%dy' % X))
                cr = getattr(figureobj,  ('c%dr' % X))

                circle = dxf.circle(cr, (cx,  cy), layer = 'ANFACE')
                drawing.add(circle)
            #  есть дуга для псевдо
            if hasattr(figureobj,  ('arc%dx' % X)):  # есть дуга
                arcx = getattr(figureobj,  ('arc%dx' % X))
                arcy = getattr(figureobj,  ('arc%dy' % X))
                arcr = getattr(figureobj,  ('arc%dr' % X))
                arcsa = getattr(figureobj,  ('arc%dsangle' % X))
                arcse = getattr(figureobj,  ('arc%deangle' % X))
                # рисум прямоугольник псевдофрезы
                arc = dxf.arc(arcr, (arcx,  arcy),  arcsa,  arcse, layer = 'ANFACE')
                drawing.add(arc)
            #  линии в цикле
            if hasattr(figureobj,  ('l%dx' % X)):  # есть линия
                lx = getattr(figureobj,  ('l%dx' % X))
                ly = getattr(figureobj,  ('l%dy' % X))
                lx1 = getattr(figureobj,  ('l%dx1' % X))
                ly1 = getattr(figureobj,  ('l%dy1' % X))
                # print(lx,  ly,  lx1,  ly1)
                linecyc = dxf.line((lx,  ly),  (lx1,  ly1), layer = 'ANFACE')
                drawing.add(linecyc)
#   записываем в файл
        drawing.save()
