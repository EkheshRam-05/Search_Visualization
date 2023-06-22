# MAZE_FILE = "mazes/square_maze_25x25.txt"
# MAZE_FILE = "mazes/pacman_maze.txt"
# MAZE_FILE = "mazes/modest_maze.txt"
MAZE_FILE = "mazes/diagonal_23x23.txt"
# MAZE_FILE = "mazes/walled_garden_10x10.txt"
# MAZE_FILE = "mazes/walled_garden_20x20.txt"
# MAZE_FILE = "mazes/wide_maze.txt"


Start_Coord = {
    "mazes/square_maze_25x25.txt": (23, 23),
    "mazes/pacman_maze.txt": (13, 14),
    "mazes/modest_maze.txt": (8, 8),
    "mazes/diagonal_23x23.txt": (21, 21),
    "mazes/walled_garden_10x10.txt": (8, 8),
    "mazes/walled_garden_20x20.txt": (18, 18),
    "mazes/wide_maze.txt": (29, 39)
}


offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
            return maze
    except IOError:
        print("There is a problem with the file you have selected.")

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path