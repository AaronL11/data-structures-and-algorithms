pub struct DSU<const N: usize> {
    parent: [usize; N],
    size: [usize; N],
}

impl<const N: usize> DSU<N> {
    pub fn new() -> Self {
        Self {
            parent: [0; N],
            size: [0; N],
        }
    }
    pub fn make_set(&mut self, n: usize) {
        self.parent[n] = n;
        self.size[n] = 1;
    }
    pub fn find(self, v: usize) -> usize {
        if v == self.parent[v] {
            v
        } else {
            self.parent[v] = self.find(self.parent[v]);
            self.parent[v]
        }
    }
    pub fn union(&mut self, a: usize, b: usize) {
        let a = self.find(a);
        let b = self.find(b);
        if a != b {
            if self.size[a] < self.size[b] {
                std::mem::swap(&mut a, &mut b);
            }
            self.parent[b] = a;
        }
    }
}
