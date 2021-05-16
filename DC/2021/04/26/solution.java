import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int r=q.nextInt(),c=q.nextInt();
		q.nextLine();
		char z[][]=new char[r][c];
		for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		z[i][j]=q.next().charAt(0);
		for(int j=0;j<c;j++){
		    for(int i=0;i<r;i++){
		        if((i==0 && z[i][j]=='=') || z[i][j]=='-')
		        z[i][j]='x';
		        else
		        break;
		    }
		}
		for(int i=0;i<r;i++){
		    for(char j:z[i])
		    System.out.print(j+" ");
		    System.out.println();
		}
	}
}
