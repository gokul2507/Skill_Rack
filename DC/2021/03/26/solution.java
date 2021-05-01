import java.util.*;
public class Hello {
    public static boolean chech(char i){
        i=Character.toLowerCase(i);
        return i=='a'||i=='e'||i=='i'||i=='o'||i=='u';
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		char[] a=q.nextLine().toCharArray(),b=q.nextLine().toCharArray();
		char[] x=new char[1000],y=new char[1000];
		int x1=0;
		for(char i:a){
		    if(chech(i))
		    x[x1++]=i;
		}
		x1=0;
		for(char i:b){
		    if(chech(i))
		    y[x1++]=i;
		}
		x1=0;
		int l=a.length;
		for(int i=0;i<l;i++){
		    if(chech(a[i]))
		    a[i]=y[x1++];
		    System.out.print(a[i]);
		}
		x1=0;
		l=b.length;
		System.out.println();
		for(int i=0;i<l;i++){
		    if(chech(b[i]))
		    b[i]=x[x1++];
		    System.out.print(b[i]);
		}
	}
}
