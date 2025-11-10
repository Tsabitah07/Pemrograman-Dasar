def static_data():
    def cube_center_of_mass(vertices):
        sum_x, sum_y, sum_z = 0, 0, 0
        for x, y, z in vertices:
            sum_x += x
            sum_y += y
            sum_z += z
        n = len(vertices)
        center = (sum_x / n, sum_y / n, sum_z / n)
        print("Center of mass:", center)
        return center

    cube_vertices = [
        (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
        (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)
    ]
    cube_center_of_mass(cube_vertices)



def input_data_1():
    def cube_center_of_mass(vertices):
        sum_x, sum_y, sum_z = 0, 0, 0
        for x, y, z in vertices:
            sum_x += x
            sum_y += y
            sum_z += z
        n = len(vertices)
        center = (sum_x / n, sum_y / n, sum_z / n)
        print("Center of mass:", center)
        return center

    cube_vertices = []
    for i in range(8):
        x = float(input(f"Enter x for vertex {i + 1}: "))
        y = float(input(f"Enter y for vertex {i + 1}: "))
        z = float(input(f"Enter z for vertex {i + 1}: "))
        cube_vertices.append((x, y, z))

    cube_center_of_mass(cube_vertices)


def input_data_2():
    kubus = {'X': 0, 'Y': 0, 'Z': 0}

    for b in range(1, 9):
        for i in kubus:
            kord = int(input(f'masukkan kooordinat {i} kubus {b} : '))
            kubus[i] += kord

    for a in kubus:
        kubus[a] /= 8
    print(f'Koordinat tengah dari kubus tersebut adalah {kubus}')