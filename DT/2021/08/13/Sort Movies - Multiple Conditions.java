import java.util.*;

class Movie implements Comparable<Movie>{
    String n,r;
    int t,y;
    public Movie(String x,String y,int z){
        String[] q=y.split(":");
        this.n=x;
        this.y=z;
        this.r=y;
        this.t=Integer.parseInt(q[0]+q[1]);
    }
    @Override
    public int compareTo(Movie q){
        if(this.y!=q.y){
            return q.y-this.y;
        }
        if(this.t!=q.t)
        return q.t-this.t;
        return this.n.compareTo(q.n);
    }
    public String toString(){
        return n+" "+this.r+" "+this.y;
    }
    
}

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

