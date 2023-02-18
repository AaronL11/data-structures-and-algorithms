#![allow(dead_code)]
use super::egcd::egcd;

pub fn crt2(a: isize, n: isize, b: isize, m: isize) -> Option<(isize, isize)> {
    let K = n * m;
    let (g, x, y) = egcd(n, m);
    if a % g == b % g {
        Some((((a * m * y + b * n * x) / g) % K, K))
    } else {
        None
    }
}

pub fn crtn(nums: &[(isize, isize)]) -> Option<(isize, isize)> {
    if nums.is_empty() {
        None
    } else if nums.len() == 1 {
        Some(nums[0])
    } else {
        let [(a, n), (b, m)] = nums[..2];
        crt2(a, n, b, m) {
            crtn(&nums[2..])
        }
    }
}
