from trigdeg.core import Triangle, Square


figure = Triangle()  # создание экземпляра класса 
figure.add_figure('triangle1')  # инициализация названия
figure.add_vertex('V1', (3, 5, 0)) # инициализация вершины треугольника
figure.add_vertex('V2', (0, 3, -3)) # инициализация вершины треугольника
figure.add_vertex('V3', (5, 0, -2)) # инициализация вершины треугольника


triangle = figure.get_figure('triangle1') # возвращает словарь значений { вершина: ее координаты  }

sides = figure.side_value()
deg = figure.deg_value()
area = figure.get_area()

#print(sides, deg, area)
 


figure2 = Square()  # создание экземпляра класса 
figure2.add_vertex('V1', (4, 6, 1)) # инициализация вершины 
figure2.add_vertex('V2', (1, 4, -2)) # инициализация вершины 
figure2.add_vertex('V3', (6, 1, -1)) # инициализация вершины
figure2.add_vertex('V4', (-1, 5, 1)) # инициализация вершины 
figure2.add_figure('squear')
square = figure2.get_figure('squear') # возвращает словарь значений { вершина: ее координаты  }
area2 = figure2.get_area() # инициализация названия
print(area2)