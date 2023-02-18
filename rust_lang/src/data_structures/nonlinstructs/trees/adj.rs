struct Tree<T: Default> {
    root: usize,
    arena: Vec<(T, Vec<usize>)>,
}

impl<T> Tree<T>
where
    T: Default,
{
    fn new(v: &(usize, usize, T)) -> Self {
        let root = 0;
        let mut arena = vec![];
        for (i, j, w) in v {}
        Self { root, arena }
    }
}
