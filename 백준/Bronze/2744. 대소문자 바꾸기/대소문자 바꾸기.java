import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        StringBuilder sb = new StringBuilder(input);

        for(int i = 0; i < sb.length(); i++){
            char c = sb.charAt(i);
            if(c>='A' && c<='Z'){
                sb.setCharAt(i, (char)(c+32));
            } else if(c>='a' && c<='z'){
                sb.setCharAt(i, (char)(c-32));
            }
        }
        System.out.println(sb.toString());
    }
}