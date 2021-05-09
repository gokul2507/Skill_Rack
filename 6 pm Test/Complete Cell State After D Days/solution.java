import java.util.*;
public class Hello{

    final static int CELLCOUNT = 8;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cells[] = new int[CELLCOUNT];
        for(int index=0; index < CELLCOUNT; index++){
            cells[index]=sc.nextInt();
        }
        int daysToProcess = sc.nextInt();
        cells = cellComplete(cells, daysToProcess);
        
        for(int index=0; index < CELLCOUNT; index++){
            System.out.print(cells[index] + " ");
        }
    }
static int[] cellComplete(int cells[], int days){ 
    int i,j,t=0,p,n; 
    for(i=0;i<days;i++) 
    for(j=0;j<8;j++)    
    {       
        p=(j==0)?0:t;  
        n=(j==7)?0:cells[j+1]; 
        t=cells[j];    
        cells[j]=(p==n)?0:1;  
        }   
        return cells;
    
}
}