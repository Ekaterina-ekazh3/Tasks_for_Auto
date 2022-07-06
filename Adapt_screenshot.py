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

array_of_coords = []
neighbours = [start_point]

while neighbours:
    p = neighbours.pop()
    array_of_coords.append(p)

    n1 = (p[0] + 1, p[1])  # сосед по вертикали
    n2 = (p[0], p[1] + 1)  # сосед по горизонтали

    if n1[0] < len(array_of_pixels):
        if list(array_of_pixels[n1[0]][n1[1]]) == list(array_of_pixels[p[0]][p[1]]):
            neighbours.append(n1)
    if n2[1] < len(array_of_pixels[0]):
        if list(array_of_pixels[n2[0]][n2[1]]) == list(array_of_pixels[p[0]][p[1]]):
            neighbours.append(n2)

new_array_of_pixels = array_of_pixels.copy()

for coord in array_of_coords:
    new_array_of_pixels[coord[0]][coord[1]] = RED

changed_image = Image.fromarray(new_array_of_pixels)
changed_image.show()
