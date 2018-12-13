from playLA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([3, 4])
    print(vec)
    print(len(vec))
    print(vec[0], vec[1])

    vec2 = Vector([2, 0])
    print(f"{vec}+{vec2}={vec+vec2}")
    print(f"{vec}-{vec2}={vec-vec2}")
    print(f"{vec}*{3}={vec*3}")
    print(Vector.zero(2))
    print(vec.norm())
    print(f'normalize {vec.normalize()}')
    print(f'normalize norm {vec.normalize().norm()}')
