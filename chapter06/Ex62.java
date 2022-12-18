import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;

public class Ex62 {
    public static void main(String[] args) {
        // input
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> a = new ArrayList<>(n);
        List<Integer> b = new ArrayList<>(n);
        List<Integer> c = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            a.add(scanner.nextInt());
        }
        for (int i = 0; i < n; i++) {
            b.add(scanner.nextInt());
        }
        for (int i = 0; i < n; i++) {
            c.add(scanner.nextInt());
        }
        scanner.close();

        // 中部のパーツを全探索
        // 上部は[0, b_i)
        // 下部は(b_i, 10^9]
        a.sort(Comparator.naturalOrder());
        c.sort(Comparator.naturalOrder());
        long ans = 0L;
        for (int e : b) {
            ans += (long) lower_bound(a, e) * (n - upper_bound(c, e));
        }

        System.out.println(ans);
    }

    public static int lower_bound(List<Integer> l, int key) {
        int left = 0;
        int right = l.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (l.get(mid) < key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right + 1;
    }

    public static int upper_bound(List<Integer> l, int key) {
        int left = 0;
        int right = l.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (l.get(mid) <= key) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right + 1;
    }
}
