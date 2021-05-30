#include <stdio.h>
#include <stdlib.h>
int gettime(char a[]){
    int h=0,m=0;
    for(int i=0;i<5;i++){
        if(i==2)
        continue;
        if(i<2){
            h*=10;
        h+=a[i]-'0';
        }
        if(i>2){
            m*=10;
            m+=a[i]-'0';
        }
    }
    return h*100+m;
}
void printAlarmTimings(char startTime[], char endTime[], int X)
{
    int sth=0,stm=0,eth=0,etm=0,tt;
    tt=gettime(startTime);
    stm=tt%100;
    sth=tt/100;
    tt=gettime(endTime);
    etm=tt%100;
    eth=tt/100;
    while(1){
        stm+=X;
        sth+=stm/60;
        stm%=60;
        if(sth*100+stm>eth*100+etm)
        break;
        printf("%02d:%02d\n",sth,stm);
    }
}
int main()
{
    char startTime[6], endTime[6];
    int X;
    scanf("%s\n%s\n%d", startTime, endTime, &X);
    printAlarmTimings(startTime, endTime, X);
    return 0;
}
