z=list(zip(*list(input().split() for _ in range(9))))
print(sum([int("".join(z[i][:int(j)])) for i,j in enumerate(input().strip())]))