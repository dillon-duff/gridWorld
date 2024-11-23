from blocks import MoverBlock, ConsumerBlock, RotatorBlock, EyeBlock

color_map = {
    3: {
        "name": "mover",
        "color": "green",
        "rgb": (0, 255, 0),
        "block_class": MoverBlock
    },
    1: {
        "name": "consumer",
        "color": "red",
        "rgb": (255, 0, 0),
        "block_class": ConsumerBlock
    },
    4: {
        "name": "rotator",
        "color": "blue",
        "rgb": (0, 0, 255),
        "block_class": RotatorBlock
    },
    2: {
        "name": "eye",
        "color": "yellow",
        "rgb": (255, 255, 0),
        "block_class": EyeBlock
    },
}

WIDTH = 1200
HEIGHT = 800