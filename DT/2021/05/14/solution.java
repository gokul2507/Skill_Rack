import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
Scanner in=new Scanner(System.in);
int r=in.nextInt(),c=in.nextInt();
String mat[][]=new String[r][c];
for(int i=0;i<r;i++)
{
    for(int j=0;j<c;j++)
    mat[i][j]=in.next();
}
for(int i=0;i<c;i++)
{
    ArrayList<String> al1=new ArrayList<>();
    ArrayList<String> al2=new ArrayList<>();
    for(int j=0;j<r;j++)
    {
        if(mat[j][i].length()==1 && Character.isLetter(mat[j][i].charAt(0)))
        al1.add(mat[j][i]);
        else
        al2.add(mat[j][i]);
    }
    int ind=0;
    for(String st:al1)
    mat[ind++][i]=st;
    for(String st:al2)
    mat[ind++][i]=st;
}
for(int i=0;i<r;i++)
{
    for(int j=0;j<c;j++)
    System.out.print(mat[i][j]+" ");
    System.out.println();
}
	}
}