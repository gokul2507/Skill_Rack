import java.util.*;
public class Hello {
    static int a;
    static void print(int p){
        for(int i=0;i<a;i++)
        System.out.print(p+i+" ");
        System.out.println();
    }
    public static void main(String[] args) {
        a=new Scanner(System.in).nextInt();
        int i=1,t=a,z[]=new int[(a)/2];
        for(int j=(a)/2-1;j>=0;j--){
            print(i);
            i+=t;
            z[j]=i;
            i+=t;
        }
        if(a%2==1)
        print(i);
        for(int j:z){
            print(j);
        }
	}
}