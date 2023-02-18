use std::cmp;

const INF: isize = 1_000_000;

pub fn bellman_ford(
    start: usize,
    n: usize,
    m: usize,
    E: &Vec<(usize, usize, isize)>,
) -> Vec<isize> {
    let mut d = vec![INF; n];
    d[start] = 0;
    for i in 0..n - 1 {
        for j in 0..m {
            let (u, v, w) = E[j];
            if d[u] < INF {
                d[v] = cmp::min(d[v], d[u] + w);
            }
        }
    }
    d
}

pub fn bellman_ford_with_cycle(
    start: usize,
    n: usize,
    m: usize,
    E: &Vec<(usize, usize, isize)>,
) -> (Vec<isize>, Vec<bool>) {
    let mut d = vec![INF; n];
    let mut cyc = vec![false; n];
    d[start] = 0;
    for _ in 0..n - 1 {
        for j in 0..m {
            let (u, v, w) = E[j];
            if d[u] < INF {
                d[v] = cmp::min(d[v], d[u] + w);
            }
        }
    }
    let mut ch = true;
    while ch {
        ch = false;
        for j in 0..m {
            let (u, v, w) = E[j];
            if d[u] < INF {
                if d[u] + w < d[v] && !cyc[v] {
                    d[v] = -INF;
                    cyc[v] = true;
                    ch = true;
                }
            }
        }
    }
    (d, cyc)
}
