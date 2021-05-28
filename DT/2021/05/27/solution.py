R , C = list(map( int , input().split() ))
port = [ ['*' for i in range(C+2)] ]
for i in range(R):
    port.append( ['*'] +  input().split() + ['*'] )
port.append( ['*' for i in range(C+2)] )
#print(port)
minute = 0
port_not_empty = True
while port_not_empty:
    minute += 1
    if minute%2==0:
        for col in range(C+2):
            for row in range(R+1,-1,-1):
                if port[row][col] == '#':
                    if '#' not in port[row][col+1] + port[row][col-1]:
                        port[row][col] = '*'
                        if port[row-1][col] == '#':
                            port[row-1][col] = '*'
                    break
    else:
        for row in range(R+2):
            for col in range(C+1,-1,-1):
                if port[row][col] == '#':
                    if '#' not in port[row-1][col] + port[row+1][col]:
                        port[row][col] = '*'
                        if port[row][col-1] == '#':
                            port[row][col-1] = '*'
                    break
    port_not_empty = False
    for row in port:
        if '#' in row:
            port_not_empty = True
            break
print( minute )  