import java.util.*;
public class Hello {

    public static void main(String[] args) {
	    Scanner s=new Scanner(System.in);
	    int r=s.nextInt();
	    int c=s.nextInt();
	    char[][] mat=new char[r][c];
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                mat[i][j]=s.next().charAt(0);
            }
        }
        String s1=s.next();
        for(int g=0;g<r;g++) {
            for(int h=0;h<c;h++) {
                for(int a=0;a<r-g;a++) {
                    for(int b=0;b<c-h;b++) {
                        String s2="";
                        for(int i=a;i<=a+g;i++) {
                            for(int j=b;j<=b+h;j++) {
                                s2+=mat[i][j]+"";
                            }
                        }
                        if(s2.equals(s1)) {
                            for(int i=a;i<=a+g;i++) {
                                for(int j=b;j<=b+h;j++) {
                                    System.out.print(mat[i][j]+" ");
                                }
                                System.out.println();
                            }
                            System.exit(0);
                        }
                    }
                }
            }
        }
	}
}