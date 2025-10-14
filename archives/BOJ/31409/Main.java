import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = Integer.parseInt(scan.nextLine());
        int[] bs = Arrays.stream(scan.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int count = 0;
        int current;
        boolean check;

        for (int i = 0; i < N; i++) {
            check = false;
            current = bs[i];
            for (int j = 0; j < N; j++) {
                if (current == i + 1) {
                    if (j == 0) {
                        continue;
                    } else {
                        check = true;
                        break;
                    }
                }
                current = bs[current - 1];
            }
            if (!check) {
                bs[i] = (i + 1) % N + 1;
                count++;
            }
        }

        System.out.println(count);
        for (int b : bs) {
            System.out.print(b + " ");
        }

        scan.close();
    }
}