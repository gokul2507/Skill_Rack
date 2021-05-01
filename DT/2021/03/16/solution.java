import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int z1=0,n=q.nextInt();
		int[] z=new int[n];
		q.nextLine();
		for(String i:q.nextLine().split(" ")){
		    z[z1++]=Integer.parseInt(i);
		}
		int x=q.nextInt();
		char k=q.next().charAt(0);
		if(k=='R'){
		    for(int i=0,j=n-1;i<=j;i++,j--){
		        int y=z[i];
		        z[i]=z[j];
		        z[j]=y;
		    }
		}
		z1=1;
		int c=1,t=z[0]-x;
		while(z1<n){
		    if(t<=0)
		    break;
		    if(t<z[z1])
		    t=z[z1];
		    t-=x;
		    c++;
		    z1++;
		}
		
		System.out.println(c);
	}
}
