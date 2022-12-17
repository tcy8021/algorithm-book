import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

// 座標圧縮
public class Ex61 {
    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(12, 43, 7, 15, 9);
        List<Integer> b = new ArrayList<>(a);
        b.sort(Comparator.naturalOrder());

        List<Integer> result = new ArrayList<>();
        for (int e : a) {
            result.add(Collections.binarySearch(b, e));
        }

        System.out.println(result.toString());
    }
}
