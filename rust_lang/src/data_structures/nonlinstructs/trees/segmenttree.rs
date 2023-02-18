#![allow(dead_code)]
use std::cmp;

struct SegmentTree<'a> {
    tree: Vec<usize>,
    data: &'a [usize],
}

impl<'a> SegmentTree<'a> {
    fn new(a: &'a [usize]) -> Self {
        let mut r = Self {
            tree: vec![0; 4 * a.len()],
            data: a,
        };
        r.build(1, 0, a.len() - 1);
        r
    }
    fn build(&mut self, v: usize, tl: usize, tr: usize) {
        if tl == tr {
            self.tree[v] = self.data[tl]
        } else {
            let tm = (tl + tr) / 2;
            self.build(v * 2, tl, tm);
            self.build(v * 2 + 1, tm + 1, tr);
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
        }
    }
    fn sum(&mut self, v: usize, tl: usize, tr: usize, l: usize, r: usize) -> usize {
        if l > r {
            0
        } else if l == tl && r == tr {
            self.tree[v]
        } else {
            let tm = (tl + tr) / 2;
            self.sum(v * 2, tl, tm, l, cmp::min(r, tm))
                + self.sum(v * 2 + 1, tm + 1, tr, cmp::max(l, tm + 1), r)
        }
    }
    fn update(&mut self, v: usize, tl: usize, tr: usize, pos: usize, nv: usize) {
        if tl == tr {
            self.tree[v] = nv
        } else {
            let tm = (tl + tr) / 2;
            if pos <= tm {
                self.update(v * 2, tl, tm, pos, nv)
            } else {
                self.update(v * 2 + 1, tm + 1, tr, pos, nv)
            }
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
        }
    }
    fn idx(&self, i: usize) -> usize {
        self.tree[i]
    }
}
