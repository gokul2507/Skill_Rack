import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),l=0;
		int qw[]=new int[101];
		int z[]=new int[n],or[]=new int[n];
		for(int i=0;i<n;i++){
		    int r=q.nextInt();
		    or[i]=r;
		    if(qw[r]==1)continue;
		    qw[r]=1;
		    z[l++]=r;
		}
		for(int i=0;i<l;i++){
		    for(int j=i+1;j<l;j++){
		        if(z[i]<z[j]){
		            z[i]+=z[j];
		            z[j]=z[i]-z[j];
		            z[i]-=z[j];
		        }
		    }
		}
		int t=or[q.nextInt()-1];
		for(int i=0;i<l;i++)
		if(z[i]==t){
		    System.out.println(i+1);
		    return;
		}
	}
}