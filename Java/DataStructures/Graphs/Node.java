package Java.DataStructures.Graphs;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.Collection;
import java.util.Optional;
import java.util.stream.Collector;
import java.util.stream.Collectors;

class Tree<T> {

}


class Node<T> {
    private T leaf;
    private ArrayList<Node<T>> branches;

    public Node(T data) {
        this.leaf = data;
        this.branches = null;
    }

    public <C extends Collection<T>> Node(T data, C branches) {
        this.leaf = data;
        this.branches = (ArrayList<Node<T>>) branches.stream()
                                                     .map(leaf -> new Node<T>(leaf))
                                                     .collect(Collectors.toList());
    }

    public void addNode(T data) {
        if (this.branches != null) {
            this.branches.add(new Node<T>(data));
        } else {
            this.branches = new ArrayList<Node<T>>();
            this.branches.add(new Node<T>(data));
        }
    }

    public Optional<Node<T>> getNode(T name) {
        return this.branches.stream().filter(leaf -> leaf.getLeaf()==name).reduce((i,x) -> i);
    }

    public void addBranch(T... branches) {
        if (this.branches != null) {
            this.branches.addAll(Arrays.stream(branches)
                                       .map(leaf -> new Node<T>(leaf))
                                       .collect(Collectors.toList()));
        } else {
            
            this.branches = (ArrayList<Node<T>>) Arrays.stream(branches)
                                                       .map(leaf -> new Node<T>(leaf))
                                                       .collect(Collectors.toList());
        }
    }

    public T getLeaf() {
        return this.leaf;
    }

    public boolean checkDFS(T find) {
        if (find == this.leaf) {
            return true;
        } else if (this.branches == null) {
            return false;
        } else {
            boolean flag = false;
            for (Node<T> leaf : this.branches) {
                flag = leaf.checkDFS(find);
                if (flag) { break; }
            }
            return flag;
        }
    }

    public boolean checkBFS(T find) {
        if (find == this.leaf) {
            return true;
        } else if (this.branches == null) {
            return false;
        } else {
            boolean flag = false;
            for (Node<T> leaf : this.branches) {
                flag = leaf.getLeaf() == find;
                if (flag) { break; }
            }
            if (flag) {
                return true;
            } else {
                for (Node<T> leaf : this.branches) {
                    flag = leaf.checkBFS(find);
                    if (flag) { break; }
                }
                return flag;
            }
        }
    }

    @Override
    public String toString() {
        return new StringBuilder().append("\s{\s")
                                  .append(leaf)
                                  .append("\s:")
                                  .append("\s[\s")
                                  .append(branches)
                                  .append("\s]\s")
                                  .append("\s}")
                                  .toString();
    }

    public static void main(String[] args) {
        Node<Integer> node = new Node<Integer>(0);

        node.addNode(1);
        node.addNode(2);
        node.addNode(2);
        node.addNode(3);
        int n = node.getLeaf();

        // Integer[] leafs = node.getNode(2);

        var nod = node.getNode(2).get();
        nod.addBranch(0,1,2,3,4);
        System.out.println(n);
        System.out.println(nod);
        System.out.println(node.getNode(2));
        System.out.println(node);
        System.out.println(node.checkDFS(4));
        System.out.println(node.checkBFS(4));
    }
}
