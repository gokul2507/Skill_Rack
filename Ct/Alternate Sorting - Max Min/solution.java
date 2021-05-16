private static void alternateSort(int arr[], int LENGTH) {
    for(int i=0;i<LENGTH;i++){
        int p=i;
        for(int j=i+1;j<LENGTH;j++){
            int s=arr[p]-arr[j];
            if(i%2==0)
            s=arr[j]-arr[p];
            if(s>0)
            p=j;
        }
        if(i!=p){
            arr[i]+=arr[p];
            arr[p]=arr[i]-arr[p];
            arr[i]-=arr[p];
        }
    }
}