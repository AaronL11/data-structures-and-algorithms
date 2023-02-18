pub struct DSU<const N: usize> {
    parent: [usize; N],
}

impl<const N: usize> DSU<N> {
    fn new() -> Self {
        Self { parent: [0; N] }
    }
    fn make_set(&mut self, n: usize) {
        self.parent[n] = n;
    }
    fn find(self, v: usize) -> usize {
        if v == self.parent[v] {
            v
        } else {
            self.parent[v] = self.find(self.parent[v]);
            self.parent[v]
        }
    }
    fn union(&mut self, a: usize, b: usize) {
        let a = self.find(a);
        let b = self.find(b);
        if a != b {
            self.parent[b] = a;
        }
    }
}
