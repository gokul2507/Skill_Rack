import java.util.*;
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),l=0;
		char[][] z=new char[1][1];
		q.nextLine();
		for(int i=0;i<n;i++){
		    String t=q.nextLine();
		    if(i==0){
		        l=t.length();
		        z=new char[n][l];
		    }
		    z[i]=t.toCharArray();
		}
		int k=q.nextInt();
		for(int i=0;i<n;i++){
		    for(int j=0;j<l;j++){
		        char c=z[i][j];
		        if(j>0 && j<l-1)
		        c=z[(i+k)%n][j];
		        System.out.print(c);
		    }
		    System.out.println();
		}
	}
}
