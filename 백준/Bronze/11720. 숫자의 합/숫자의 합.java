import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cnt = sc.nextInt();
		String st = sc.next();
		int sum = 0;
		for(int i=0; i< cnt; i++ ) {
			sum += st.charAt(i)-48;
		}
		System.out.println(sum);
		
		sc.close();
	}

}
