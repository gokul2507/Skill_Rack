#include <stdlib.h>
#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    for(int ctr = N; ctr >= 1; ctr--)
    {
        printf("%d ",   1 << ctr  );
    }
    return 0;
}
          

