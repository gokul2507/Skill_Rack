void reverseArray(int *arr, int len)
{
    int i=0,j=len-1;
    while(i<j){
        int t=*(arr+i);
        *(arr+i)=*(arr+j);
        *(arr+j)=t;
        i++;
        j--;
    }
}
