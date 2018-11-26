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


class Triangle(FigureInitialize):

    def __init__(self):
        super(Triangle, self).__init__()
        self.side = {}
        self.cos = {}

    def add_vertex_coord(self, key, *args):
        self.vertex[key] = args

    def get_vertex(self, key):
        for item in self.name_space.values():
            for key in item:
                return item.get(key)

    # side equations AB, BC, AC
    def side_value(self):

        key = self._get_key()
        sides = [key[0] +'_'+ key[1], key[1] +'_'+ key[2], key[0] +'_'+ key[2]]
        
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
        
        self.cos_V1 = round(math.degrees(
            math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 3)
        self.cos_V2 = round(math.degrees(
            math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 3) 
        self.cos_V3 = round(math.degrees(
            math.acos((b**2 + c**2 - a**2) / (2 * c * b))), 3)
        
        self.cos = dict(zip(key, [float(self.cos_V1), float(self.cos_V2), float(self.cos_V3)]))
        
        return self.cos



class Square(FigureInitialize):
    """docstring for ClassName"""
    def __init__(self):
        super(Square, self).__init__()

        



figure = Triangle()  # создание экземпляра класса 
figure.add_figure('triangle1')  # инициализация названия
figure.add_vertex_coord('V1', 3, 5, 0) # инициализация вершины треугольника
figure.add_vertex_coord('V2', 0, 3, -3) # инициализация вершины треугольника
figure.add_vertex_coord('V3', 5, 0, -2) # инициализация вершины треугольника


triangle = figure.get_figure('triangle1') # возвращает словарь значений { вершина: ее координаты  }

sides = figure.side_value()
deg = figure.deg_value()

print(sides, deg)
