import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt(),c=0;
		int a[][]=new int[n][2];
		for(int i=0;i<n;i++){
		    a[i][0]=q.nextInt();
		    a[i][1]=q.nextInt();
		}
		int x1=q.nextInt(),y1=q.nextInt(),x2=q.nextInt(),y2=q.nextInt();
		for(int i=0;i<n;i++){
		    if(x1<=a[i][0] && a[i][0]<=x2 && y2<=a[i][1] && a[i][1]<=y1)
		    c++;
		}
		System.out.print(c);
	}
}
