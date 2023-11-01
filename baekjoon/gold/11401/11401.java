import java.util.Scanner;

class Main {
  static long P = 1000000007;
  public static void main(String[] args) {
    long n, k, denom;
    Scanner sc = new Scanner(System.in);
    n = sc.nextLong();
    k = sc.nextLong();

    denom = (factorial(k) * factorial(n - k)) % P;
    System.out.println((factorial(n) * pow(denom, P - 2)) % P);
  }

  public static long factorial(long n) {
    long ret = 1;
    for (long i = 1; i <= n; i++) {
      ret *= i;
      ret %= P;
    }
    return ret;
  }

  public static long pow(long base, long exp) {
    long ret = 1;
    for (long i = exp; i > 0; i /= 2) {
      if (i % 2 == 1) {
        ret *= base;
        ret %= P;
      }
      base *= base;
      base %= P;
    }
    return ret;
  }
}