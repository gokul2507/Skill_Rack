import java.util.*;
 
public class Hello {
    class Company
{

  String Name;
  public Company (String Name) 
 {
    this.Name = Name;
 }


  public String generateEmailId(String a, String b)
 {
    return(a.toLowerCase()+". "+b.toLowerCase()+"@"+Name.toLowerCase());
  }

}
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String domainName = sc.nextLine().trim();
        Company company = new Company(domainName);
        int N = Integer.parseInt(sc.nextLine().trim());
        for (int ctr = 1; ctr <= N; ctr++) {
            String emp[] = sc.nextLine().trim().split("\\s+");
            System.out.println(company.generateEmailId(emp[0], emp[1]));
        }
    }
}

