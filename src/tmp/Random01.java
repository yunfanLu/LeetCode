package tmp;

import java.math.BigDecimal;

public class Random01 {

    static BigDecimal ONE = new BigDecimal("1.0");
    static BigDecimal ZERO = new BigDecimal("0.0");
    static BigDecimal TWO = new BigDecimal("2.0");

    static BigDecimal foo(BigDecimal x){
        if (x.compareTo(ONE) < 1 && x.compareTo(ZERO) > -1){
            BigDecimal t = x.multiply(TWO);
            if (t.compareTo(ONE) == 1) {
                return t.subtract(ONE);
            }else{
                return t;
            }
        }
        return ZERO;
    }

    static String bar(BigDecimal x){
        String r = x.toString();
        return r.substring(0,Math.min(r.length(), 13));
    }

    public static void main(String[] args){
        BigDecimal a = new BigDecimal("0.10000000001");
        BigDecimal b = new BigDecimal("0.1000000000000000001");
        for(int i = 0; i < 100; i ++){
            a = foo(a);
            b = foo(b);
            System.out.println(i + "\t\t: " + bar(a) + "\t\t" + bar(b) + "\t" + a.subtract(b).abs());
        }
    }
}
