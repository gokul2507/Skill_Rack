import java.util.*;

interface Transaction {

    void withdraw(int amt);

    void deposit(int amt);

    int viewBalance();
} // end of Transaction interface
class BankAccount implements Transaction{
    private int balance;
    BankAccount(int bal)
    {
        this.balance=bal;
    }
    public void deposit(int amt)
    {
        balance+=amt;
    }
    public void withdraw(int amt)
    {
        if(balance>=amt)
        balance-=amt;
        else
        System.out.println("Insufficient Balance");
    }
    public int viewBalance()
    {
        return balance;
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int initialBalance = sc.nextInt();
        Transaction account = new BankAccount(initialBalance);
        int N = sc.nextInt();
        for (int ctr = 1; ctr <= N; ctr++) {
            int amt = sc.nextInt();
            if (amt > 0) {
                account.deposit(amt);
            } else {
                account.withdraw(-amt);
            }
            System.out.println(account.viewBalance());
        }
    } // end of main method
} // end of Hello class