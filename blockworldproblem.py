# Define a class BlockWorld to represent a simple block-stacking problem with an initial state of three blocks A, B, and C.
class BlockWorld:
    def __init__(self):
        # Initialize the state with three blocks: 'A', 'B', and 'C'.
        self.state = ['A', 'B', 'C']

    # Create a method move in the class to simulate moving a block from a source location to a destination location if it's a valid move.
    def move(self, source, destination):
        # Check if the source and destination are the same or if the source block doesn't exist in the current state.
        if source == destination or source not in self.state:
            return False

        # Remove the block from the source location and store it in the 'block' variable.
        block = self.state.pop(self.state.index(source))

        # Place the block in the destination location.
        self.state.append(block)

        # Return True to indicate a successful move.
        return True

    # Start solving the problem in the solve method by specifying a sequence of block movements.
    def solve(self):
        # Move block A from source 'A' to destination 'C'.
        self.move('A', 'C')

        # Move block A from source 'A' to destination 'B'.
        self.move('A', 'B')

        # Move block C from source 'C' to destination 'B'.
        self.move('C', 'B')

        # Move block A from source 'A' to destination 'C'.
        self.move('A', 'C')

        # Move block B from source 'B' to destination 'A'.
        self.move('B', 'A')

        # Move block B from source 'B' to destination 'C'.
        self.move('B', 'C')

        # Move block A from source 'A' to destination 'C'.
        self.move('A', 'C')

        # Return the final state of the block arrangement.
        return self.state

# Create an instance of the BlockWorld class.
block_world = BlockWorld()

# Solve the block-stacking problem and store the final state.
final_state = block_world.solve()

# Print the final state of the blocks.
print("Final state:", final_state)
