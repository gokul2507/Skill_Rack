import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int x=q.nextInt(),y=q.nextInt();
		char z[][]=new char[x][y];
		q.nextLine();
		
		for(int i=0;i<x;i++){
		    String[] t=q.nextLine().split(" ");
		    for(int j=0;j<y;j++){
		        z[i][j]=t[j].charAt(0);
		        if(z[i][j]=='B')
		        z[i][j]='-';
		    }
		}
		for(int j=0;j<y;j++){
    		for(int i=x-1;i>=0;i--){
    		    //System.out.println(z[i][j]=="B"+"\n");
    		    if(z[i][j]=='-'){
    		       //System.out.println(i+" "+j+"\n");
    		        boolean flag=true;
    		        for(int k=0;k<i;k++){
    		            if(z[k][j]=='A'){
    		                z[k][j]='-';
    		                z[i][j]='A';
    		                flag=false;
    		                break;
    		            }
    		            z[k][j]='-';
    		        }
    		        if(flag)
    		        break;
    		    }
    		}
		}
    	for(int i=0;i<x;i++){
    	    for(char j:z[i])
    	    System.out.print(j+" ");
    	    System.out.println();
    	}
    }
}
