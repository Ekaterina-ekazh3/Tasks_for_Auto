from numpy import asarray, ndarray, array_equal
from PIL import Image

img = Image.open("time.png").convert('RGB')
array_of_pixels = asarray(img)

height, width = array_of_pixels.shape[:-1:]

start_point = (0, 0)

base_color = array_of_pixels[start_point[0]][start_point[1]]
target_color = [255, 0, 0]


def adapt_screenshot(strt_point, trgt_color, check_func):
    neighbours = [strt_point]
    array_of_coords = set()
    check_function = check_func

    while neighbours:
        p = neighbours.pop()
        array_of_coords.add(p)

        neigh_bottom = (p[0] + 1, p[1])  # сосед снизу
        neigh_right = (p[0], p[1] + 1)  # сосед справа
        neigh_top = (p[0] - 1, p[1])  # сосед сверху
        neigh_left = (p[0], p[1] - 1)  # сосед слева

        if neigh_bottom[0] < len(array_of_pixels):
            if check_function(array_of_pixels[neigh_bottom[0]][neigh_bottom[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_bottom not in array_of_coords:
                    neighbours.append(neigh_bottom)
        if neigh_right[1] < len(array_of_pixels[0]):
            if check_function(array_of_pixels[neigh_right[0]][neigh_right[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_right not in array_of_coords:
                    neighbours.append(neigh_right)
        if neigh_top[0] >= 0:
            if check_function(array_of_pixels[neigh_top[0]][neigh_top[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_top not in array_of_coords:
                    neighbours.append(neigh_top)
        if neigh_left[1] >= 0:
            if check_function(array_of_pixels[neigh_left[0]][neigh_left[1]], array_of_pixels[p[0]][p[1]]):
                if neigh_left not in array_of_coords:
                    neighbours.append(neigh_left)

    col_array = array_of_pixels.copy()
    for coord in array_of_coords:
        col_array[coord[0]][coord[1]] = trgt_color

    return col_array


colored_array = adapt_screenshot(start_point, target_color, array_equal)

changed_image = Image.fromarray(colored_array)
changed_image.show()
