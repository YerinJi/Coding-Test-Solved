import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int price = sc.nextInt();
		int cnt = sc.nextInt();
		int check = 0;
		for(int i=1; i<= cnt; i++) {
			int price1 = sc.nextInt();
			int pcnt = sc.nextInt();
			check += price1 * pcnt;
		}
		if(price == check)
			System.out.println("Yes");
		else
			System.out.println("No");
	}

}