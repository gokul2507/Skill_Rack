import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int r=q.nextInt(),c=q.nextInt();
		int z[][]=new int[c][r];
		for(int j=0;j<r;j++)
		for(int i=0;i<c;i++)
		z[i][j]=q.nextInt();
		for(int i=0;i<c;i++){
		    for(int j:z[i])
		    System.out.print(j+" ");
		    System.out.println();
		}
	}
}
