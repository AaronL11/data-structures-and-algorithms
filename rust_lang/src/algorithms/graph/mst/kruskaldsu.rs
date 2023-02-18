use crate::data_structures::nonlinstructs::trees::disjointset::generic::DSU;

fn kruskal(g: Vec<Vec<usize>>) -> (usize, Vec<(usize, usize)>) {
    let n = g.len();
    let mut total_weight = 0;
    let mut tree = Vec::with_capacity(n);
    let mut edges = Vec::with_capacity(n * n);
    let mut dsu = DSU::new();
    for i in 0..n {
        dsu.make_set(i);
        for j in i + 1..n {
            edges[i + j] = (i, j, g[i][j]);
        }
    }
    edges.sort_by(|(_, _, a), (_, _, b)| a.cmp(&b));
    for (u, v, w) in edges {
        if dsu.find(u) != dsu.find(v) {
            total_weight += w;
            tree.push((u, v));
            dsu.union(u, v)
        }
    }
    (total_weight, tree)
}
