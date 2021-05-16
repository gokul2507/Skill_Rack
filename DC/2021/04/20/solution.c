int uni(int n){
    while (n>9){ n/=10;}
    return n;
}
boundedArray* getIntegersStartingWithD(int SIZE, int arr[], int D)
{
    boundedArray *l=malloc(sizeof(boundedArray));
    l->SIZE=0;
    l->arr=malloc(SIZE*sizeof(int*));
    for(int i=0;i<SIZE;i++) if(uni(arr[i])==D) l->arr[l->SIZE++]=arr[i];
    if(l->SIZE==0){ l->SIZE=1; l->arr[0]=-1;}
    return l;
}
