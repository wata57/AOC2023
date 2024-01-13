import time
from collections import deque
import math

start_time = time.time()

class Exer08:
    def __init__(self):
        self.navigation_map = {}
        self.navigation_instructions = []

    def add_location(self, location, left_choice, right_choice):
        self.navigation_map[location] = (left_choice, right_choice)

    def load_data(self, navigation_data):
        instructions, location_data = navigation_data.strip().split("\n\n")
        self.navigation_instructions = [
            0 if direction == 'L' else 1 for direction in instructions
        ]
        for data in location_data.split("\n"):
            location, choices = data.split(" = ")
            left, right = choices.strip("()").split(", ")
            self.add_location(location, left, right)

    def navigate_desert_ghosts(self):
        start_nodes = [node for node in self.navigation_map if node.endswith('A')]
        first_z_steps = [-1] * len(start_nodes)
        cycle_lengths = [0] * len(start_nodes)
        current_nodes = start_nodes.copy()
        steps = 0

        while any(cycle_length == 0 for cycle_length in cycle_lengths):
            direction = self.navigation_instructions[steps % len(self.navigation_instructions)]
            steps += 1

            for i, node in enumerate(current_nodes):
                if node.endswith('Z'):
                    if first_z_steps[i] == -1:
                        first_z_steps[i] = steps
                    else:
                        if cycle_lengths[i] == 0:
                            cycle_lengths[i] = steps - first_z_steps[i]

                current_nodes[i] = self.navigation_map[node][direction]
        return math.lcm(*cycle_lengths)

with open('input.txt', 'r') as navigation_data:
    ex_instance = Exer08()
    ex_instance.load_data(navigation_data.read())
    print(ex_instance.navigate_desert_ghosts())

end_time = time.time()

total_time = end_time - start_time

print(f"run time = {total_time}")