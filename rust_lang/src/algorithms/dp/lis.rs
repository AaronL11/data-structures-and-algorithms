fn LIS(A: &Vec<usize>) -> usize {
    let n = A.len();
    let mut LIS = vec![0; n + 1];
    LIS[0] = 0;
    for i in 1..=n {
        LIS[i] = 1
            + (0..i - 1)
                .filter_map(|k| {
                    if A[k] < A[i - 1] {
                        Some(LIS[k + 1])
                    } else {
                        None
                    }
                })
                .max()
                .unwrap_or(0);
    }
    LIS[n]
}
