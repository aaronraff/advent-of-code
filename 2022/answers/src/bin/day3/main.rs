use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::io::Read;
use std::io::Seek;
use std::io::SeekFrom;

fn type_to_priority(item: char) -> u32 {
    // A is 65 in ascii and a is 97.
    // A is worth 27 points and a is worth 1 point.
    let score = item as u32;
    if item.is_lowercase() {
        return score - 96
    }

    score - 38
}

fn part_one(reader: &mut impl BufRead) -> Result<u32, std::io::Error> {
    let mut score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let chars: Vec<char> = line.chars().collect();
        let midway = chars.len() / 2 - 1;

        let mut map: HashMap<char, bool> = HashMap::new();
        for index in 0..midway+1 {
            map.insert(chars[index], true);
        }

        let mut found: HashMap<char, bool> = HashMap::new();
        for index in midway+1..chars.len() {
            let item = chars[index];
            if map.get(&item).is_some() && found.get(&item).is_none() {
                found.insert(item, true);
                score += type_to_priority(chars[index]);
            }
        }
    }

    Ok(score)
}

fn part_two(reader: &mut impl BufRead) -> Result<u32, std::io::Error> {
    let mut score = 0;
    let mut lines = reader.lines();
    loop {
        let mut group: Vec<String> = Vec::new();
        for _ in 0..3 {
            match lines.next() {
                Some(x) => group.push(x.unwrap()),
                None => return Ok(score)
            }
        }

        let mut overlap: HashMap<char, u8> = HashMap::new();
        for bag in group {
            let mut in_bag: HashMap<char, bool> = HashMap::new();
            for item in bag.chars() {
                // Item was already accounted for.
                if in_bag.insert(item, true).is_some() {
                    continue
                }

                match overlap.get(&item) {
                    Some(x) => {
                        let updated = x + 1;
                        overlap.insert(item, updated);
                        if updated == 3 {
                            score += type_to_priority(item);
                        }
                    },
                    None => {
                        overlap.insert(item, 1);
                        ()
                    },
                }
            }
        }
    }
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let mut reader = BufReader::new(file);

    let score = part_one(&mut reader).unwrap();
    println!("Part one answer: {score}");

    // Back up to the beginning of the file.
    reader.by_ref().seek(SeekFrom::Start(0)).unwrap();
    let score_two = part_two(&mut reader).unwrap();
    println!("Part two answer: {score_two}");
}
