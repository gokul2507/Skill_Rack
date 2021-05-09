char* getCommaSeparatedValues(int SIZE, int arr[])
{
    char *answer=malloc(sizeof(char [101]));
    int t=0;
    for(int i=0;i<SIZE;i++){
        sprintf(answer+t,"%d",arr[i]);
        while(arr[i]){
            t++;
            arr[i]/=10;
        }
        if(i!=SIZE-1)
        *(answer+t++)=',';
    }
    return answer;
}