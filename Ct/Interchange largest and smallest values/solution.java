import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),s=0,l=0;
		int[] z=new int[n];
		for(int i=0;i<n;i++){
		    z[i]=q.nextInt();
		    if(i!=0){
		        if(z[i]<z[s])
		        s=i;
		        if(z[i]>z[l])
		        l=i;
		    }
		}
		z[s]+=z[l];
		z[l]=z[s]-z[l];
		z[s]-=z[l];
		for(int i:z)
		System.out.print(i+" ");
	}
}
