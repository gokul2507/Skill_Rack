import java.util.*;
public class Hello {
    static int x,y,l1;
    static int[][] z;
    static int[] l;
    public static void mod(int m,int p){
        int t=z[0][m]%10;
        if(p==0)
        l[l1++]=z[0][m];
        else
        z[0][m]=l[l1++];
        for(int i=0;i<x;i++){
            if(t==z[i][m+1]%10){
                if(p==0)
                l[l1++]=z[i][m+1];
                else
                z[i][m+1]=l[l1++];
            }
        }
        for(int i=x-1;i>0;i--){
            if(t==z[i][m]%10){
                if(p==0)
                l[l1++]=z[i][m];
                else
                z[i][m]=l[l1++];
            }
        }
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		x=q.nextInt();
		y=q.nextInt();
		z=new int[x][y];
		for(int i=0;i<x;i++)
		for(int j=0;j<y;j++)
		z[i][j]=q.nextInt();
		for(int i=0;i<y-(y%2);i++){
		    l=new int[x*2];
		    l1=0;
		    mod(i,0);
		    //swap
		    int o=l[l1-1];
		    for(int j=l1-1;j>0;j--)
		    l[j]=l[j-1];
		    l[0]=o;
		    l1=0;
		    mod(i,1);
		    i++;
		}
		for(int i=0;i<x;i++){
		    for(int j=0;j<y;j++)
		    System.out.print(z[i][j]+" ");
		    
		    System.out.println();
		}
	}
}
