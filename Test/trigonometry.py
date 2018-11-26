from trigdeg.core import Triangle


figure = Triangle()

figure.add_vertex_coord('V1', 3, 5, 0),
figure.add_vertex_coord('V2', 0, 3, -3),
figure.add_vertex_coord('V3', 5, 0, -2)

figure.add_figure('triangle1')

triangle = figure.get_figure('triangle1')
side_a = figure.get_vertex('V1')
side_b = figure.get_vertex('V2')
side_c = figure.get_vertex('V3')
sides = figure.side_value()
deg = figure.deg_value()
 