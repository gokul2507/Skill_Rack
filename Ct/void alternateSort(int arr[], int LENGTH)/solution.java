import java.util.Arrays;
import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //Accept Input
        int N = sc.nextInt();
        int arr[] = new int[N];
        for (int index = 0; index < N; index++) {
            arr[index] = sc.nextInt();
        }

        alternateSort(arr, N);

        for (int index = 0; index < N; index++) {
            System.out.print(arr[index]+" ");
        }
    }
    private static void alternateSort(int arr[], int LENGTH) {
        for(int i=0;i<LENGTH;i++){
            int t=i;
            for(int j=i+1;j<LENGTH;j++){
                if(i%2!=0){
                    if(arr[t]>arr[j])
                    t=j;
                }
                else{
                    if(arr[t]<arr[j])
                    t=j;
                }
            }
            if(i!=t){
                arr[t]+=arr[i];
                arr[i]=arr[t]-arr[i];
                arr[t]=arr[t]-arr[i];
            }
        }
    }
} // end of the class
