use std::collections::{BTreeSet, HashMap, VecDeque};

const INF: usize = 10000000;

fn djikstraSet(
    start: usize,
    n: usize,
    G: HashMap<usize, Vec<(usize, usize)>>,
) -> (Vec<usize>, Vec<isize>) {
    let mut d = vec![INF; n + 1];
    let mut p = vec![-1; n + 1];
    d[start] = 0;
    let mut q = BTreeSet::from([(0usize, start)]);
    while !q.is_empty() {
        let top = q.iter().next().unwrap();
        q.remove(&top);
        let (_, v) = top;
        for (u, w) in G[v] {
            if d[*v] + w < d[u] {
                q.remove(&(d[u], u));
                d[u] = d[*v] + w;
                p[u] = *v as isize;
                q.insert((d[u], u));
            }
        }
    }
    (d, p)
}

#[allow(non_snake_case)]
fn djikstraQ(start: usize, n: usize, G: &HashMap<usize, Vec<(usize, usize)>>) -> Vec<usize> {
    let mut q = VecDeque::from([start]);
    let mut d = vec![INF; n];
    d[start] = 0;
    while let Some(v) = q.pop_front() {
        if let Some(edges) = G.get(&v) {
            for (u, w) in edges {
                if d[v] + w < d[*u] {
                    d[*u] = d[v] + *w;
                    q.push_back(*u);
                }
            }
        }
    }
    d
}
