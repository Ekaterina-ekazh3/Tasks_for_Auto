# Требуется скрипт, который мог бы перекрашивать пикселы скриншота формы, лежащие вне замкнутых контуров,
# ограничивающих контролы, расположенные на этой форме.
#
# Скрипт получает на вход
# 1. или png файл, скриншота, или соответствующий ему двумерный массив,
# 2. координаты точки, с которой его следут начиеать обходить (по умолчанию: 0, 0 (то есть, верхний левый угол),
# 3. подмешиваемый цвет в виде одной из трёх строковых констант: "RED", "GREEN" или "BLUE".
#
# Если на вход получен png файл, то он скрипт преобразует его в двумерный массив.
# Скрипт обходит массив, начиная с указанной точки, и строит список связанных с ней точек, того же (или близкого) цвета.
#
# После того как список точек для перекраски будет готов, скрипт создаёт копию двумерного массива,
# в котором точки из сформированного списка будут перкрашены.
#
# Опционально новый двумерный массив преобразуется в новый png файл.
#
# Алгоритм обхода соседних пикселов находится здесь.
#
# Алгоритм преобразования из png в массив и обратно можно уточнить у Стаса.


from numpy import asarray
from PIL import Image

img = Image.open("image.png")
array_of_pixels = asarray(img)

RED = [255, 0, 0]
start_point = (0, 0)


# list<pixels> pixels_in_component;
# stack<pixels> neighbours;
# neighbours.add(starting_point)
#
# while not neighbours.empty:
#    p = neighbours.pop();
#    pixels_in_component.append(p)
#    for each adjacent pixel n of p:
#      if color(n) == color(starting_point):
#          neighbours.append(n)

pixels_in_component = []
neighbours = [start_point]

while neighbours:
    p = neighbours.pop()
    pixels_in_component.append(p)
    for x in range(len(array_of_pixels)):
        for y in range(len(array_of_pixels[x])):
            if array_of_pixels[x + 1][y] == array_of_pixels[x][y] and array_of_pixels[x][y + 1] == array_of_pixels[x][
                y]:
                neighbours.append((x, y))

new_array_of_pixels = list(array_of_pixels)

for coord in neighbours:
    new_array_of_pixels[coord[0]][coord[1]] = RED

changed_image = Image.fromarray(new_array_of_pixels)
changed_image.show()
