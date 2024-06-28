import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String st = sc.next();
		int cnt = 0;
		for(int i=0;i<st.length();i++) {
			cnt++;
		}
		System.out.println(cnt);
		sc.close();
	}

}
