import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] arr = scan.nextLine().split(" ");
        int n = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);

        int[] answer = new int[n];

        for (int i = 0; i < m; i++) {
            arr = scan.nextLine().split(" ");
            for (int j = Integer.parseInt(arr[0]) - 1; j < Integer.parseInt(arr[1]); j++) {
                answer[j] = Integer.parseInt(arr[2]);
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(answer[i] + " ");
        }
        scan.close();
    }
}
