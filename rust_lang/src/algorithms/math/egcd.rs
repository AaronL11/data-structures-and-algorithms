#[allow(dead_code)]
pub fn egcd(a: isize, b: isize) -> (isize, isize, isize) {
    if b == 0 {
        (a, 1, 0)
    } else {
        let (g, x, y) = egcd(a, b);
        (g, y, x - (a / b) * y)
    }
}
