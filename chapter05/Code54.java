import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Code54 {
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
        dp.set(0, 0);

        for (int i = 0; i < N - 1; i++) {
            dp.set(i + 1, Math.min(dp.get(i + 1), dp.get(i) + Math.abs(h.get(i) - h.get(i + 1))));
            if (i < N - 2) {
                dp.set(i + 2, Math.min(dp.get(i + 2), dp.get(i) + Math.abs(h.get(i + 2) - h.get(i))));
            }
        }

        System.out.println(dp.get(N - 1));
    }
}