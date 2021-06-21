import java.util.Scanner;
public class Hello {
    class MaxCreditLimitExceededException extends Exception{
        public MaxCreditLimitExceededException(String s){
            super(s);
        }
    }
    class InsufficientBalance extends Exception{
        public InsufficientBalance(String s){
            super(s);
        }
    }
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());

        //Initial account balance
        int balance = 1000;

        for (int transactionCtr = 1; transactionCtr <= N; transactionCtr++) {
            char transactionType = sc.next().charAt(0);
            int amount = Integer.parseInt(sc.nextLine().trim());
            try {
                if (transactionType == '+') {
                    if (amount > 10000) {
                        throw new MaxCreditLimitExceededException("Max credit limit exceeded");
                    }
                    balance += amount;
                    System.out.println(balance);
                } else if (transactionType == '-') {
                    if (amount > balance) {
                        throw new InsufficientBalance("Insufficient balance");
                    }
                    balance -= amount;
                    System.out.println(balance);
                }
            } catch (MaxCreditLimitExceededException | InsufficientBalance e) {
                System.out.println(e.getMessage());
            }
        }
    } // end of main function
} // end of Hello class