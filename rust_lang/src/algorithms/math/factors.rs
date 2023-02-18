#[allow(dead_code)]
fn factor_sieve(n: usize) -> Vec<usize> {
    let mut factors = vec![2; n + 1];
    factors[1] = 1;
    (2..=n).for_each(|i| (i + i..=n).step_by(i).for_each(|j| factors[j] += 1));
    factors
}
