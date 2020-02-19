int fib(int n){
    int mod = 1000000007,
        a = 0,
        b = 1,
        c,
        i;
    if (n == 0){
        return a;
    }
    if (n == 1){
        return b;
    }
    for (i = 2; i <= n; i ++){
        c = (a + b) % mod;
        a = b % mod;
        b = c % mod;
    }
    return c;
}