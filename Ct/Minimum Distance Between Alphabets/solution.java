import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		String s=q.nextLine();
		char c1=q.next().charAt(0),c2=q.next().charAt(0);
		int l=s.length(),z1[]=new int[l],z2[]=new int[l],zl1=0,zl2=0;
		if(c1==c2 && s.indexOf(c1)==s.lastIndexOf(c1)){
		    System.out.println(l-1);
		    return;
		}
		for(int i=0;i<l;i++){
		    if(s.charAt(i)==c1)
		    z1[zl1++]=i;
		    if(s.charAt(i)==c2)
		    z2[zl2++]=i;
		}
		int t=l;
		for(int i=0;i<zl1;i++){
		    for(int j=0;j<zl2;j++){
		        if(z1[i]!=z2[j]){
		            t=Math.min(t,Math.max(z1[i],z2[j])-Math.min(z1[i],z2[j]));
		        }
		    }
		}
		System.out.println(Math.max(t-1,0));
	}
}