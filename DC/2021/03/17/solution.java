import java.util.*;
public class Hello {
    static int x,y;
    static char[][] z;
    public static boolean check(int x,int y){
        boolean t=false;
        try{
            if(z[x][y]=='*')
            t=true; 
        }
        catch(Exception e){}
        return t;
    }
    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        x=q.nextInt();
        y=q.nextInt();
        z=new char[x][y];
        q.nextLine();
        for(int i=0;i<x;i++)
        for(int j=0;j<y;j++)
        z[i][j]=q.next().charAt(0);
        int c=0;
        for(int i=0;i<x;i++)
        for(int j=0;j<y;j++)
        if(z[i][j]=='-' &&(check(i-1,j-1)||check(i-1,j+1)||check(i+1,j-1)||check(i+1,j+1)))
        c++;
        System.out.println(c);
	}
}
