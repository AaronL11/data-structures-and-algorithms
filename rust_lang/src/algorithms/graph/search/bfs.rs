use crate::data_structures::nonlinstructs::graphs::adj::Graph;
use std::{
    collections::{HashSet, VecDeque},
    hash::Hash,
};

fn bfs<T, F: FnMut(&T) -> T>(start: T, G: Graph<T>, visit: F)
where
    T: Hash + Eq + PartialOrd + Ord,
{
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();
    queue.push_back(start);
    while let Some(item) = queue.pop_front() {
        if visited.contains(&item) {
            continue;
        }
        visit(&item);
        visited.insert(item);
        if let Some(nodes) = G.0.get(&item) {
            for node in nodes {
                queue.push_back(*node);
            }
        }
    }
}
