fn bgcd(a: isize, b: isize) -> isize {
    let (mut u, mut v) = (a, b);
    let mut k = 0;
    while u & 1 == v & 1 {
        u >>= 1;
        v >>= 1;
        k += 1;
    }
    let mut t = if u & 1 == 1 { -v } else { u };
    while t != 0 {
        t >>= 1;
        if t & 1 == 0 {
            continue;
        }
        if t > 0 {
            u = t;
        } else {
            v = -t;
        }
        t = u - v;
    }
    u << k
}
