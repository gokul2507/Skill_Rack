import java.util.*;
public class Hello {
    static char z[][];
    static int a,b;
    static String s;
    public static void replace(int x,int y){
        while(s.length()>0){
            z[x][y]=s.charAt(0);
            y++;
            x+=y/b;
            y%=b;
            x%=a;
            s=s.substring(1);
        }
        for(int i=0;i<a;i++){
            for(char j:z[i]){
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		a=q.nextInt();
		b=q.nextInt();
		q.nextLine();
		z=new char[a][b];
		for(int i=0;i<a;i++){
		    for(int j=0;j<b;j++)
		    z[i][j]=q.next().charAt(0);
		    q.nextLine();
		}
		s=q.nextLine();
		for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
		if(z[i][j]==s.charAt(0)){
		    replace(i,j);
		    return;
		}
	}
}