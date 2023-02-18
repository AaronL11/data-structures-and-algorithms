fn stirling2(n: usize, k: usize) -> usize {
    let mut S = vec![vec![0; k + 1]; n + 1];
    for i in 1..=n {
        S[i][1] = 1;
    }
    for i in 1..=n {
        for j in 2..=k {
            S[i][j] = if i == k {
                1
            } else {
                (j * S[i - 1][j] + S[i - 1][j - 1]) % MOD
            };
        }
    }
    S[n][k]
}
