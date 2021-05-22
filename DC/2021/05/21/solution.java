import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
Scanner in=new Scanner(System.in);
String s=in.nextLine();
String ar[]=s.split(" ");
if(ar.length>1)
{
    for(int i=ar.length-1;i>=0;i--)
    System.out.println(ar[i]+" ");
}
else
{
    ArrayList<Integer> al=new ArrayList<>();
    al.add(Integer.parseInt(s));
    while(in.hasNextInt())
    al.add(in.nextInt());
    for(int i=al.size()-1;i>=0;i--)
    System.out.print(al.get(i)+" ");
}
	}
}