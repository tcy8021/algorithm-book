import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Code55 {
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

        System.out.println(rec(N - 1, h));
    }

    private static int rec(int i, List<Integer> h) {
        if (i == 0) {
            return 0;
        }

        int result = Integer.MAX_VALUE;
        result = Math.min(result, rec(i - 1, h) + Math.abs(h.get(i) - h.get(i - 1)));
        if (i > 1) {
            result = Math.min(result, rec(i - 2, h) + Math.abs(h.get(i) - h.get(i - 2)));
        }

        return result;
    }
}
