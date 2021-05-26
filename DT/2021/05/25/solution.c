#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

int main() {
    bool map[26] = {false};
    char s[27]; scanf("%s", s);
    int i = 0, ans = 0, j;
    
    while(map[s[i]-'a'] = true, s[++i]);
    for(i = 0; i < 26;) {
        while(i < 26 && !map[i])    i++;
        j = i;
        while(i < 26 && map[i])     i++;
        ans += i - j > 1;}
    printf("%d", ans ? ans : -1);}