import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        int l=0,t=q.nextInt(),n=q.nextInt();
        q.nextLine();
        int[] z=new int[n];
        for(String i:q.nextLine().split(" ")){
            z[l++]=Integer.parseInt(i);
            if(l>=t){
                int m=z[l-1];
                for(int j=l-2;j>=l-t;j--)
                m=Math.max(m,z[j]);
                System.out.print(m+" ");
            }
        }
	}
}
