import java.util.*;
public class Hello {
    static char[][] z;
    public static void submat(int r1,int c1,int r2,int c2,char p){
        while(r1<r2){
            int j=c1;
            while(j<c2){
                if(z[r1][j]!='0')
                p=Character.toUpperCase(p);
                else
                p=Character.toLowerCase(p);
                z[r1][j++]=p;
            }
            r1++;
        }
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		z=new char[x][y];
		for(int i=0;i<x;i++)
		for(int j=0;j<y;j++)
		z[i][j]=q.next().charAt(0);
		int k=q.nextInt(),li=0;
		String l="abcdefghijklmnopqrstuvwxyz";
		for(int i=x-k;i>=0;){
		    int j=0;
		    int ti=i;
		    while(ti<x && j<y){
		        submat(ti,j,ti+k,j+k,l.charAt(li++));
		        li%=26;
		        ti+=k;
		        j+=k;
		    }
		    i-=k;
		}
		for(int j=k;j<y;){
		    int i=0,tj=j;
		    while(i<x && tj<y){
		        submat(i,tj,i+k,tj+k,l.charAt(li++));
		        li%=26;
		        i+=k;
		        tj+=k;
		    }
		    j+=k;
		}
		for(int i=0;i<x;i++){
		    for(int j=0;j<y;j++)
		    System.out.print(z[i][j]+" ");
		    System.out.println();
		}
	}
}
