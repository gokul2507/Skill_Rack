import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		int z[][]=new int[x][y];
		for(int i=0;i<x;i++)
		for(int j=0;j<y;j++)
		z[i][j]=q.nextInt();
		int a=q.nextInt()-1,b=q.nextInt()-1;
		for(int i=0;i<y;i++)
		System.out.print(z[a][i]*z[b][y-1-i]+" ");
	}
}