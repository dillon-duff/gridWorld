# Evolution Simulator of Beings

Every Being is composed of blocks.

Every block is a certain color and has a certain function

## Block Colors

### Green
- Move forward (moves the entire body in a direction)
- Controlled by brain

### Red
- Consumer
- Controlled by brain

### Blue
- Rotator (local rotation, forcing a NxN area to be full of blocks to rotate)
- Controlled by brain

### Gray
- Shield (weighs more than neutral but otherwise functionally identical)

### Brown
- Neutral

### Yellow
- Eye (sensor)
- Sees a square of blocks, where the eye is one of the square's corners. So it can have 4 directions.
- Always on

### Orange
- Reproducer

### Purple
- Ear (sensor)
- Hears a cone of blocks, where the ear is one of the cone's corners. So it can have 4 directions.
- Always on

### Pink
- Communicator
- Emits a sound in a cone of blocks, where the communicator is one of the cone's corners. So it can have 4 directions.

Blocks eat food to survive.

Foods are composed of blocks.

Foods are consumed with the consumer blocks and the number of consumer blocks must be greater than or equal to the number of food blocks.

Each Being has a brain that controls the blocks.

Each brain has a number of neurons whose inputs are the outputs of the sensor blocks.

The brain outputs the control signals to the blocks.

The blocks act in order according to their color.

This order is not fixed.

Each block consumes energy to act.

The energy consumed can be different for the same action depending on what blocks the action is performed on (costs more to rotate shield than neutral).

Foods come in may forms

## Food Types

## Seeds
- Low energy, but can grow into a plant with higher energy value

## Flowers
- Medium energy, but periodically produce seeds

## Fruit
- High energy
- Decays over time

## Leaves
- Very low energy
- Regrows relatively quickly

# Life Cycle


Random instantiation for each Being as a random 3x3 grid of blocks.

Food randomly spawns on the grid

If two Beings meet, they can reproduce if they are touching and both activate their reproducer blocks.

Brains are instantiated as networks with a neuron for each sensor, and outputs for each block that can perform an action.

