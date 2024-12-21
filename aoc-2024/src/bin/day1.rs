use std::collections::HashMap;
use std::collections::hash_map::Entry;
use std::fs::read_to_string;

fn one(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut left = left.clone();
    let mut right = right.clone();

    left.sort();
    right.sort();

    let mut counter = 0;
    for (index, l_val) in left.iter().enumerate() {
        let diff = l_val - right[index];
        counter += diff.abs();
    }

    counter
}

fn two(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    let mut similarity_score = 0;
    let mut counts: HashMap<i32, i32> = HashMap::new();
    for r_val in right.iter() {
        match counts.entry(*r_val) {
            Entry::Occupied(mut e) => {
                let curr = e.get();
                let val = e.insert(curr + 1);
                val
            }
            Entry::Vacant(e) => *e.insert(1),
        };
    }

    for l_val in left.iter() {
        let r_count = counts.entry(*l_val).or_default();
        similarity_score += *l_val * *r_count;
    }

    similarity_score
}

fn main() {
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    for line in read_to_string("./input/day1.txt").unwrap().lines() {
        let (l_val, r_val) = line.split_once("   ").unwrap();
        left.push(l_val.parse::<i32>().unwrap());
        right.push(r_val.parse::<i32>().unwrap());
    }

    let counter = one(&left, &right);
    println!("Part One: {counter}");

    let similarity_score = two(&left, &right);
    println!("Part Two: {similarity_score}");
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_data() -> (Vec<i32>, Vec<i32>) {
        let left = vec![3, 4, 2, 1, 3, 3];
        let right = vec![4, 3, 5, 3, 9, 3];
        (left, right)
    }
    
    #[test]
    fn one_happy_path() {
        let (left, right) = test_data();
        let res = one(&left, &right);
        assert_eq!(res, 11);
    }

    #[test]
    fn two_happy_path() {
        let (left, right) = test_data();
        let res = two(&left, &right);
        assert_eq!(res, 31);
    }
}
