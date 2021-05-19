import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		int z[]=new int[n];
		for(int i=0;i<n;i++)
		z[i]=q.nextInt();
		for(int i=0;i<n;i++){
		    int p=i;
		    for(int j=i+1;j<n;j++){
		        if(z[p]%10>z[j]%10)
		           p=j;
		        else{
		            if(z[p]%10==z[j]%10 && (z[p]/10)%10>(z[j]/10)%10)
		                p=j;
		        }
		    }
		    if(i!=p){
		        z[i]+=z[p];
		        z[p]=z[i]-z[p];
		        z[i]-=z[p];
		    }
		    System.out.print(z[i]+" ");
		}
	}
}