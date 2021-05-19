#include<stdio.h>
#include<stdlib.h>
#include <string.h>

int main() {
    int R, C, y, x, i = 0, j, ii, s1, s2, n, c;   scanf("%d%d\n", &R, &C);
    char mat[R][C]; while(scanf("%c ", *mat+i++), i < R * C);
    char s[101];    scanf("%s", s); n = strlen(s);
    int size = 0;
    
    for(i = 1; i * i < n; i++)
        size += n % i == 0;
    int fact[size = 2 * size + (i * i == n)];
    
    for(j = 0, i = 1; i * i <= n; i++)
        if(n % i == 0)
            if(fact[j++] = i, i != n / i)
                fact[j++] = n / i;
    
    for(ii = 0; ii < size; ii++)
        for(s2 = n / (s1 = fact[ii]), y = 0; y <= R-s1; y++)
            for(x = 0; x <= C-s2; x++) {
                for(c = 0, i = y; i < y+s1; i++)
                    for(j = x; j < x+s2; j++)
                        if(mat[i][j] != s[c++])
                            goto next;
                for(i = y; i < y+s1; i += printf("\n"))
                    for(j = x; j < x+s2; printf("%c ", mat[i][j++]));
                return; next:;}}