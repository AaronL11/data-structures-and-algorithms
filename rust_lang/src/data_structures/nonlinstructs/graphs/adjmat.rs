pub struct Graph(Vec<Vec<usize>>);

impl Graph {
    fn new(g: &[&[usize]]) -> Self {
        Self(
            g.iter()
                .map(|r| r.iter().map(|x| *x).collect::<Vec<_>>())
                .collect::<Vec<_>>(),
        )
    }
}

pub struct WGraph(Vec<Vec<isize>>);

impl WGraph {
    fn new(g: &[&[isize]]) -> Self {
        Self(
            g.iter()
                .map(|r| r.iter().map(|x| *x).collect::<Vec<_>>())
                .collect::<Vec<_>>(),
        )
    }
}
