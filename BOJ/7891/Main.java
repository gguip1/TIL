import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long n = Integer.parseInt(scan.nextLine());

        for (int i = 0; i < n; i++) {
            String[] inputs = scan.nextLine().split(" ");
            System.out.println(Long.parseLong(inputs[0]) + Long.parseLong(inputs[1]));
        }

        scan.close();
    }
}
