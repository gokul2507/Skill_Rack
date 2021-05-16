import java.util.*;
public class Hello {
    static int x,y,k;
    static String s;
    static int z[][];
    public static boolean check(int m){
        int a=(x-1-m)%2;
        if(a==0)
        s="L";
        else
        s="R";
        if(x-m-1<k){
            System.out.println(s+" "+y+"\nU");
            return false;
        }
        else{
            int inc=1,sr=0,en=y;
            if(a==0){
                inc=-1;
                en=-1;
                sr=y-1;
            }
            int c=0;
            while(sr!=en){
                if(z[m][sr]!=0)
                c++;
                else{
                    System.out.print(s+" "+(c+1));
                    return true;
                }
                sr+=inc;
            }
            System.out.println(s+" "+c+"\nU");
            return false;
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
		k=q.nextInt();
		for(int i=x-1;i>=0;i--){
		    if(check(i)){
		        break;
		    }
		}
	}
}
