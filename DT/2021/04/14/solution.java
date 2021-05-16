import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int a=q.nextInt();
		q.nextLine();
		String[][] z1=new String[a][a],z2=new String[a][a];
		for(int i=0;i<a;i++)
		z1[i]=q.nextLine().split(" ");
		for(int i=0;i<a;i++)
		z2[i]=q.nextLine().split(" ");
		int k=q.nextInt();
		for(int i=0;i<a;i++){
		    for(int j=0;j<a;j++){
		        if(i<k || j<k || a-i-1<k || a-j-1<k){
		           String c=z1[i][j];
		           z1[i][j]=z2[i][j];
		           z2[i][j]=c;
		        }
		        System.out.print(z1[i][j]+" ");
		    }
		    System.out.println();
		}
		for(int i=0;i<a;i++){
		    for(String j:z2[i])
		    System.out.print(j+" ");
		    System.out.println();
		}
	}
}
