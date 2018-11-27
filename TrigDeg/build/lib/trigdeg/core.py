# -*- coding: utf-8 -*-
# ------------------------------------------------- ------------------------------
# Module for trigonometric calculations. Accepts calls through the interface and values
# Parent - FigureInitialize
#
# Reassignment of base classes no
#
# name_space =  "name" of figure", [attributes] type {dictionary}
# vertex =  "name" of vertices of a square, ["attributes"], type {dictionary}
# V_V  = sides of the shape, ["attributes"], type (int)
# cos_V1 = cosine of an angle, ["attributes"],type (int)  
# method names - semantic values of functions
# reference example> README.md /
# [1] "Syntax Description Language ..."
#-------------------------------------------------------------------------------
import math
import decimal


class FigureInitialize:
    """ The base class of figure. Designe pattern - Singleton."""
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        """ __name_space static attribute of class, wo take key and value.
        key mast a name of figure, value mast be a quantity of sides  """
        self.name_space = {}
        self.vertex = {}

    # adding a shape to the parent class field
    def add_figure(self, key):
        self.name_space[key] = self.vertex

    def get_figure(self, key):
        return self.name_space.get(key)

    def _get_key(self):
        return [key for key in self.vertex.keys()]
    
    def remove_figure(self, key):
        return self.name_space.get(key)

    def add_vertex(self, key, *args):
        try:
            len(args[0]) >= 3  
            self.vertex[key] = args[0]
        except: 
            raise CordError('invalid value')

    def get_vertex(self, key):
        for item in self.name_space.values():
            for key in item:
                return item.get(key)


class Triangle(FigureInitialize):

    def __init__(self):
        super(Triangle, self).__init__()
        self.side = {}
        self.cos = {}
        self.area = {}


    # side equations AB, BC, AC
    def side_value(self):

        key = self._get_key()
        sides = ['side_'+key[0] +'_'+ key[1], 'side_'+key[1] +'_'+ key[2], 'side_'+key[0] +'_'+ key[2]]
        _x1, _y1, _z1 = self.vertex.get(key[0])
        _x2, _y2, _z2 = self.vertex.get(key[1])
        _x3, _y3, _z3 = self.vertex.get(key[2])
        
        V1_V2 = round(decimal.Decimal(
            math.sqrt((_x1 - _x2) ** 2 + (_y1 - _y2) ** 2 + (_z1 - _z2) ** 2)), 1)
        V2_V3 = round(decimal.Decimal(
            math.sqrt((_x2 - _x3) ** 2 + (_y2 - _y3) ** 2 + (_z2 - _z3) ** 2)), 1)
        V1_V3 = round(decimal.Decimal(
            math.sqrt((_x1 - _x3) ** 2 + (_y1 - _y3) ** 2 + (_z1 - _z3) ** 2)), 1)
        
        self.side = dict(zip(sides, [float(V1_V2), float(V2_V3), float(V1_V3)]))
        
        return self.side
    
    
    # Calculation of the sides of a triangle by the cosine theorem.
    # cos a = (b**2 + c**2 - a**2) / (2bc)  
    def deg_value(self):
        key = self._get_key()
        a, b, c = self.side.values()
        cos_key = ['cos_' + key[0], 'cos_'+ key[1], 'cos_'+ key[2]]
        
        self.cos_V1 = round(math.degrees(
            math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 3)
        self.cos_V2 = round(math.degrees(
            math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 3) 
        self.cos_V3 = round(math.degrees(
            math.acos((b**2 + c**2 - a**2) / (2 * c * b))), 3)
        
        self.cos = dict(zip(cos_key, [float(self.cos_V1), float(self.cos_V2), float(self.cos_V3)]))
        
        return self.cos


    def get_area(self):
        a, b, c = self.side.values()
        half_meter = (a + b + c) / 2
        self.area = dict(zip('a', [round( half_meter * (half_meter - a)*(half_meter - b)*(half_meter - c),3)]))
        return self.area


class Square(FigureInitialize):
    """docstring for ClassName"""
    def __init__(self):  
        super(Square, self).__init__()
        self.side = {}
        self.cos = {}
        self.area = {}

    def _square_calc(self):
        out = []
        key = self._get_key()
        
        i = int(len(key)-2)
        while i:
            triangle = Triangle()
            triangle.add_vertex(key[0], self.vertex.get(key[0]))
            triangle.add_vertex(key[i], self.vertex.get(key[i]))
            triangle.add_vertex(key[i+1], self.vertex.get(key[i+1]))
            triangle.add_figure('__inside_'+ str(i))
            
            out += [triangle.side_value(), triangle.deg_value(), triangle.get_area()]

            i-=1            
        return out

    # area 
    def get_area(self):
        area = []
        value = self._square_calc()
        
        for i in value:
            if i.get('a'):
                area.append(i.get('a'))
        
        return sum(area)


