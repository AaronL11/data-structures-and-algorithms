use crate::data_structures::misc::matroid::Matroid;
use std::collections::HashSet;
use std::hash::Hash;

pub fn greedy<T, O, F>(M: Matroid<T>, w: F) -> HashSet<T>
where
    T: Hash + Eq + Clone,
    O: PartialOrd + Ord,
    F: Fn(&T) -> O,
{
    let mut A = HashSet::new();
    let mut S: Vec<_> = M.S.iter().collect::<_>();
    S.sort_by(|a, b| w(&b).cmp(&w(&a)));
    for x in S {
        let x = HashSet::from([*x]);
        if (&A & &x).is_subset(&M.I) {
            A = &A & &x;
        }
    }
    A
}
