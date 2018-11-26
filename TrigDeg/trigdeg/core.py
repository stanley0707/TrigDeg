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
        self.V1_V2 = 1
        self.V2_V3 = 1
        self.V1_V3 = 1
        self.cos_V1 = None
        self.cos_V2 = None
        self.cos_V3 = None

    # adding a shape to the parent class field
    def add_figure(self, key):
        self.name_space[key] = self.vertex

    def get_figure(self, key):
        return self.name_space.get(key)

    def remove_figure(self, key):
        return self.name_space.get(key)



class Triangle(FigureInitialize):
    
    def add_vertex_coord(self, key, *args):
        self.vertex[key] = args

    def get_vertex(self, key):
        for item in self.name_space.values():
            for key in item:
                return item.get(key)

    # side equations AB, BC, AC
    def side_value(self):

        key = [key for key in self.vertex.keys()]
        x1, y1, z1 = self.vertex.get(key[0])
        x2, y2, z2 = self.vertex.get(key[1])
        x3, y3, z3 = self.vertex.get(key[2])
        
        self.V1_V2 = round(decimal.Decimal(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)), 1)
        self.V2_V3 = round(decimal.Decimal(math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2 + (z2 - z3) ** 2)), 1)
        self.V1_V3 = round(decimal.Decimal(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2 + (z1 - z3) ** 2)), 1)
        
        Triangle.deg_value(self)
        
        return "{}, {}, {}".format(self.V1_V2, self.V2_V3, self.V1_V3)
    
    
    # Calculation of the sides of a triangle by the cosine theorem.
    # cos a = (b**2 + c**2 - a**2) / (2bc)  
    def deg_value(self):
        
        a, b, c = self.V1_V2, self.V2_V3, self.V1_V3
        self.cos_V1 = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 3)
        self.cos_V2 = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))), 3) 
        self.cos_V3 = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * c * b))), 3)
        
        return "{}, {}, {}".format(self.cos_V1, self.cos_V2, self.cos_V3)