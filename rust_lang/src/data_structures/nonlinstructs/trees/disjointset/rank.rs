pub struct DSU<const N: usize> {
    parent: [usize; N],
    rank: [usize; N],
}

impl<const N: usize> DSU<N> {
    fn new() -> Self {
        Self {
            parent: [0; N],
            rank: [0; N],
        }
    }
    fn make_set(&mut self, n: usize) {
        self.parent[n] = n;
        self.rank[n] = 0;
    }
    fn find(self, v: usize) -> usize {
        if v == self.parent[v] {
            v
        } else {
            self.find(self.parent[v])
        }
    }
    fn union(&mut self, a: usize, b: usize) {
        let a = self.find(a);
        let b = self.find(b);
        if a != b {
            if self.rank[a] < self.rank[b] {
                std::mem::swap(&mut a, &mut b);
            }
            self.parent[b] = a;
            if self.rank[a] == self.rank[b] {
                self.rank[a] += 1;
            }
        }
    }
}
