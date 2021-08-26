#include <stdio.h>
#include <stdlib.h>

int main()
{
    int X, Y;
    scanf("%d %d", &X, &Y);
    for(int val = X; val <= Y; val++)
    {
        int temp = val;
        while(temp > 0)
        {
            if(temp%2)
                break;
            temp/=10;
        } // end of while loop
        if(temp != 0)
        {
            printf("%d ", val);
        } // end of if condition
    } // end of for loop
    return 0;
} // end of main function