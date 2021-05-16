import java.util.*;
public class Hello {
    static int r1,r2,c1,c2;
    static char[][] z=new char[8][8];
    public static void kinght(int x,int y){
        if(x>=0 && x<8 && y>=0 &&y<8 && (x!=r1 || y!=c1))
        z[x][y]='k';
    }
    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
		for(int i=0;i<8;i++)
		for(int j=0;j<8;j++)
		z[i][j]='0';
		r1=q.nextInt()-1;
		c1=q.nextInt()-1;
		r2=q.nextInt()-1;
		c2=q.nextInt()-1;
		kinght(r2-1,c2-2);
		kinght(r2+1,c2-2);
		kinght(r2+2,c2-1);
		kinght(r2+2,c2+1);
		kinght(r2-1,c2+2);
		kinght(r2+1,c2+2);
		kinght(r2-2,c2+1);
		kinght(r2-2,c2-1);
		int x=r1,y=c1;
		while(x>0 && y>0){
		    x--;
		    y--;
		}
		while(x<8 && y<8){
		    if(z[x][y]=='k')
		        z[x][y]='x';
		        else
		        z[x][y]='q';
		    
		    x++;
		    y++;
		}
		x=r1;
		y=c1;
		while(x>0 && y<7){
		    x--;
		    y++;
		}
		while(x<8 && y>=0){
		    if(z[x][y]=='k')
		        z[x][y]='x';
		        else
		        z[x][y]='q';
		    
		    x++;
		    y--;
		}
		x=0;
		while(x<8){
		    if(z[x][c1]=='k')
		        z[x][c1]='x';
		        else
		        z[x][c1]='q';
		        x++;
		    
		}
		y=0;
		while(y<8){
		    if(z[r1][y]=='k')
		    z[r1][y]='x';
		    else
		    z[r1][y]='q';
		    y++;
		}
		z[r1][c1]='Q';
		z[r2][c2]='K';
		for(int i=0;i<8;i++){
		    for(int j=0;j<8;j++)
		    System.out.print(z[i][j]+" ");
		    System.out.println();
		}
	}
}
