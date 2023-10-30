import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        long t, n, m, r, i, j;

        Scanner sc = new Scanner(System.in);
        t = sc.nextLong();

        for (i = 0; i < t; i++) {
            n = sc.nextLong();
            m = sc.nextLong();
            r = 1;
            for (j = 0; j < n; j++) {
                r *= (m - j);
                r /= (j + 1);
            }
            System.out.println(r);
        }
    }
}