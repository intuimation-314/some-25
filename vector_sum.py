import math
import itertools

def vector_sum_2d(n):
    sum_x = 0
    sum_y = 0

    for k in range(n):
        angle = 2 * math.pi * k / n
        sum_x += math.cos(angle)
        sum_y += math.sin(angle)

    print(f"Sum of vectors (x, y): ({round(sum_x,3)}, {round(sum_y,3)})")

def vector_sum_3d(n):
    sum_x = 0
    sum_y = 0
    sum_z = 0

    for p in range( n + 1):  # Includes poles
        phi = math.pi * p / n
        for k in range(n):
            theta = 2 * math.pi * k / n
            x = math.sin(phi) * math.cos(theta)
            y = math.sin(phi) * math.sin(theta)
            z = math.cos(phi)

            sum_x += x
            sum_y += y
            sum_z += z

    print(f"Sum of vectors (x, y, z): ({round(sum_x, 2)}, {round(sum_y, 2)}, {round(sum_z,2)})")

def vector_sum_4d(n):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    sum_w = 0

    for p1 in range(n + 1):  # phi1 from 0 to π
        phi1 = math.pi * p1 / n
        for p2 in range(n + 1):  # phi2 from 0 to π
            phi2 = math.pi * p2 / n
            for k in range(n):  # theta from 0 to 2π
                theta = 2 * math.pi * k / n

                x = math.sin(phi1) * math.sin(phi2) * math.cos(theta)
                y = math.sin(phi1) * math.sin(phi2) * math.sin(theta)
                z = math.sin(phi1) * math.cos(phi2)
                w = math.cos(phi1)

                sum_x += x
                sum_y += y
                sum_z += z
                sum_w += w

    print(f"Sum of vectors (x, y, z, w): ({round(sum_x, 2)}, {round(sum_y, 2)}, {round(sum_z, 2)}, {round(sum_w, 2)})")

def vector_sum_nd(dim, n):
    total = [0.0 for _ in range(dim)]  

    # Create angle values:
    angles_list = []
    for i in range(dim - 2):
        angles_list.append([math.pi * p / n for p in range(n + 1)])  # phi angles (0 to pi)
    angles_list.append([2 * math.pi * k / n for k in range(n)])      # theta (0 to 2pi)

    for angles in itertools.product(*angles_list):
        coords = []
        prod = 1
        for i in range(dim):
            if i < dim - 1:
                angle = angles[i]
                coords.append(prod * math.cos(angle))
                prod *= math.sin(angle)
            else:
                coords.append(prod)  # last dimension

        for i in range(dim):
            total[i] += coords[i]

    # Print rounded result
    rounded = tuple(round(x, 2) for x in total)
    print(f"Sum of vectors in {dim}D: {rounded}")

# Example usage
n = 20 # Try different values like 3, 5, 10...
vector_sum_2d(n)
vector_sum_3d(n)
vector_sum_4d(n)

for i in range(2, 6):
    vector_sum_nd(i, n)