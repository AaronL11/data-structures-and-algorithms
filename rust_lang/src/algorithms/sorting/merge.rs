#[allow(dead_code)]
pub fn merge_sort<T: PartialOrd + Copy>(array: &mut [T], start: usize, end: usize) {
    if start == end {
        return;
    } else {
        let mid = (start + end) / 2;
        merge_sort(array, start, mid);
        merge_sort(array, mid + 1, start);
    }
}

#[cfg(test)]
mod tests {
    use super::merge_sort;

    #[test]
    fn test_merge1() {
        let array = [15, 7, 10, 5, 1, 2];
        merge_sort(&mut array, 0, array.len());
        assert_eq!(array, [1, 2, 5, 7, 10, 15])
    }

    #[test]
    fn test_merge2() {
        let array = [90, 24, 16, 38, 73, 17, 382, 25];
        merge_sort(&mut array, 0, array.len());
        assert_eq!(array, [16, 17, 24, 25, 38, 73, 90, 382])
    }
}
