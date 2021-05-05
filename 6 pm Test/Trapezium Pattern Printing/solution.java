import java.util.Scanner;

public class Hello{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        printPattern(sc.nextInt());
    }

public static void printPattern(int N) {
    int a=1;
    int b=(N*N)+1;
    int s=0;
    for(int l=N;l>=1;l--){
        for(int c=s;c>=1;c--){
            System.out.print("-");
        }
        for(int i=1;i<=l;i++){
            if(i==l)
                System.out.print(a++);
            else
                System.out.print((a++)+"*");
        }
        for(int i=1;i<=l;i++){
            System.out.print("*"+(b++));
        }
        System.out.println();
        s+=2;
        b=(b-1)-((l-1)*2);
    }
}
}