import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int bucket = sc.nextInt();
		int change = sc.nextInt();
		int arr[] = new int[bucket];
		for(int i= 0; i< arr.length; i++)
			arr[i] = i+1;
		for(int i=1; i<= change; i++ ) {
			int one = sc.nextInt()-1;
			int two = sc.nextInt()-1;
			while(one < two) {
				int tmp = arr[one];
				arr[one] = arr[two];
				arr[two] = tmp;
				one++;
				two--;
			}
		}
		for(int i=0; i< arr.length; i++) {
			System.out.print(arr[i] +" ");
		}
	}

}