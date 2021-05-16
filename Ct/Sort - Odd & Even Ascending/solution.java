import java.util.*;
public class Hello {
    static int[] z,o,e;
    static int n,oi=0,ei=0;
    public static int[] sort(int[] a,int l){
        for(int i=0;i<l;i++){
            for(int j=i+1;j<l;j++)
            if(z[a[i]]>z[a[j]]){
                int t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
        return a;
    }
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		n=q.nextInt();
		z=new int[n];
		o=new int[n];
		e=new int[n];
		for(int i=0;i<n;i++)
		{
		    int t=q.nextInt();
		    z[i]=t;
		    if(t%2==0)
		    e[ei++]=i;
		    else
		    o[oi++]=i;
		}
		e=sort(e,ei);
		o=sort(o,oi);
		ei=0;
		oi=0;
		for(int i:z)
		if(i%2!=0)
		System.out.print(z[o[oi++]]+" ");
		else
		System.out.print(z[e[ei++]]+" ");
	}
}
