import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = Integer.parseInt(scan.nextLine().trim());
        String[] input;

        for (int i = 0; i < t; i++) {
            input = scan.nextLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[0]);

            ArrayList<ArrayList<Integer>> prize = new ArrayList<ArrayList<Integer>>();

            for (int j = 0; j < n; j++) {
                input = scan.nextLine().split(" ");
                ArrayList<Integer> emptyList = new ArrayList<Integer>();
                for (int z = 0; z < Integer.parseInt(input[0]) + 2; z++) {
                    emptyList.add(Integer.parseInt(input[z]));
                }
                prize.add(emptyList);
            }

            input = scan.nextLine().split(" ");
            int[] stickers = new int[m];

            for (int j = 0; j < m; j++) {
                stickers[j] = Integer.parseInt(input[j]);
            }

            int answer = 0;
            prize.sort(Comparator.comparingDouble(a -> a.get(0) / a.get(a.size() - 1)));

            for (int j = n; 0 < j; j--) {
                int[] v = new int[prize.get(j).get(0)];
                for (int z = 0; z < prize.get(j).get(0); z++) {
                    v[z] = prize.get(j).get(z + 1);
                }

            }
        }

        scan.close();
    }
}
