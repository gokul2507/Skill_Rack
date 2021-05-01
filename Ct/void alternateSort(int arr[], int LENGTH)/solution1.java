import java.util.Scanner;

public class Hello {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    printPattern(N);
  }
  private static void alternateSort(int arr[], int LENGTH) {
    Arrays.sort(arr);
    int x[]=new int[LENGTH];
    int i=0,l=0,r=LENGTH-1;
    for(l=0,r=-1+LENGTH;l<r;r--,l++){
        x[i++]=arr[r];
        x[i++]=arr[l];
    }
    if(LENGTH%2==1)
    x[r+l]=arr[r];
    for(i=0;i<LENGTH;i++)
    arr[i]=x[i];
  }
} // end of class
