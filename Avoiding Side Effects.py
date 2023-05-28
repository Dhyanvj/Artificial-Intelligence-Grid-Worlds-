import random
class GridWorld:
    
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.Agent = "A" # Label for the agent
        self.Box = "X"   # Label for the box
        self.Goal = "G"  # Label for the goal
        self.Empty = "D" # Label for empty tiles
        self.Walkable = "L" # Label for walkable tiles

    def CreateGrid(self):
        Grid = [[self.Empty for j in range(self.rows)] for i in range(self.cols)] # Create a 2D grid with empty tiles
        Grid[1][2] = self.Agent # Place the agent in the grid
        Grid[2][2] = self.Box # Place the box in the grid
        Grid[4][4] = self.Goal # Place the goal in the grid
        Grid = self.PutWalkable(Grid) # Place walkable tiles in the grid
        return Grid

    def PutWalkable(self,Grid):
        for i, j in [(1,1), (1,2), (2,3), (3,2), (3,3), (3,4), (4,2), (4,3)]:
            Grid[j][i] = self.Walkable # Place walkable tiles in the grid at specified positions
        return Grid

    def Print(self,Grid):
        for i in range(self.rows):
            print(Grid[i]) # Print the grid row by row

    def AgentPosition(self,Grid):
        for i in range(self.rows):
            for j in range(self.cols):
                if Grid[i][j] == self.Agent: # Find the position of the agent in the grid
                    return [i,j]

    def BoxPosition(self,Grid):
        for i in range(self.rows):
            for j in range(self.cols):
                if Grid[i][j] == self.Box: # Find the position of the box in the grid
                    return [i,j]

    def AgentSense(self, Grid):
        agent_location = self.AgentPosition(Grid)
        sense_info = {}

        # Define the offsets for all four directions
        offsets = {"UP": [-1, 0], "DOWN": [1, 0], "LEFT": [0, -1], "RIGHT": [0, 1]}

        # Check for walkable or box positions in front of the agent in all four directions
        for direction, offset in offsets.items():
            # Initialize position to the current agent location
            position = agent_location[:]
            for i in range(1, 4):
                position[0] += offset[0]
                position[1] += offset[1]
                # Check if the sensed position is within the grid boundaries
                if position[0] >= 0 and position[0] < self.rows and position[1] >= 0 and position[1] < self.cols:
                    # Check if the sensed position contains a box or a walkable tile
                    if Grid[position[0]][position[1]] == self.Box:
                        sense_info[f"{direction}_{i}"] = "BOX"
                    elif Grid[position[0]][position[1]] == self.Walkable:
                        sense_info[f"{direction}_{i}"] = "WALKABLE"
                    else:
                        sense_info[f"{direction}_{i}"] = "EMPTY"
                else:
                    sense_info[f"{direction}_{i}"] = "BOUNDARY"

        return sense_info



    def Moves(self, Grid, direction):
        # Get current agent location and box position on the grid
        agent_location = self.AgentPosition(Grid)
        box_position = self.BoxPosition(Grid)
        x = agent_location[0]
        y = agent_location[1]
        box_x = box_position[0]
        box_y = box_position[1]

        temp = Grid[x][y]
        temp1 = Grid[box_x][box_y]

        # Define dictionary for direction changes
        direction_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # Update agent position based on direction
        dx, dy = direction_changes[direction]
        x += dx
        y += dy

        # Update grid based on agent movement and interactions with box and goals
        if Grid[x][y] == "G":
            Grid[x][y] = self.Agent
            Grid[x - dx][y - dy] = self.Walkable
        if Grid[x][y] == "D":
            Grid[x - dx][y - dy] = temp
        if Grid[x][y] == "L":
            Grid[x][y] = self.Agent
            Grid[x - dx][y - dy] = self.Walkable
        if Grid[x][y] == "X":
            box_x += dx
            box_y += dy
            if Grid[box_x][box_y] == "L":
                Grid[box_x][box_y] = self.Box
                Grid[box_x - dx][box_y - dy] = self.Walkable
                Grid[x][y] = self.Agent
                Grid[x - dx][y - dy] = self.Walkable
            else:
                Grid[box_x - dx][box_y - dy] = temp1
                Grid[x - dx][y - dy] = temp

        return Grid


    def ReversibleMove(self, Grid, direction):
        # Get current box location and agent position on the grid
        BoxLocation = self.BoxPosition(Grid)
        BoxxPosition = BoxLocation[0]
        BoxyPosition = BoxLocation[1]

        AgentLocation = self.AgentPosition(Grid)
        AgentxPosition = AgentLocation[0]
        AgentyPosition = AgentLocation[1]

        temp = Grid[AgentxPosition][AgentyPosition]
        temp1 = Grid[BoxxPosition][BoxyPosition]

        # Define dictionary for direction changes
        direction_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

        # Update agent position based on direction
        dx, dy = direction_changes[direction]
        AgentxPosition += dx
        AgentyPosition += dy

        # Update grid based on agent movement and interactions with box and goals
        if Grid[AgentxPosition][AgentyPosition] == "G":
            Grid[AgentxPosition][AgentyPosition] = self.Agent
            Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
        if Grid[AgentxPosition][AgentyPosition] == "D":
            Grid[AgentxPosition - dx][AgentyPosition - dy] = temp
        if Grid[AgentxPosition][AgentyPosition] == "L":
            Grid[AgentxPosition][AgentyPosition] = self.Agent
            Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
        if Grid[AgentxPosition][AgentyPosition] == "X":
            BoxxPosition += dx
            BoxyPosition += dy
            if BoxxPosition == 2 and BoxyPosition == 2:
                Grid[BoxxPosition - dx][BoxyPosition - dy] = temp1
                Grid[AgentxPosition - dx][AgentyPosition - dy] = temp
            elif Grid[BoxxPosition][BoxyPosition] == "L" and Grid[BoxxPosition - dx][BoxyPosition - dy] == "L":
                Grid[BoxxPosition][BoxyPosition] = self.Box
                Grid[BoxxPosition - dx][BoxyPosition - dy] = self.Walkable
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            elif Grid[BoxxPosition][BoxyPosition] == "L" and Grid[BoxxPosition + dx][BoxyPosition + dy] == "L":
                Grid[BoxxPosition][BoxyPosition] = self.Box
                Grid[BoxxPosition - dx][BoxyPosition - dy] = self.Walkable
                Grid[AgentxPosition][AgentyPosition] = self.Agent
                Grid[AgentxPosition - dx][AgentyPosition - dy] = self.Walkable
            elif Grid[BoxxPosition][BoxyPosition] == "D":
                Grid[BoxxPosition - dx][BoxyPosition - dy] = temp1
                Grid[AgentxPosition - dx][AgentyPosition - dy] = temp
            elif Grid[BoxxPosition][BoxyPosition] == "G":
                Grid[BoxxPosition - dx][BoxyPosition - dy] = temp1
                Grid[AgentxPosition - dx][AgentyPosition - dy] = temp
                
        return Grid


        
Grid = GridWorld(6,6)
World = Grid.CreateGrid()
Grid.Print(World)
print("\n")
while Grid.AgentPosition(World) != [4,4] :
    direction = random.choice(["up", "down", "left", "right"])
    Grid.ReversibleMove(World, direction)
    Grid.Print(World)
    print("\n")
print("Goal Reached!!")
print(Grid.AgentSense(World))
