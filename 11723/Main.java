import java.io.*;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int M = Integer.parseInt(br.readLine());

        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < M; i++) {
            String Q = br.readLine();

            if (Q.equals("all")) {
                for (int j = 1; j <= 20; j++) {
                    set.add(j);
                }
            } else if (Q.equals("empty")) {
                set.clear();
            } else {
                String[] query = Q.split(" ");
                int val = Integer.parseInt(query[1]);
                if (query[0].equals("add")) {
                    set.add(val);
                } else if (query[0].equals("remove")) {
                    set.remove(val);
                } else if (query[0].equals("toggle")) {
                    if (set.contains(val)) {
                        set.remove(val);
                    } else {
                        set.add(val);
                    }
                } else if (query[0].equals("check")) {
                    if (set.contains(val)) {
                        bw.write(1 + "\n");
                    } else {
                        bw.write(0 + "\n");
                    }
                }
            }
        }
        bw.flush();
        bw.close();
    }
}