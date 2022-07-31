import java.util.Scanner;

public class tax {
    public static void main(String args[]) {
        Scanner obj = new Scanner(System.in);
        long t;
        String n1 = "55,00,000";

        String x = n1.replaceAll("[^a-zA-Z0-9]", "");
        long n = Integer.parseInt(x);
        // System.out.println(n);
        if (n >= 0 && n < 250000) {
            t = n;
        } else if (n >= 250000 && n < 500000) {
            t = n * 5 / 100;
        } else if (n >= 500000 && n < 750000) {
            t = n * 10 / 100;
        } else if (n >= 750000 && n < 1000000) {
            t = n * 15 / 100;
        } else if (n >= 1000000 && n < 1250000) {
            t = n * 20 / 100;
        } else if (n >= 1250000 && n < 150000) {
            t = n * 25 / 100;
        } else {
            t = n * 30 / 100;
        }
        if (n == 5000000) {
            t = t + n * 10 / 100;
        } else if (n == 10000000) {
            t = t + n * 15 / 100;
        } else if (n == 20000000) {
            t = t + n * 25 / 100;
        } else if (n == 50000000) {
            t = t + n * 37 / 100;
        }
        t = t + n * 4 / 100;

        String res = String.valueOf(t);
        String res1 = new String();
        // 1,04,000

        // 000,40,1

        int len = res.length();
        len -= 1;

        for (int i = len, count = 0; i >= 0; i--, count++) {

            if (count % 2 == 0 && count > 0) {
                // System.out.println("Count => " + count);
                res1 += res.charAt(i);
                res1 += ",";
            } else {
                res1 += res.charAt(i);
            }

        }
        // String res1[]= res.split(",",2);
        // for ( string : res1) {

        // }
        StringBuilder input1 = new StringBuilder();

        // append a string into StringBuilder input1
        input1.append(res1);

        // reverse StringBuilder input1
        input1.reverse();
        System.out.println(input1);
    }
}
