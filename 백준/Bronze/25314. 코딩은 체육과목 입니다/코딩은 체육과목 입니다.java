import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int byt = sc.nextInt();
		for(int i =1; i<= byt/4; i++) {
			System.out.print("long ");
		}
		System.out.print("int");
	}

}