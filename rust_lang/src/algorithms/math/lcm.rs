use super::gcd::gcd;

#[allow(dead_code)]
fn lcm(a: isize, b: isize) -> isize {
    a * (b / gcd(a, b))
}
