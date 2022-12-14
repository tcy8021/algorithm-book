import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Random;

public class Code64 {
    public static void main(String[] args) {
        // prepare
        List<Integer> a = new ArrayList<Integer>();
        List<Integer> b = new ArrayList<Integer>();
        Random rnad = new Random();
        for (int i = 0; i < 10; i++) {
            a.add(rnad.nextInt(100));
            b.add(rnad.nextInt(100));
        }

        // sort
        b.sort(Comparator.naturalOrder());

        // binary search
        int bound = 1;
        int min_val = Integer.MAX_VALUE;
        int ans_a_index = -1;
        int ans_b_index = -1;
        for (int i = 0; i < a.size(); i++) {
            System.out.println("##### i: " + i);
            int left = 0;
            int right = b.size() - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                int target = bound - a.get(i);
                if (b.get(mid) == target) {
                    min_val = bound;
                    ans_a_index = i;
                    ans_b_index = mid;
                    break;
                } else if (b.get(mid) > target) {
                    if (a.get(i) + b.get(mid) < min_val) {
                        min_val = a.get(i) + b.get(mid);
                        ans_a_index = i;
                        ans_b_index = mid;
                    }
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }

        // print
        System.out.println("a: " + a.toString());
        System.out.println("b: " + b.toString());
        System.out.println("bound: " + bound);
        System.out.println("min_val: " + min_val);
        System.out.println("ans_a_index: " + ans_a_index);
        System.out.println("ans_b_index: " + ans_b_index);
    }
}