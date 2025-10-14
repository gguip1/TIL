
import java.util.AbstractMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] inputs = scan.nextLine().split(":");
        int minutes = Integer.parseInt(inputs[0]);
        int seconds = Integer.parseInt(inputs[1]) + minutes * 60;

        LinkedList<Map.Entry<int[], Boolean>> stack = new LinkedList<Map.Entry<int[], Boolean>>();
        stack.add(new AbstractMap.SimpleEntry<int[], Boolean>(new int[] { 0, 0 }, false));
        while (stack.size() > 0) {
            Map.Entry<int[], Boolean> node = stack.pop();

            int[] deltas = { 10, 30, 60, 600 };
            for (int delta : deltas) {
                if (delta == 30) {
                    if (!node.getValue()) {
                        if (node.getKey()[0] == 0) {
                            stack.add(new AbstractMap.SimpleEntry<int[], Boolean>(
                                    new int[] { node.getKey()[0] + delta, node.getKey()[1] + 1 }, true));
                        } else {
                            stack.add(new AbstractMap.SimpleEntry<int[], Boolean>(
                                    new int[] { node.getKey()[0], node.getKey()[1] + 1 }, true));
                        }
                    } else {
                        stack.add(new AbstractMap.SimpleEntry<int[], Boolean>(
                                new int[] { node.getKey()[0] + delta, node.getKey()[1] + 1 }, true));
                    }
                } else {
                    stack.add(new AbstractMap.SimpleEntry<int[], Boolean>(
                            new int[] { node.getKey()[0] + delta, node.getKey()[1] + 1 }, node.getValue()));
                }
            }
        }

        scan.close();
    }
}
