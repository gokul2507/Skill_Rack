import java.util.*;
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		int dp[]=new int[10001];
		Arrays.fill(dp,Integer.MAX_VALUE);
		dp[0]=0;
		int coins[]={1,5,7,10};
		for(int i=1;i<=10000;i++){
		    for(int j:coins){
		        if(j<=i && dp[i-j]!=Integer.MAX_VALUE){
		            dp[i]=Math.min(dp[i],1+dp[i-j]);
		        }
		    }
		}
		for(int i=0;i<n;i++){
		    System.out.println(dp[q.nextInt()]);
		}
	}
}
