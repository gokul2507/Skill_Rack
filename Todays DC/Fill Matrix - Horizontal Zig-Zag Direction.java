public class solution {
    
}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		int[] z=new int[n];
		for(int i=0;i<n;i++){
		    z[i]=q.nextInt();
		}
		int inc=-1,x=q.nextInt(),y=q.nextInt(),l=0,r=x-1,c=y-1;
		int[][] m=new int[x][y];
		while(l<n){
		    m[r][c]=z[l++];
		    c+=inc;
		    if(c==-1){7
		        c=0;
		        r-=1;
		        inc*=-1;
		    }
		    else
		    if(c==y){
		        c=y-1;
		        r-=1;
		        inc*=-1;
		    }
		    if(r==-1){
		        r=x-1;
		        c=y-1;
		        inc=-1;
		    }
		}
		for(int i=0;i<x;i++){
		    for(int j=0;j<y;j++){
		        System.out.print(m[i][j]+" ");
		    }
		    System.out.println();
		}
	}
}