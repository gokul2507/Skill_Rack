import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int r=q.nextInt(),c=q.nextInt();
		q.nextLine();
		String z[][]=new String[r][c];
		for(int i=0;i<r;i++){
		    z[i]=q.nextLine().split(" ");
		}
		String w="";
		int e=0;
		for(int j=0;j<c;j++){
		    for(int i=0;i<r;i++){
		        if(z[i][j].matches("[a-zA-Z#]"))
		        w+=z[i][j];
		        else{
		            e+=Integer.parseInt(z[i][j]);
		        }
		    }
		}
		System.out.println(e+"\n"+w);
	}
}
