from image import Image
from point import Point
from ray import Ray
from colour import Colour


class RenderEngine:
    """Renders 3D objects into 2D objects using ray tracing"""

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = +1.0 / aspect_ratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j * ystep
            for i in range(width):
                x = x0 + i * xstep
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
            print("{:3.0f}%".format(float(j) / float(height) * 100))
        return pixels

    def colour_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material
        obj_colour = material.colour_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        colour = material.ambient * Colour.from_hex("#000000")
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Diffuse shading (Lambert)
            colour += (
                    obj_colour
                    * material.diffuse
                    * max(normal.dot_product(to_light.direction), 0)
            )
            # Specular shading
            half_vector = (to_light.direction + to_cam).normalise()
            colour += (
                    light.colour
                    * material.specular
                    * max(normal.dot_product(half_vector), 0) ** specular_k
            )
        return colour

    def ray_trace(self, ray, scene):
        colour = Colour(0, 0, 0)
        # Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return colour
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        colour += self.colour_at(obj_hit, hit_pos, hit_normal, scene)
        return colour

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return dist_min, obj_hit



