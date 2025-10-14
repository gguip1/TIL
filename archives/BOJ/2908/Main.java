import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] input = scan.nextLine().split(" ");

        String a = input[0];
        String b = input[1];

        String reverseA = "";
        String reverseB = "";

        for (int i = 2; i >= 0; i--) {
            reverseA += a.charAt(i);
            reverseB += b.charAt(i);
        }

        if (Integer.parseInt(reverseA) > Integer.parseInt(reverseB)) {
            System.out.println(reverseA);
        } else {
            System.out.println(reverseB);
        }

        scan.close();
    }
}
