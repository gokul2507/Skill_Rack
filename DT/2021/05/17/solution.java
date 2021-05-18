import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner sc=new Scanner(System.in);
		int i,j,k,l,n,r,c;
		r=sc.nextInt();
		c=sc.nextInt();
		int a[][]=new int[r][c];
		for(i=0;i<r;i++){
		    for(j=0;j<c;j++){
		        a[i][j]=sc.nextInt();
		    }
		}
		n=sc.nextInt()-1;
		k=n+1;
		while(true){
		    for(j=0;j<c;j++){
		        if(k>=r){
		            System.out.print(a[n][j]+" ");
		        }
		        else if(n<0){
		            System.out.print(a[k][j]+" ");
		        }
		        else{
		            System.out.print((a[k][j]+a[n][j])+" ");
		        }
		    }
		    k++;
		    n--;
		    System.out.println();
		    if(k>=r && n<0)    break;
		}
	}
}