import java.util.*;
 
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        List<Movie> movies = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            String currMovie[] = sc.nextLine().trim().split("\\s+");
            Movie movie = new Movie(currMovie[0], currMovie[1],
                    Integer.parseInt(currMovie[2]));
            movies.add(movie);
        }
        Collections.sort(movies);
        for (Movie movie : movies) {
            System.out.println(movie);
        }
    } // end of main function
} // end of Hello class

