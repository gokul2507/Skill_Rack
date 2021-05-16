import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		char z[][]=new char[y][x];
		q.nextLine();
		for(int i=0;i<x;i++){
		    String t[]=q.nextLine().split(" ");
		    for(int j=0;j<y;j++){
		        z[j][i]=t[j].charAt(0);
		        if(z[j][i]=='B')
		        z[j][i]='-';
		        if(i==x-1)
		        Arrays.sort(z[j]);
		    }
		}
		for(int j=0;j<x;j++){
		    for(int i=0;i<y;i++)
		    System.out.print(z[i][j]+" ");
		    System.out.println();
		}
	}
}
