use std::{collections::HashMap, hash::Hash};

pub struct DSU<T>
where
    T: Hash + Eq + Clone,
{
    parent: HashMap<T, T>,
    size: HashMap<T, usize>,
}

impl<T> DSU<T>
where
    T: Hash + Eq + Clone,
{
    pub fn new(n: usize) -> Self {
        Self {
            parent: HashMap::with_capacity(n),
            size: HashMap::with_capacity(n),
        }
    }
    pub fn make_set(&mut self, n: T) {
        self.parent.insert(n, n);
        self.size.insert(n, 1);
    }
    pub fn find(self, v: T) -> T {
        if let Some(p) = self.parent.get_mut(&v) {
            if v == *p {
                v
            } else {
                *p = self.find(*p);
                *p
            }
        } else {
            self.make_set(v);
            v
        }
    }
    pub fn union(&mut self, a: T, b: T) {
        let a = self.find(a);
        let b = self.find(b);
        if a != b {
            if self.size[&a] < self.size[&b] {
                std::mem::swap(&mut a, &mut b);
            }
            self.parent[&b] = a;
        }
    }
}
