fn catalan(n: usize) -> usize {
    if n <= 1 {
        1
    } else {
        (0..n)
            .map(|i| catalan(i) * catalan(n - i - 1))
            .sum::<usize>()
    }
}

#[allow(non_snake_case)]
fn catalan_dp(n: usize) -> u128 {
    let mut C = vec![0u128; n + 1];
    C[0] = 1;
    C[1] = 1;
    for i in 2..=n {
        C[i] = (0..i).map(|j| C[j] * C[i - j - 1]).sum::<u128>();
    }
    C[n]
}
