private static void printPattern(int N) {
    int t=1;
    for(int i=1;i<=N;i++){
        if(i%2==0){
            t+=i-1;
            for(int j=0;j<i;j++)
            System.out.print((t--)+" ");
            t+=i+1;
        }
        else{
            for(int j=0;j<i;j++)
            System.out.print((t++)+" ");
        }
        System.out.println();
    }
}