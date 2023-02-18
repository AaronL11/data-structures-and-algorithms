#[allow(dead_code)]
fn prime_sieve(n: usize) -> Vec<usize> {
    assert!(n >= 2);
    let mut primes = vec![1; n];
    (2..n).for_each(|i| {
        if primes[i] == 1 {
            (i * i..n).step_by(i).for_each(|j| primes[j] = 0)
        }
    });
    (2..n).filter(|&i| primes[i] == 1).collect::<Vec<_>>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn prime_sieve_test1() {
        assert_eq!(prime_sieve(10), [2, 3, 5, 7])
    }
}
