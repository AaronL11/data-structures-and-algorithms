use std::collections::HashMap;
use std::hash::Hash;

pub struct Graph<T: Hash + Eq + PartialOrd + Ord + Default>(pub HashMap<T, Vec<T>>);

impl<T> Graph<T>
where
    T: Hash + Eq + PartialOrd + Ord + Default,
{
    fn new(m: &[(T, T)]) -> Self {
        let mut g: HashMap<T, Vec<T>> = HashMap::new();
        for (k, v) in m {
            if let Some(nodes) = g.get_mut(&k) {
                nodes.push(*v);
            } else {
                g.insert(*k, vec![*v]);
            }
        }
        Self(g)
    }
}

pub struct WGraph<T: Hash + Eq + PartialOrd + Ord + Default>(pub HashMap<T, Vec<(T, isize)>>);

impl<T> WGraph<T>
where
    T: Hash + Eq + PartialOrd + Ord + Default,
{
    fn new<I: IntoIterator<Item = (T, T, isize)>>(m: I) -> Self {
        let mut g: HashMap<T, Vec<(T, isize)>> = HashMap::new();
        for (k, v, w) in m {
            if let Some(nodes) = g.get_mut(&k) {
                nodes.push((v, w));
            } else {
                g.insert(k, vec![(v, w)]);
            }
        }
        Self(g)
    }
}
