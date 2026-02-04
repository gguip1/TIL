import java.io.*;
import java.util.*;

public class Main {
    static String sentence;
    static int N;
    static String[] words;

    static String decrypt(String sentence) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if (c >= 'a' && c <= 'z') result.append((char)('a' + (c - 'a' + 1) % 26));
            else result.append(c);
        }

        return result.toString();
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        sentence = br.readLine();
        N = Integer.parseInt(br.readLine());
        words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        for (int i = 0; i < 26; i++) {
            for (String word : words) {
                if (sentence.contains(word)) {
                    System.out.println(sentence);
                    System.exit(0);
                }
            }
            sentence = decrypt(sentence);
        }
    }
}
