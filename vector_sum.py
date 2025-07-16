import math

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

# Example usage
n = 8 # Try different values like 3, 5, 10...
vector_sum_2d(n)
vector_sum_3d(n)
