import java.util.*;
public class Hello {
    public static void printnum(int n,int p){
        int in=1,s=1,e=n+1;
        if(p==0){
            s=n;
            e=0;
            in=-1;
        }
        while(s!=e){
            System.out.print(s);
            s+=in;
        }
    }
    public static void main(String[] args) {
		int n=new Scanner(System.in).nextInt();
		for(int i=1;i<=n;i++){
		    String s="*";
		    if(i%2==1){
		        System.out.print(s);
		        s="";
		    }
		    printnum(i,i%2);
		    System.out.println(s);
		}
	}
}
