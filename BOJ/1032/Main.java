import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        String[] dirs = new String[n];

        for(int i = 0; i < n; i++){
            dirs[i] = scan.next();
        }

        String result = dirs[0];

        for(int i = 1; i < n; i++){
            for(int j = 0; j < result.length(); j++){
                if(result.charAt(j) != dirs[i].charAt(j)){
                    result = result.substring(0, j) + "?" + result.substring(j + 1);
                }
            }
        }

        System.out.println(result);
    }
}