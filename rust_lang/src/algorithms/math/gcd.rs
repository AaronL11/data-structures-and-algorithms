#[allow(dead_code)]
pub fn gcd(a: isize, b: isize) -> isize {
    assert!(a >= b);
    match a % b {
        0 => b,
        r @ _ => gcd(b, r),
    }
}
