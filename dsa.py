# def solve_maze(maze):
#     def is_valid_move(row, col):
#         return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (maze[row][col] == " " or maze[row][col] == "T")

#     def dfs(row, col, path):
#         if not is_valid_move(row, col):
#             return False
        
#         if maze[row][col] == "T":
#             return True
        
#         # Mark the current cell as visited
#         maze[row][col] = "."
        
#         # Try moving in all four directions
#         for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             if dfs(row + dr, col + dc, path + [(row + dr, col + dc)]):
#                 return True
        
#         # If no path found, backtrack
#         maze[row][col] = " "
#         return False

#     # Find the starting position
#     start_row, start_col = -1, -1
#     for i in range(len(maze)):
#         for j in range(len(maze[0])):
#             if maze[i][j] == "P":
#                 start_row, start_col = i, j
#                 break
#         if start_row != -1:
#             break
    
#     if start_row == -1:
#         return "Unsolved", []
    
#     path = [(start_row, start_col)]
#     if dfs(start_row, start_col, path):
#         return "Solved", path
#     else:
#         return "Unsolved", []

# # Driver
# maze1 = [
#     [" ", "*", " ", "*", " ", " "],
#     [" ", "*", " ", "*", " ", " "],
#     ["P", " ", " ", " ", "*", " "],
#     ["*", " ", "*", "*", "*", " "],
#     [" ", " ", " ", " ", "*", "T"],
#     ["*", " ", " ", " ", " ", " "]
# ]
# status, path = solve_maze(maze1)
# print(status)
# if status == "Solved":
#     print("Path:", path)

# maze2 = [
#     [" ", "*", " ", "*", " ", " "],
#     [" ", "*", " ", "*", " ", " "],
#     ["P", " ", " ", " ", "*", " "],
#     ["*", " ", "*", "*", "*", " "],
#     [" ", " ", " ", " ", "*", "T"],
#     ["*", " ", " ", " ", " ", "*"]
# ]
# status, path = solve_maze(maze2)
# print(status)
# if status == "Solved":
#     print("Path:", path)





#_____________________________
'copilot'
# def solve_maze(maze):
#     def dfs(x, y, path):
#         if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == "*":
#             return False
#         if maze[x][y] == "T":
#             path.append((x, y))
#             return True

#         maze[x][y] = "*"  # Mark as visited
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         for dx, dy in directions:
#             if dfs(x + dx, y + dy, path):
#                 path.append((x, y))
#                 return True

#         return False

#     start_x, start_y = None, None
#     for i in range(len(maze)):
#         for j in range(len(maze[0])):
#             if maze[i][j] == "P":
#                 start_x, start_y = i, j
#                 break

#     if start_x is None or start_y is None:
#         return "Unsolved", []

#     path = []
#     if dfs(start_x, start_y, path):
#         path.reverse()
#         return "Solved", path
#     else:
#         return "Unsolved", []


def solve_maze(maze):
    for i in range(len(maze)):
        for j in range(len (maze[0])):
            if maze[i][j]=='P':
                s_x,s_y=i,j
                break
    stack=[(s_x,s_y)]
    
    while stack:
        next=0
        x,y=stack[-1]
        if maze[x][y]=='T':
            return 'Solved',stack
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        
        for i in direction:
            x1=x+i[0]
            y1=y+i[1]
            if x1 in range(len(maze)) and y1 in range(len(maze[0])) and maze[x1][y1] != '*' and maze[x1][y1] != '%':
                stack.append((x1,y1))
                maze[x][y]='%'
                next=1
                break
        if next==0:
            stack.pop()
            maze[x][y] = '%'
    return 'unsolved',[]
                
            

# Driver
maze1 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
]

maze2 = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", "*"]
]

status1, path1 = solve_maze(maze1)
print(status1)
if status1 == "Solved":
    print("Path:", path1)

status2, path2 = solve_maze(maze2)
print(status2)
if status2 == "Solved":
    print("Path:", path2)
