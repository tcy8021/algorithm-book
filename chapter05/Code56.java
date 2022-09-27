import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Code56 {
    public static void main(String[] args) {
        int N;
        List<Integer> h = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)) {
            N = Integer.parseInt(scanner.nextLine());
            String[] sa = scanner.nextLine().split(" ");
            for (String s : sa) {
                h.add(Integer.parseInt(s));
            }
        }

        List<Integer> dp = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            dp.add(Integer.MAX_VALUE);
        }

        System.out.println(rec(N - 1, h, dp));
    }

    private static int rec(int i, List<Integer> h, List<Integer> dp) {
        if (i == 0) {
            return 0;
        }

        if (dp.get(i) != Integer.MAX_VALUE) {
            return dp.get(i);
        }

        dp.set(i, Math.min(dp.get(i), rec(i - 1, h, dp) + Math.abs(h.get(i) - h.get(i - 1))));
        if (i > 1) {
            dp.set(i, Math.min(dp.get(i), rec(i - 2, h, dp) + Math.abs(h.get(i) - h.get(i - 2))));
        }

        return dp.get(i);
    }
}
