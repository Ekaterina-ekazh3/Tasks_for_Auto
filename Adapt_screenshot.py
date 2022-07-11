# Требуется скрипт, который мог бы перекрашивать пикселы скриншота формы, лежащие вне замкнутых контуров,
# ограничивающих контролы, расположенные на этой форме.


from numpy import asarray
from numpy import in1d
from PIL import Image

img = Image.open("time.png").convert('RGB')
array_of_pixels = asarray(img)
# print(array_of_pixels)
RED = [255, 0, 0]
start_point = (0, 0)

array_of_coords = []
neighbours = [start_point]

# row_from_array = array_of_pixels[1]
# # print(row_from_array)
# neighbours_colors = []
# for nc in row_from_array[:3]:
#     if not in1d(nc, neighbours_colors).any():
#         neighbours_colors.append(list(nc))
#         print(nc)
# print(neighbours_colors)

while neighbours:
    p = neighbours.pop()
    array_of_coords.append(p)

    n1 = (p[0] + 1, p[1])  # сосед по вертикали
    n2 = (p[0], p[1] + 1)  # сосед по горизонтали

    if n1[0] < len(array_of_pixels):
        if list(array_of_pixels[n1[0]][n1[1]]) == list(array_of_pixels[p[0]][p[1]]):
            if n1 not in array_of_coords:
                neighbours.append(n1)
    if n2[1] < len(array_of_pixels[0]):
        if list(array_of_pixels[n2[0]][n2[1]]) == list(array_of_pixels[p[0]][p[1]]):
            if n2 not in array_of_coords:
                neighbours.append(n2)
# print(array_of_coords)

# start_point_alter = (len(array_of_pixels) - 1, len(array_of_pixels[0] - 1))

new_array_of_pixels = array_of_pixels.copy()

for coord in array_of_coords:
    new_array_of_pixels[coord[0]][coord[1]] = RED
# print(new_array_of_pixels)
changed_image = Image.fromarray(new_array_of_pixels)
changed_image.show()
