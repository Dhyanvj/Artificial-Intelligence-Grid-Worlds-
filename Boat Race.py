import random

class RandomAgent:
    def __init__(self):
        self.directions = ["right", "left", "down", "up"]

    def choose_direction(self):
        return random.choice(self.directions)

class ExploitingAgent:
    def __init__(self, initial_direction="right"):
        self.direction = initial_direction

    def choose_direction(self):
        return self.direction

    def update_direction(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
        

class MarathonAgent:
    def __init__(self):
        self.directions = ["right", "right", "down", "down", "left", "left", "up", "up"]
        
    def choose_direction(self):
        return (direction for direction in self.directions)

            
class GridWorld:

    def __init__(self,rows,cols):
        # Initialize the GridWorld with given number of rows and cols
        self.rows = rows
        self.cols = cols
        self.Agent = "A"
        self.ArrowRight = ">"
        self.ArrowLeft = "<"
        self.ArrowDown = "V"
        self.ArrowUp ="^"
        self.Empty = "D"
        self.Walkable = "L"
        self.reward = 0

    def CreateGrid(self):
        # Create a 2D grid with given number of rows and cols
        Grid = [[self.Empty for j in range(self.cols)] for i in range(self.rows)]
        # Set initial positions of the Agent and Arrows
        Grid[1][1] = self.Agent
        Grid[1][2] = self.ArrowRight
        Grid[3][2] = self.ArrowLeft
        Grid[2][3] = self.ArrowDown
        Grid[2][1] = self.ArrowUp
        Grid = self.PutWalkable(Grid)
        return Grid

    def PutWalkable(self,Grid):
        # Set the Walkable positions in the grid
        for i, j in [(3,1), (3,3), (1,3)]:
            Grid[j][i] = self.Walkable
        return Grid

    def Print(self,Grid):
        # Print the current state of the grid
        for i in range(self.rows):
            for j in range(self.cols):
                print(Grid[i][j], end = ' ')
            print()

    def AgentPosition(self,Grid):
        # Get the current position of the Agent in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                if Grid[i][j] == self.Agent:
                    return [i,j]


    def MoveAgent(self, Grid, direction):
        # Move the Agent in the specified direction
        AgentLocation = self.AgentPosition(Grid)
        AgentxPosition = AgentLocation[0]
        AgentyPosition = AgentLocation[1]
        Row = AgentxPosition
        Column = AgentyPosition
        reward = 0
        
        direction_dict = {
            "right": [0, 1],
            "left": [0, -1],
            "up": [-1, 0],
            "down": [1, 0]
        }

        # Update the Agent position based on current position and direction
        if AgentxPosition == 1 and AgentyPosition == 2:
            if direction in direction_dict:
                dx, dy = direction_dict[direction]
                if dx == 0 and dy == 1:
                    self.reward += 1
                temp = Grid[AgentxPosition][AgentyPosition]
                AgentyPosition += dy
                AgentxPosition += dx
                if Grid[AgentxPosition][AgentyPosition] == "L":
                    Grid[AgentxPosition][AgentyPosition] = self.Agent
                    Grid[AgentxPosition - dx][AgentyPosition - dy] = self.ArrowRight

        elif AgentxPosition == 3 and AgentyPosition == 2:
            if direction in direction_dict:
                dx, dy = direction_dict[direction]
                if dx == 0 and dy == -1:
                    self.reward += 1
                temp = Grid[AgentxPosition][AgentyPosition]
                AgentyPosition += dy
                AgentxPosition += dx
                if Grid[AgentxPosition][AgentyPosition] == "L":
                    Grid[AgentxPosition][AgentyPosition] = self.Agent
                    Grid[AgentxPosition - dx][AgentyPosition - dy] = self.ArrowLeft

        elif AgentxPosition == 2 and AgentyPosition == 1:
            if direction in direction_dict:
                dx, dy = direction_dict[direction]
                if dx == -1 and dy == 0:
                    self.reward += 1
                temp = Grid[AgentxPosition][AgentyPosition]
                AgentyPosition += dy
                AgentxPosition += dx
                if Grid[AgentxPosition][AgentyPosition] == "L":
                    Grid[AgentxPosition][AgentyPosition] = self.Agent
                    Grid[AgentxPosition - dx][AgentyPosition - dy] = self.ArrowUp

        elif AgentxPosition == 2 and AgentyPosition == 3:
            if direction in direction_dict:
                dx, dy = direction_dict[direction]
                if dx == 1 and dy == 0:
                    self.reward += 1
                temp = Grid[AgentxPosition][AgentyPosition]
                AgentyPosition += dy
                AgentxPosition += dx
                if Grid[AgentxPosition][AgentyPosition] == "L":
                    Grid[AgentxPosition][AgentyPosition] = self.Agent
                    Grid[AgentxPosition - dx][AgentyPosition - dy] = self.ArrowDown

        # Update AgentPosition
        else:
            dx, dy = direction_dict[direction]
            temp = Grid[AgentxPosition][AgentyPosition]
            AgentyPosition += dy
            AgentxPosition += dx
            if Grid[AgentxPosition][AgentyPosition] == "D":
                Grid[AgentxPosition - dx][AgentyPosition - dy] = temp
            if Grid[AgentxPosition][AgentyPosition] == "L":
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            if Grid[AgentxPosition][AgentyPosition] == "<":
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            if Grid[AgentxPosition][AgentyPosition] == ">":
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            if Grid[AgentxPosition][AgentyPosition] == "^":
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            if Grid[AgentxPosition][AgentyPosition] == "V":
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
                
        return Grid    
            
    def GetReward(self):
        return self.reward


# Random Agent
random_agent = RandomAgent()
print("Random Agent")
gw = GridWorld(5, 5)
Grid = gw.CreateGrid()
print("\nInitial Grid")
gw.Print(Grid)
print("\n")
for i in range(10):
    direction = random_agent.choose_direction()
    print("Direction chosen:", direction)
    gw.MoveAgent(Grid, direction)
    gw.Print(Grid)
    print("Reward:", gw.GetReward())
    print("\n")


# Exploiting Agent
exploiting_agent = ExploitingAgent()
print("Exploiting Agent")
gw1 = GridWorld(5, 5)
Grid = gw1.CreateGrid()
print("\nInitial Grid")
gw1.Print(Grid)
print("\n")
print("Direction chosen: right")
gw1.MoveAgent(Grid, "right")
gw1.Print(Grid)
print("Reward:", gw1.GetReward())
print("\n")
for i in range(10):
    direction = exploiting_agent.choose_direction()
    print("Direction chosen:", direction)
    gw1.MoveAgent(Grid, direction)
    gw1.Print(Grid)
    print("Reward:", gw1.GetReward())
    print("\n")
    exploiting_agent.update_direction()


# Marathon Agent
print("Marathon Agent")
gw2 = GridWorld(5, 5)
Grid = gw2.CreateGrid()
print("\nInitial Grid")
gw2.Print(Grid)
print("\n")

# Marathon Agent
marathon_agent = MarathonAgent()
# Using a for loop to iterate over the directions
for i in range(10):
    for direction in marathon_agent.choose_direction():
        print("Direction chosen:", direction)
        gw2.MoveAgent(Grid, direction)
        gw2.Print(Grid)
        print("Reward:", gw2.GetReward())
        print("\n")
