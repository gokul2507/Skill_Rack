import java.util.*;
public class Hello {
    static int z[],l=0;
    public static void move(int x){
        for(int i=x;i<l-1;i++)
        z[i]=z[i+1];
        z[l-1]=0;
        l--;
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int s=q.nextInt(),n=q.nextInt(),m=0;
		z=new int[s];
		for(int i=0;i<n;i++){
		    int f=1,t=q.nextInt();
		    for(int j=0;j<l;j++){
		        if(z[j]==t){
		            f=0;
		            move(j);
		            break;
		        }
		    }
		    if(f==1){
		        if(l>=s){
		            move(0);
		        }
		        m++;
		        //System.out.println("-");
		    }
		    z[l++]=t;
		    /*for(int j=0;j<l;j++){
		        System.out.print(z[j]+" ");
		    }
		    System.out.println();*/
		}
		System.out.print(m);
	}
}