import java.util.*;
public class Hello {

    public static void main(String[] args) {
		char[] a=new Scanner(System.in).nextLine().toCharArray();
		for(int i=0;i<a.length;){
    		String s="";
    		for(int j=i;j<i+5;j++){
    		    if(Character.isUpperCase(a[j]))
    		    s+="1";
    		    else
    		    s+="0";
    		}
    		int x=Integer.parseInt(s,2);
    		int t=(x<26)?0:x;
    		char y=' ';
    		switch(t){
    		    case 0:
    		        y=(char)(x+97);
    		        break;
    		    case 26:
    		        y='.';
    		        break;
    		  case 27:
    		      y=',';
    		      break;
    		  case 29:
    		      y='?';
    		      break;
    		  case 30:
    		      y='\'';
    		      break;
    		  case 31:
    		      y='\"';
    		      break;
    		}
    		System.out.print(y);
    		i+=5;
		}
	}
}
