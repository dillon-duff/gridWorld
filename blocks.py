from being import Being

class MoverBlock:
    def __init__(self, orientation=0):
        self.orientation = orientation

    def update_being(self, being: Being):
        pass

class ConsumerBlock:
    def __init__(self):
        pass

    def update_being(self, being: Being):
        pass


class RotatorBlock:
    def __init__(self, orientation=0):
        self.orientation = orientation

    def update_being(self, being: Being):
        pass

class ShieldBlock:
    def __init__(self):
        pass

    def update_being(self, being: Being):
        pass

class NeutralBlock:
    def __init__(self):
        pass

    def update_being(self, being: Being):
        pass

class EyeBlock:
    def __init__(self, orientation=0):
        self.orientation = orientation

    def update_being(self, being: Being):
        pass


class ReproducerBlock:
    def __init__(self):
        pass

    def update_being(self, being: Being):
        pass

class EarBlock:
    def __init__(self, orientation=0):
        self.orientation = orientation

    def update_being(self, being: Being):
        pass

class CommunicatorBlock:
    def __init__(self, orientation=0):
        self.orientation = orientation

    def update_being(self, being: Being):
        pass

