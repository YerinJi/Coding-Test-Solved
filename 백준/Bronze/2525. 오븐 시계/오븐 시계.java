import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		int time = sc.nextInt();
		if(m+time <=59) {
			m += time;
			System.out.println(h + " " + m);
		}
		else {
			m += time;
			if(m%60 == 0) {
				h += m/60;
				m = 0;
			}
			else {
				h += m/60;
				m = m%60;
			}
			
			if(h>=24)
				h-=24;
				
			System.out.println(h + " " + m);
		}
	}

}
