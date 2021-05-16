import java.util.*;
class Details{
    String name;
    HashSet<String> folder;
    HashSet<String> file;
    public Details(String name){
        this.name=name;
        folder=new HashSet<String>();
        file=new HashSet<String>();
    }
    public void AddFolder(String folderName){
        folder.add(folderName);
    }
    public void AddFile(String fileName){
        file.add(fileName);
    }
    String sizeof(int l,String s){
        if(l>1 ||l==0)
        s+="s";
        return " "+l+" "+s;
    }
    public String toString(){
        return sizeof(folder.size(),"folder")+sizeof(file.size(),"file");
    }
}
public class Hello {
    public static void main(String[] args) {
		Scanner q=new Scanner(System.in);
		int n=q.nextInt();
		q.nextLine();
		TreeMap<String,Details> z=new TreeMap<String,Details>();
		Details t;
		while(n-->0){
		    String[] s=q.nextLine().split("\\\\");
		    t=z.getOrDefault(s[1],new Details(s[1]));
		    int l=s.length-2;
		    if(l>1){
		        t.AddFolder(s[2]);
		    }
		    else{
		        t.AddFile(s[2]);
		    }
		    z.put(s[1],t);
		}
		for(String i:z.keySet()){
		    System.out.print(i+" -");
		    t=z.get(i);
		    System.out.println(t);
		}
	}
}
