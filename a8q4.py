with open("Maze3.txt", "r") as f:
    lines = f.readlines()
    
    array = [line.split() for line in lines]
    
# example = [line.split() for line in
#            ['0 0 0 0 0 1 0 0', '1 0 1 1 0 0 0 0', '1 0 0 1 0 1 0 1', '0 1 0 0 0 1 0 0', '0 0 0 0 1 1 0 1',
#             '0 0 1 0 0 0 0 0']]

path = []
allowed_moves = [(0,0), (1, 0),(0, 1), (0, -1), (-1, 0)]
'''
allowed moves: 0,1 when you add 1 to the column, you move right
                0,-1 move left
                1,0 when you add one to the row you move down
                -1,0 move up
'''
visited = []


def solve_maze(m, s, g):
    
    if (s[0] == g[0]) and (s[1] == g[1]):
        
        for i in range(len(m)):           
            print(m[i])
            for j in range(len(m[0])): # fill the visited cells tuple by checking whether the value of the current cell  is "P"
                if m[i][j] == "P":
                    visited.append((i,j))
        print("The path from start to goal is:")    
        print(visited)
        
        return
    else:
        for i in range(len(allowed_moves)):  # iterate through all movements
            new = (s[0] + allowed_moves[i][0], s[1] + allowed_moves[i][1])
            
            if (new[0] >= 0) and (new[0] < len(m)) and (new[1] >= 0) and (new[1] < len(m[0])) and (
                    (m[new[0]][new[1]]) == '0') and (new not in visited):
                
                m[new[0]][new[1]] = 'P'
                

                solve_maze(m, new, g)
            elif new in visited:
                continue




