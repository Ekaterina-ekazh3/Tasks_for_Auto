# Требуется скрипт, который мог бы перекрашивать пикселы скриншота формы, лежащие вне замкнутых контуров,
# ограничивающих контролы, расположенные на этой форме.


from numpy import asarray
from PIL import Image
from numba import jit

img = Image.open("time.png").convert('RGB')
array_of_pixels = asarray(img)

RED = [255, 0, 0]
start_point = (0, 0)

@jit
def define_coords(start_pnt):
    neighbours = [start_pnt]
    arr_of_coords = []

    while neighbours:
        p = neighbours.pop()
        arr_of_coords.append(p)

        n1 = (p[0] + 1, p[1])  # сосед по вертикали
        n2 = (p[0], p[1] + 1)  # сосед по горизонтали

        if n1[0] < len(array_of_pixels):
            if list(array_of_pixels[n1[0]][n1[1]]) == list(array_of_pixels[p[0]][p[1]]):
                if n1 not in arr_of_coords:
                    neighbours.append(n1)
        if n2[1] < len(array_of_pixels[0]):
            if list(array_of_pixels[n2[0]][n2[1]]) == list(array_of_pixels[p[0]][p[1]]):
                if n2 not in arr_of_coords:
                    neighbours.append(n2)
    return arr_of_coords


array_of_coords = define_coords(start_point)

new_array_of_pixels = array_of_pixels.copy()

for coord in array_of_coords:
    new_array_of_pixels[coord[0]][coord[1]] = RED

changed_image = Image.fromarray(new_array_of_pixels)
changed_image.show()
