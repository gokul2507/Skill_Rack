import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int a=q.nextInt(),n=q.nextInt();
		String z[][]=new String[a][n];
		for(int i=0;i<a;i++){
		    for(int j=0;j<n;j++){
		        z[i][j]=q.next();
		    }
		    q.nextLine();
		}
		for(int j=0;j<n;j++){
		    String e[]=new String[n],o[]=new String[n];
		    int el=0,ol=0;
		    for(int i=0;i<a;i++)
		    if("asdfghjklmnbvcxzqwertyuiop".contains(z[i][j]))
		    e[el++]=z[i][j];
		    else
		    o[ol++]=z[i][j];
		    for(int i=0;i<el;i++)
		    z[i][j]=e[i];
		    for(int i=0;i<ol;i++)
		    z[el+i][j]=o[i];
		}
		for(int i=0;i<a;i++){
		    for(int j=0;j<n;j++)
		    System.out.print(z[i][j]+" ");
		    System.out.println();
		}
	}
}