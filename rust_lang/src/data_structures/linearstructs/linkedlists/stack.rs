use std::Rc;

struct Node<T> {}

type Stack = Option<Rc<Node<T>>>;
