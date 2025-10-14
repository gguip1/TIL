import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] input = scan.nextLine().split(" ");

        int r1 = Integer.parseInt(input[0]);
        int s = Integer.parseInt(input[1]);

        System.out.println(s * 2 - r1);
        scan.close();
    }
}
