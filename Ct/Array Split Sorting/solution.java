private static void arraySplitSort(int[] arr, int N, int K){
    for(int i=0;i<N;i++){
        int p=i,o=N;
        if(i<K){
            o=K;
        }
        for(int j=i+1;j<o;j++){
            int t=arr[p]-arr[j];
            if(i>=K)
                t=arr[j]-arr[p];
            if(t>0)
                p=j;
        }
        if(i!=p){
            arr[i]+=arr[p];
            arr[p]=arr[i]-arr[p];
            arr[i]-=arr[p];
        }
    }
 }