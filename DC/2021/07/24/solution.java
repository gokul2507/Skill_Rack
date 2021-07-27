import java.util.*;
class Hello{  
    public static void main(String[] args){    
        Scanner sc=new Scanner(System.in); 
        int rowCount=0,sum=0;   
        while(sc.hasNextLine()){   
            String str=sc.nextLine(); 
            rowCount++;      
            if((rowCount&1)==1){ 
                System.out.print(str+" ");    
            }
            else{  
                sum+=(Integer.parseInt(str));
            }   
        }     
        System.out.printf("\n%d",sum);  
    }
}