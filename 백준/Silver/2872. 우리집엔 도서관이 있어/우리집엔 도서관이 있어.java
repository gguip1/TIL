import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        List<Integer> a = br.lines()
                .limit(N)
                .map(String::trim)
                .filter(s -> !s.isEmpty())
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        int check_1 = N;
        int check_2 = 0;

        for (int i = a.size() - 1; i >= 0; i--){
            if (check_1 == a.get(i)) {
                check_1--;
                check_2++;
            }
        }

        System.out.println(N - check_2);
    }
}