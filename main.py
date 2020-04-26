# !/usr/bin/env python
from colour import Colour
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from material import Material
from light import Light


def main():
    width = 3200
    height = 2000
    camera = Vector(0, 0, -0.5)
    lights = [Light(Point(0, -0.6, -6), Colour.from_hex("#FFFFFF")),
              Light(Point(5, -0.9, 10), Colour.from_hex("#FFFFFF")),
              Light(Point(-1, -0.9, 10), Colour.from_hex("#FFFFFF"))]
    objects = [Sphere(Point(-0.53, 0, 1), 0.5, Material(Colour.from_hex("#FF0000"))),
               Sphere(Point(0.53, 0, 1), 0.5, Material(Colour.from_hex("#F80000"))),
               Sphere(Point(0, 1000000.5, 1), 1000000, Material(Colour.from_hex("#FFFFFF")))]
    scene = Scene(camera, objects, lights, width, height)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("render.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
