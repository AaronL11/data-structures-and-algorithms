use crate::data_structures::nonlinstructs::graphs::adj::Graph;
use std::{collections::HashSet, hash::Hash};

fn dfs<T, F: FnMut(&T) -> T>(start: T, G: Graph<T>, visit: F)
where
    T: Hash + Eq + PartialOrd + Ord,
{
    let mut stack = vec![];
    let mut visited = HashSet::new();
    stack.push(start);
    while let Some(item) = stack.pop() {
        if visited.contains(&item) {
            continue;
        }
        visit(&item);
        visited.insert(item);
        if let Some(nodes) = G.0.get(&item) {
            for node in nodes {
                stack.push(*node);
            }
        }
    }
}
