fn choose(n: usize, k: usize) -> usize {
    let mut C = vec![vec![1; k + 1]; n + 1];
    for i in 1..=n {
        for j in 1..=cmp::min(i, k) {
            C[i][j] = if i == j {
                1
            } else {
                C[i - 1][j - 1] + C[i - 1][j]
            };
        }
    }
    C[n][k]
}
