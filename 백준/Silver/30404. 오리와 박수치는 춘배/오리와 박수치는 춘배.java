import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] inputs;

        inputs = scan.nextLine().split(" ");

        int n = Integer.parseInt(inputs[0]);
        int k = Integer.parseInt(inputs[1]);

        List<Integer> xs = Arrays.stream(scan.nextLine().split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        int answer = 0;
        int time = 0;

        for (int x : xs) {
            if (time < x) {
                time = x + k;
                answer += 1;
            }
        }

        System.out.println(answer);
        scan.close();
    }
}
