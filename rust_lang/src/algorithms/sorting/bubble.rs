
#[allow(dead_code)]
pub fn bubble_sort<T: PartialOrd + Copy>(array: &mut [T]) {
    let n = array.len();
    for _ in 0..n {
        for j in 0..n-1 {
            if array[j] > array[j+1] {
                let temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::bubble_sort;

    #[test]
    fn test_bubble1() {
        let mut array = [1,2,4,3,5];
        bubble_sort(&mut array);
        assert_eq!(
            array,
            [1,2,3,4,5]
            )
    }

    #[test]
    fn test_bubble2() {
        let mut array = [9,3,6,1,4,2];
        bubble_sort(&mut array);
        assert_eq!(
            array,
            [1,2,3,4,6,9]
            )
    }
}

