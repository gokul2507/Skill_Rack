import java.util.*;
public class Hello {

    public static void main(String[] args) {
		HashMap<Character,Integer> d=new HashMap<Character,Integer>();
		String z="",l="";
		for(char i:new Scanner(System.in).nextLine().strip().toCharArray()){
		    d.put(i,d.getOrDefault(i,-1)+1);
		    if(!z.contains(Character.toString(i)))
		    z+=Character.toString(i);
		}
		for(char i:z.toCharArray())
		{if(d.get(i)>0)
		System.out.print(i);}
	}
}
