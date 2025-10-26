import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputs;

        inputs = scanner.nextLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        List<ArrayList<Boolean>> n_creatures = new ArrayList<ArrayList<Boolean>>();
        List<ArrayList<Boolean>> p_creatures = new ArrayList<ArrayList<Boolean>>();

        for (int i = 0; i < N; i++) {
            n_creatures.add(new ArrayList<Boolean>(List.of(false, true)));
        }

        for (int i = 0; i < N; i++) {
            p_creatures.add(new ArrayList<Boolean>(List.of(true, false)));
        }

        for (int i = 0; i < M; i++) {
            inputs = scanner.nextLine().split(" ");
            int a = Integer.parseInt(inputs[0]);
            String b = inputs[1];
            int c = Integer.parseInt(inputs[2]);

            n_creatures.get(a - 1).set(b.equals("P") ? 0 : 1, c == 0 ? false : true);
            p_creatures.get(a - 1).set(b.equals("P") ? 0 : 1, c == 0 ? false : true);
        }

        int minV = 0;
        int maxV = 0;

        for (ArrayList<Boolean> creature : n_creatures) {
            if (creature.get(0) && !creature.get(1)) {
                minV += 1;
            }
        }

        for (ArrayList<Boolean> creature : p_creatures) {
            if (creature.get(0) && !creature.get(1)) {
                maxV += 1;
            }
        }

        System.out.println(minV + " " + maxV);

        scanner.close();
    }
}