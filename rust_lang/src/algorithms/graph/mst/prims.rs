const INF: usize = 100_000_000;

#[derive(Clone)]
struct Edge {
    w: usize,
    to: isize,
}

impl Edge {
    fn new() -> Self {
        Self { w: INF, to: -1 }
    }
}

fn prims(g: Vec<Vec<usize>>) -> Option<(usize, Vec<(usize, usize)>)> {
    let n = g.len();
    let mut total_weight = 0;
    let mut selected = vec![false; n];
    let mut min_e = vec![Edge::new(); n];
    let mut tree = vec![];
    min_e[0].w = 0;
    for i in 0..n {
        let mut v = -1;
        for j in 0..n {
            if !selected[j] && (v == -1 || min_e[j].w < min_e[v as usize].w) {
                v = j as isize;
            }
        }
        if min_e[v as usize].w == INF {
            return None;
        }
        selected[v as usize] = true;
        total_weight += min_e[v as usize].w;
        if min_e[v as usize].to != -1 {
            tree.push((v as usize, min_e[v as usize].to as usize))
        }
        for to in 0..n {
            if g[v as usize][to] < min_e[to].w {
                min_e[to] = Edge {
                    w: g[v as usize][to],
                    to: v,
                };
            }
        }
    }
    Some((total_weight, tree))
}
