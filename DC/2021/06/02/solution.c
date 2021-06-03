#include <stdio.h>
#include <math.h>

typedef struct point
{
    int X;
    int Y;
} Point;
double calculateDistance(Point *p1, Point *p2)
{
    double xd,yd;
    xd=pow((p1->X-p2->X),2);
    yd=pow((p1->Y-p2->Y),2);
    return sqrt(xd+yd);
}
int main()
{
    Point P1, P2, P3;
    scanf("%d %d\n", &P1.X, &P1.Y);
    scanf("%d %d", &P2.X, &P2.Y);
    printf("%.2lf", calculateDistance(&P1, &P2));
    return 0;
}
