class Ray:
    """ray has origin and normalised directio"""
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalise()