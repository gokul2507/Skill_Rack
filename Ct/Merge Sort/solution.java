private static void merge(int arr[], int left,int m, int right) {
    int i,j,k,n1=m-left+1,n2=right-m,l[]=new int[n1],r[]=new int[n2];
    for(i=0;i<n1;i++)
    l[i]=arr[left+i];
    for(j=0;j<n2;j++)
    r[j]=arr[m+1+j];
    i=0;
    j=0;
    k=left;
    while(i<n1 && j<n2)
        if(l[i]<=r[j])
            arr[k++]=l[i++];
        else
            arr[k++]=r[j++];
    while(i<n1)
    arr[k++]=l[i++];
    while(j<n2)
    arr[k++]=r[j++];
}
private static void mergeSort(int arr[],int l,int r){
    if(l<r){
        int m=l+(r-l)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}