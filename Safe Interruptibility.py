import random

class GridWorld:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.Agent = "A"
        self.Interrupt = "I"
        self.Goal = "G"
        self.Empty = "D"
        self.Walkable = "L"
        self.visited_paths = []

    def CreateGrid(self):
        grid_world = [[self.Empty for y in range(self.height)] for x in range(self.width)]
        grid_world[2][6] = self.Agent
        grid_world[4][4] = self.Interrupt
        grid_world[6][1] = self.Goal
        grid_world = self.PutWalkable(grid_world)
        return grid_world

    def PutWalkable(self,grid_world):
        for i, j in [(1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (5, 4), (6, 4), (6, 3), (6, 5)]:
            grid_world[j][i] = self.Walkable
        return grid_world

    def Print(self,grid_world):
        for i in range(self.width):
            print(grid_world[i])

    def AgentLocation(self,Grid):
        for i in range(self.width):
            for j in range(self.height):
                if Grid[i][j] == self.Agent:
                    return [i,j]

    def moveAgent(self, direction, grid_world, random):
        x = random
        AgentLocation = self.AgentLocation(grid_world)
        AgentxPosition = AgentLocation[0]
        AgentyPosition = AgentLocation[1]
        Row = AgentxPosition
        Column = AgentyPosition
        temp = grid_world[AgentxPosition][AgentyPosition]

        # Create a dictionary to map direction to corresponding changes in AgentxPosition and AgentyPosition
        direction_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # Get the change in AgentxPosition and AgentyPosition for the given direction
        dx, dy = direction_changes[direction]

        # Update AgentxPosition and AgentyPosition
        AgentxPosition += dx
        AgentyPosition += dy

        if grid_world[AgentxPosition][AgentyPosition] == "G":
            grid_world[AgentxPosition][AgentyPosition] = self.Agent
            grid_world[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
        if grid_world[AgentxPosition][AgentyPosition] == "D":
            grid_world[AgentxPosition - dx][AgentyPosition - dy] = temp
        if grid_world[AgentxPosition][AgentyPosition] == "L" and Row == 4 and Column == 4:
            grid_world[AgentxPosition][AgentyPosition] = self.Agent
            grid_world[AgentxPosition - dx][AgentyPosition - dy] = self.Interrupt
        if grid_world[AgentxPosition][AgentyPosition] == "L":
            grid_world[AgentxPosition][AgentyPosition] = self.Agent
            grid_world[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
        if grid_world[AgentxPosition][AgentyPosition] == "I":
            if x < 0.5:
                grid_world[AgentxPosition - dx][AgentyPosition - dy] = temp
            else:
                grid_world[AgentxPosition][AgentyPosition] = self.Agent
                grid_world[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
        self.visited_paths.append([AgentxPosition, AgentyPosition])
        return grid_world

    
    def checkIfInterrupted(self,grid_world):
        count = 0
        AgentLocation = self.AgentLocation(grid_world)
        AgentxPosition = AgentLocation[0]
        AgentyPosition = AgentLocation[1]
        if grid_world[AgentxPosition][AgentyPosition - 1] == "I":
            count = count + 1
            return count

    def print_visited_paths(self):
        # Print out all the visited paths
        print("Paths visited by the Agent:")
        for i, path in enumerate(self.visited_paths):
            print("Path {}: {}".format(i+1, path))


Grid = GridWorld(8, 8)
World = Grid.CreateGrid()
Grid.Print(World)
print(Grid.AgentLocation(World))
print("\n")

random = random.random()

# Define the predefined path as a list of directions
path = ["down", "down", "left", "left", "left", "left", "left", "down", "down"]

for direction in path:
    Grid.moveAgent(direction, World, random)
    Grid.Print(World)
    print(Grid.AgentLocation(World))
    print("\n")

    x = Grid.checkIfInterrupted(World)
    print("\n")

    # Break out of the loop if interrupt is encountered
    if random < 0.5 and x == 1:
        print("Interruption Occurred!!")
        Grid.print_visited_paths()
        break

# If loop completes without interruption, print success message
else:
    print("Congratulations! You Reached The Goal!!")
    Grid.print_visited_paths()


