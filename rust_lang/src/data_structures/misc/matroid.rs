use std::collections::HashSet;

pub struct Matroid<T> {
    pub S: HashSet<T>,
    pub I: HashSet<T>,
}
