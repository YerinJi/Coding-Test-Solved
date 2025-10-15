import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringBuilder sb = new StringBuilder(input);
        if(sb.charAt(0)=='A'){
            if(sb.charAt(1)=='+')
                System.out.println(4.3);
            else if(sb.charAt(1)=='0')
                System.out.println(4.0);
            else if(sb.charAt(1)=='-')
                System.out.println(3.7);
        }else if(sb.charAt(0)=='B'){
            if(sb.charAt(1)=='+')
                System.out.println(3.3);
            else if(sb.charAt(1)=='0')
                System.out.println(3.0);
            else if(sb.charAt(1)=='-')
                System.out.println(2.7);
        }else if(sb.charAt(0)=='C'){
            if(sb.charAt(1)=='+')
                System.out.println(2.3);
            else if(sb.charAt(1)=='0')
                System.out.println(2.0);
            else if(sb.charAt(1)=='-')
                System.out.println(1.7);
        }else if(sb.charAt(0)=='D'){
            if(sb.charAt(1)=='+')
                System.out.println(1.3);
            else if(sb.charAt(1)=='0')
                System.out.println(1.0);
            else if(sb.charAt(1)=='-')
                System.out.println(0.7);
        }else
            System.out.println(0.0);
    }
}