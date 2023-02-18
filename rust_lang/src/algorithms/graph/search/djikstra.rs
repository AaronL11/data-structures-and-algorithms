const INF: usize = 10000000;

fn djikstra(s: usize, G: Vec<Vec<(usize, usize)>>) -> (Vec<usize>, Vec<isize>) {
    let n = G.len();
    let mut d = vec![INF; n + 1];
    let mut p = vec![-1; n + 1];
    let mut u = vec![false; n + 1];
    d[s] = 0;
    for _ in 0..n {
        let mut v = 0;
        for j in 1..=n {
            if !u[j] && (d[j] < d[v]) {
                v = j;
            }
        }
        if d[v] == INF {
            break;
        }
        u[v] = true;
        for (to, len) in G[v] {
            if d[v] + len < d[to] {
                d[to] = d[v] + len;
                p[to] = v as isize;
            }
        }
    }
    (d, p)
}

fn restore_path(p: Vec<isize>, s: usize, t: usize) -> Vec<isize> {
    let mut path = vec![];
    let mut v = t;
    while v != s {
        path.push(v as isize);
        v = p[v] as usize;
    }
    path.push(s as isize);
    path.reverse();
    path
}
