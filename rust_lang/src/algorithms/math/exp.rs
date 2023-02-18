fn exp(b: usize, p: usize, m: usize) -> usize {
    if p == 0 {
        1
    } else if p == 1 {
        b
    } else {
        let mut t = exp(b, p / 2, m);
        t = (t * t) % m;
        if p % 2 == 0 {
            t
        } else {
            (b * t) % m
        }
    }
}
