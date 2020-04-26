class Scene:
    """has all the info needed to render an image with the engine"""

    def __init__(self, camera, objects, lights, width, height):
        self.objects = objects
        self.camera = camera
        self.height = height
        self.width = width
        self.lights = lights
