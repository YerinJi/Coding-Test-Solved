import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int result1 = 0;
		int result2;
		if(B!=C && (A==B || A==C) )
			System.out.println(1000 + A*100);
		else if(A!=B && (A==C || B==C))
			System.out.println(1000 + C*100);
		else if(A==B && B==C)
			System.out.println(10000 + A*1000);
		else {
			result1 = (A>B?A:B);
			result2 = (result1>C? result1:C);
			System.out.println(result2*100);
		}
		
	}

}