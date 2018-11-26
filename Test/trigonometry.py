from trigdeg.core import Triangle


figure = Triangle()  # создание экземпляра класса 
figure.add_figure('triangle1')  # инициализация названия
figure.add_vertex_coord('V1', 3, 5, 0) # инициализация вершины треугольника
figure.add_vertex_coord('V2', 0, 3, -3) # инициализация вершины треугольника
figure.add_vertex_coord('V3', 5, 0, -2) # инициализация вершины треугольника


triangle = figure.get_figure('triangle1') # возвращает словарь значений { вершина: ее координаты  }

sides = figure.side_value()
deg = figure.deg_value()

print(sides, deg)
 