import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){ //다음 줄에 입력이 있는지 여부를 판단
            String str = sc.nextLine();
            System.out.println(str);
        }
        sc.close();
    }
}