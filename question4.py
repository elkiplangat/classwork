
def solve_maze(m,s,g):

    if not m:
        return
    elif s == g:
        print(f"Youre done! you're at: {s}")
        return
    else:
        print(f"S: {s}")
        #print(m[s[0]][s[1]])
        if m[s[0]][s[1]] == '0':
            print("Yaaay!")
            print(f"fucking {m}")
            east = (s[0], s[1] + 1)
            s = east
            solve_maze(m,s,g)
            # south = (s[0]-1, s[1])
            # north = (s[0]+1, s[1])
            # west = (s[0], s[1]-1)
            # east = (s[0], s[1]+1)
            # print(f"bottom : {south}")
            # print(f"north : {north}")
            # print(f"west : {west}")
            # print(f"right : {east}")

        else:
            print("No through way")


        #return
    ...

with open("Maze1.txt", "r") as f:
    lines = f.readlines()
    #print(lines)
    array = [line.split() for line in lines]
    #print(array[1][1])
    #solve_maze(array,(0,0), ())
example = [line.split() for line in ['0 0 0 0 0 1 0 0', '1 0 1 1 0 0 0 0', '1 0 0 1 0 1 0 1', '0 1 0 0 0 1 0 0', '0 0 0 0 1 1 0 1','0 0 1 0 0 0 0 0' ]]
solve_maze(example, (0,0), (5,7))