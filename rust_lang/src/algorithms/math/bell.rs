fn Bell(n: usize) -> usize {
    let mut dp = vec![vec![0; n + 1]; n + 1];
    for i in 1..=n {
        for j in 0..=k {
            dp[i][j] = if i == j {
                0
            } else if i == 0 || j == 0 {
                0
            } else {
                j * dp[i - 1][j] + dp[i - 1][j - 1]
            };
        }
    }
    (0..=n).map(|k| dp[n][k]).sum::<Uint>();
}
