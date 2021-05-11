import java.util.Scanner;

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int MAX_CACHE_SIZE = sc.nextInt();
        int N = sc.nextInt();
        int pages[] = new int[N];
        for (int index = 0; index < N; index++) {
            pages[index] = sc.nextInt();
        }
        System.out.println(lruCountMiss(MAX_CACHE_SIZE, pages, N));
    }

}