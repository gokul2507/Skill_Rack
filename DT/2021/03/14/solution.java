import java.util.*;
public class Hello {
    static int x,y,l1=0,k=0;
    static int[][] z;
    static int[] l;
    public static void asd(boolean q){
        for(int i=0;i<y;i++){
            if(z[0][i]%10==k){
                if(q)
                z[0][i]=l[l1++];
                else
                l[l1++]=z[0][i];
            }
        }
        for(int i=1;i<x;i++)
        if(z[i][y-1]%10==k){
            if(q)
            z[i][y-1]=l[l1++];
            else
            l[l1++]=z[i][y-1];
        }
        for(int i=y-2;i>-1;i--)
        if(z[x-1][i]%10==k){
            if(q)
            z[x-2][i]=l[l1++];
            else
            l[l1++]=z[x-2][i];
            
        }
        for(int i=x-2;i>=0;i--){
            if(z[i][0]%10==k){
                if(q)
                z[i][0]=l[l1++];
                else
                l[l1++]=z[i][0];
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
		k=z[x-1][y-1]%10;
		l=new int[x*4-2];
		asd(1!=1);
		//Rotating the list  l
		int t=l[l1-1];
		for(int i=l1-1;i>0;i--)
		l[i]=l[i-1];
		l[0]=t;
		l1=0;
		asd(1==1);
		for(int i=0;i<x;i++){
		    for(int j=0;j<y;j++)
		    System.out.print(z[i][j]+" ");
		    
		    System.out.println();
		}
	}
}
