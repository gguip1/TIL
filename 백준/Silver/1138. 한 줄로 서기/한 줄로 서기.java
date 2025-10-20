import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String[] inputs;
        inputs = scanner.nextLine().split(" ");
        int N = Integer.parseInt(inputs[0]);

        inputs = scanner.nextLine().split(" ");
        int[] lefts = new int[N];
        for (int i = 0; i < N; i++){
            lefts[i] = Integer.parseInt(inputs[i]);
        }

        int[] answer = new int[N];

        for (int i = 0; i < N; i++){
            int index = -1;
            for (int j = 0; j < N; j++){
                if (answer[j] == 0){
                    index += 1;
                }

                if (index == lefts[i]){
                    answer[j] = i + 1;
                    break;
                }
            }
        }

        for (int ans : answer){
            System.out.print(ans + " ");
        }

        scanner.close();
    }
}
