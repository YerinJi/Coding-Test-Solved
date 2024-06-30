import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rep = sc.nextInt();
        for(int i=1; i<= rep; i++){
            int num = sc.nextInt();
            String str = sc.next();
            for(int k=0; k<str.length(); k++){
                char ch = str.charAt(k);
                for(int j=1; j<= num; j++){
                    System.out.print(ch);
                }
            }
            System.out.println();
        }

    }
}