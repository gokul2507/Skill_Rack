#include <stdio.h>
#include <math.h>

typedef struct point
{
    int X;
    int Y;
} Point;

int main()
{
    Point P1, P2, P3;
    scanf("%d %d\n", &P1.X, &P1.Y);
    scanf("%d %d", &P2.X, &P2.Y);
    printf("%d", getRectangleArea(&P1, &P2));
    return 0;
}
