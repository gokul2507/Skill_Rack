import java.util.*;
class name{
    String lastname,firstname;
    public name(String a){
        setfirstname(a.split(" ")[0]);
        setlastname(a.split(" ")[1]);
    }
    public void setfirstname(String name){
        this.firstname=name;
    }
    public void setlastname(String name){
        this.lastname=name;
    }
    public String getlastname(){
        return this.lastname;
    }
    public String getfirstname(){
        return this.firstname;
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        int n=q.nextInt();
        q.nextLine();
        name a[]=new name[n];
        for(int i=0;i<n;i++){
            a[i]=new name(q.nextLine());
        }
        Arrays.sort(a,new java.util.Comparator<name>(){
            @Override
            public int compare(name x,name y){
                int r=x.getlastname().compareToIgnoreCase(y.getlastname());
                if(r==0)
                return x.getfirstname().compareToIgnoreCase(y.getfirstname());
                return r;
            }
        }
        );
        for(name i:a)
        System.out.println(i.getfirstname()+" "+i.getlastname());
	}
}
