import java.util.*;
public class solution {

    public static void main(String[] args) {
		//Your Code Here 
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt();
		int c = sc.nextInt();
		char[][] ch = new char[r][c];
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        ch[i][j] = sc.next().charAt(0);
		    }
		}
		int flag =0;
		int n = sc.nextInt();
		for(int i=0;i<=r-n;i++){
		    for(int j=0;j<=c-n;j++){
		        flag =0;
		        if(ch[i][j]==ch[i+(n-1)][j] && ch[i][j]==ch[i][j+(n-1)] && ch[i][j]==ch[i+(n-1)][j+(n-1)]){
    		        for(int i1=i;i1<i+n;i1++){
    		            for(int j1=j;j1<j+n;j1++){
    		                if((i1-i)==(j1-j)){
    		                    ch[i1][j1]='*';
    		                    
    		                }
    		                if((i1-i)+(j1-j)==n-1){
    		                    ch[i1][j1] = '*';
    		                }
    		                flag = 1;
    		            }
    		        }
		        }
		        if(flag == 1){
		            break;
		        }
		    }
		    if(flag==1){
		        break;
		    }
		} 
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        System.out.print(ch[i][j]+" ");
		    }
		    System.out.println();
		}
		sc.close();
	}
}