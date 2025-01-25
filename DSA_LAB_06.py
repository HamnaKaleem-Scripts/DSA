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
        move=[(0,1),(1,0),(-1,0),(0,-1)]
        for i in move:
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
    return 'unsolved',stack
                
            

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

