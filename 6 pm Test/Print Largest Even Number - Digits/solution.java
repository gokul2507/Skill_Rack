import java.util.*;
public class Hello {

    public static void main(String[] args) {
		char[] z=new Scanner(System.in).nextLine().toCharArray();
		Arrays.sort(z);
		int i=0;
		for(;i<z.length;i++){
		    if("02468".contains(z[i]+""))
		    break;
		}
		for(int j=z.length-1;j>=0;j--)
		if(j!=i)
		System.out.print(z[j]);
		System.out.print(z[i]);
	}
}