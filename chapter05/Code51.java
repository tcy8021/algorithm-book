import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Code51 {
    public static void main(String[] args) {
        int N;
        List<Integer> h = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)) {
            N = Integer.parseInt(scanner.nextLine());
            String[] s = scanner.nextLine().split(" ");
            for (int i = 0; i < s.length; i++) {
                h.add(Integer.parseInt(s[i]));
            }
        }

        int dp[] = new int[N];
        for (int i = 0; i < N; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        dp[0] = 0;
        for (int i = 1; i < N; i++) {
            dp[i] = Math.min(dp[i], dp[i - 1] + Math.abs(h.get(i) - h.get(i - 1)));
            if (i > 1) {
                dp[i] = Math.min(dp[i], dp[i - 2] + Math.abs(h.get(i) - h.get(i - 2)));
            }
        }

        System.out.println(dp[N - 1]);
    }
}