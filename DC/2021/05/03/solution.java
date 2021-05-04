import java.util.*;
class matrix{
    int r,c,z[][];
    public matrix(){
        Scanner q=new Scanner(System.in);
        this.r=q.nextInt();
        this.c=q.nextInt();
        this.z=new int[this.r][this.c];
        for(int i=0;i<this.r;i++)
        for(int j=0;j<this.c;j++)
        this.z[i][j]=q.nextInt();
    }
   private boolean check(int x,int y){
        boolean p[]=new boolean[10];
        for(int i=x;i<x+3;i++){
            for(int j=y;j<y+3;j++){
                if(p[z[i][j]])
                return 0==1;
                p[z[i][j]]=true;
            }
        }
        return true;
    }
   private void assign(int x,int y){
        int l=1;
        for(int i=x;i<x+3;i++){
            for(int j=y;j<y+3;j++)
            this.z[i][j]=l++;
        }
    }
    public void checkandsort(){
        for(int i=0;i<this.r;){
            for(int j=0;j<this.c;){
                if(check(i,j))
                assign(i,j);
                j+=3;
            }
            i+=3;
        }
    }
    public void display(){
        for(int i=0;i<this.r;i++){
            for(int j=0;j<this.c;j++)
            System.out.print(this.z[i][j]+" ");
            System.out.println();
        }
    }
}
public class Hello {
    
    public static void main(String[] args) {
        matrix m=new matrix();
        m.checkandsort();
        m.display();
	}
}