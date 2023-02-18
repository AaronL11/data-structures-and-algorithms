fn modexp(a: usize, b: usize, m: usize) -> usize {
    if m == 1 {
        0
    } else {
        let mut c = 1;
        for _ in 0..b {
            c = (c * a) % m;
        }
        c
    }
}
