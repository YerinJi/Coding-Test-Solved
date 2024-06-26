import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int subject = sc.nextInt();
		double arr[] = new double[subject];
		double avg;
		double sum = 0;
		for(int i=0; i< arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		double max = arr[0];
		for(int i=1; i< arr.length; i++) {
			if(max < arr[i]) {
				max = arr[i];
			}
		}
		for(int i=0; i< arr.length; i++) {
			arr[i] = (arr[i]/max)*100;
			sum += arr[i];
		}
		avg = sum/subject;
		System.out.println(avg);
	}

}
