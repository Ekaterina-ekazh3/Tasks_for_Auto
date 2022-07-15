# Требуется скрипт, который мог бы перекрашивать пикселы скриншота формы, лежащие вне замкнутых контуров,
# ограничивающих контролы, расположенные на этой форме.


from numpy import asarray
from numpy import array_equal
from numpy import ndarray
from PIL import Image

img = Image.open("time.png").convert('RGB')
array_of_pixels = asarray(img)

RED = [255, 0, 0]
start_point = (0, 0)


def find_neighbours(neigh: list, arr_of_co: set) -> set:
    while neigh:
        p = neigh.pop()
        arr_of_co.add(p)

        neigh_by_vert = (p[0] + 1, p[1])  # сосед по вертикали
        neigh_by_hor = (p[0], p[1] + 1)  # сосед по горизонтали

        if neigh_by_vert[0] < len(array_of_pixels):
            if array_equal(array_of_pixels[neigh_by_vert[0]][neigh_by_vert[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_by_vert not in arr_of_co:
                    neigh.append(neigh_by_vert)
        if neigh_by_hor[1] < len(array_of_pixels[0]):
            if array_equal(array_of_pixels[neigh_by_hor[0]][neigh_by_hor[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_by_hor not in arr_of_co:
                    neigh.append(neigh_by_hor)
    return arr_of_co


def define_coords(start_pnt):
    neighbours = [start_pnt]
    arr_of_coords = set()
    arr_of_coords = find_neighbours(neighbours, arr_of_coords)
    return arr_of_coords


array_of_coords = define_coords(start_point)

new_array_of_pixels = array_of_pixels.copy()


def set_colour(colour: list, new_arr: ndarray, arr_co: set) -> list:
    inner_array_of_coords = arr_co
    inner_new_array_of_pixels = new_arr
    for coord in inner_array_of_coords:
        inner_new_array_of_pixels[coord[0]][coord[1]] = colour
    return new_array_of_pixels


new_array_of_pixels = set_colour(RED, new_array_of_pixels, array_of_coords)

changed_image = Image.fromarray(new_array_of_pixels)
changed_image.show()
