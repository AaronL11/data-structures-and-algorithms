#[derive(Eq, PartialEq, PartialOrd)]
struct Tree<T>
where
    T: std::hash::Hash + std::cmp::Eq + std::cmp::PartialOrd,
{
    root: Node<T>,
}

#[derive(Eq, PartialEq, PartialOrd, Hash)]
struct Node<T>
where
    T: std::hash::Hash + std::cmp::Eq + std::cmp::PartialOrd,
{
    data: T,
    children: Vec<Node<T>>,
}

impl<T> Node<T>
where
    T: std::hash::Hash + std::cmp::Eq + std::cmp::PartialOrd,
{
    fn new(data: T) -> Self {
        Self {
            data,
            children: vec![],
        }
    }
    fn add_node(&mut self, node: Node<T>) {
        self.children.push(node);
    }
    fn rm_node(&mut self, node: Node<T>) -> Option<Node<T>> {
        for i in 0..self.children.len() {
            if self.children[i] == node {
                return Some(self.children.swap_remove(i));
            }
        }
        None
    }
    fn dfs<F: FnMut(Node<T>) -> T>(&mut self, visit: F) {
        visit(*self);
        for node in self.children {
            node.dfs(visit)
        }
    }
}

impl<T> Tree<T>
where
    T: std::hash::Hash + std::cmp::Eq + std::cmp::PartialOrd,
{
    fn new(data: T) -> Self {
        Self {
            root: Node::new(data),
        }
    }
    fn dfs<F: FnMut(Node<T>) -> T>(&mut self, visit: F) {
        self.root.dfs(visit)
    }
    fn bfs<F: FnMut(Node<T>) -> T>(&mut self, visit: F) {
        let mut q = std::collections::VecDeque::new();
        q.push_back(self.root);
        while let Some(node) = q.pop_front() {
            visit(node);
            for n in node.children {
                visit(n);
                for c in n.children {
                    q.push_back(c);
                }
            }
        }
    }
}
