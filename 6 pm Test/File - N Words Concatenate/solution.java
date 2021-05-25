import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Hello {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        File s=new File("output.txt");
    s.createNewFile();
    FileWriter n=new FileWriter("output.txt");
    int x=sc.nextInt();
    for(int i=0;i<x;i++){
        String c=sc.next();
        n.write(c);
    }
n.close();
        String content = new String(Files.readAllBytes(Paths.get("output.txt")));
        System.out.println(content);
    }

}