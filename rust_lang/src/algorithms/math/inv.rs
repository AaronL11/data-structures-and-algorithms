use super::egcd::egcd;

#[allow(dead_code)]
pub fn inverse(b: isize, n: isize) -> Option<isize> {
    let (g, _, y) = egcd(b, n);
    if g != 1 {
        None
    } else {
        Some(y)
    }
}
