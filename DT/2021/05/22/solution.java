import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		q.nextLine();
		String z[][]=new String[x][y],l[][]=new String[x][y];
		for(int i=0;i<x;i++){
		    String[] t=q.nextLine().split(" ");
		    for(int j=0;j<y;j++){
		        z[i][j]=t[j];
		    }
		}
		for(int i=0;i<x;i++){
		    String[] t=q.nextLine().split(" ");
		    for(int j=0;j<y;j++){
		        if("aeiouAEUIO".contains(t[j])){
		            l[i][j]=z[i][j];
		            z[i][j]=t[j];
		        }
		        else{
		            l[i][j]=t[j];
		        }
		        System.out.print(z[i][j]+" ");
		    }
		    System.out.println();
		}
		for(int i=0;i<x;i++){
		    for(String j:l[i])System.out.print(j+" ");
		    System.out.println();
		}
	}
}