use std::clone::Clone;
use std::cmp::Ordering;
use std::cmp::PartialOrd;
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::io::Read;
use std::io::Seek;
use std::io::SeekFrom;

#[derive(Clone)]
#[derive(PartialEq)]
enum Hand {
    Rock,
    Paper,
    Scissors,
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Hand) -> Option<Ordering> {
        if self == other {
            return Some(Ordering::Equal);
        }

        if self == &Hand::Rock && other == &Hand::Scissors {
            return Some(Ordering::Greater);
        }

        if self == &Hand::Paper && other == &Hand::Rock {
            return Some(Ordering::Greater);
        }

        if self == &Hand::Scissors && other == &Hand::Paper {
            return Some(Ordering::Greater);
        }

        Some(Ordering::Less)
    }
}

enum Outcome {
    Win,
    Lose,
    Draw,
}

fn string_to_hand(val: &str) -> Option<Hand> {
    match val {
        "A" => Some(Hand::Rock),
        "B" => Some(Hand::Paper),
        "C" => Some(Hand::Scissors),
        _ => None,
    }
}

fn encrypted_string_to_hand(val: &str) -> Option<Hand> {
    match val {
        "X" => Some(Hand::Rock),
        "Y" => Some(Hand::Paper),
        "Z" => Some(Hand::Scissors),
        _ => None,
    }

}

fn encrypted_outcome_to_hand(encrypted: &str, opponent: &Hand) -> Hand {
    let desired_outcome = match encrypted {
        "X" => Outcome::Lose,
        "Y" => Outcome::Draw,
        _ => Outcome::Win,
    };

    let you = match desired_outcome {
        Outcome::Win => match opponent {
            &Hand::Rock => Hand::Paper,
            &Hand::Paper => Hand::Scissors,
            &Hand::Scissors => Hand::Rock,
        },
        Outcome::Lose => match opponent {
            &Hand::Rock => Hand::Scissors,
            &Hand::Paper => Hand::Rock,
            &Hand::Scissors => Hand::Paper,
        },
        Outcome::Draw => opponent.clone(),
    };

    you
}

fn play(you: Hand, opponent: Hand) -> i32 {
    let mut score = match you {
        Hand::Rock => 1,
        Hand::Paper => 2,
        Hand::Scissors => 3,
    };

    if you == opponent {
        score += 3
    }

    if you > opponent {
        score += 6
    }

    score
}

fn part_one(reader: &mut impl BufRead) -> Result<i32, std::io::Error> {
    let mut score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let mut split = line.split(" ");

        let opponent = string_to_hand(split.next().unwrap());
        let you = encrypted_string_to_hand(split.next().unwrap());
        score += play(you.unwrap(), opponent.unwrap());
    }

    Ok(score)
}

fn part_two(reader: &mut impl BufRead) -> Result<i32, std::io::Error> {
    let mut score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let mut split = line.split(" ");

        let opponent = string_to_hand(split.next().unwrap()).unwrap();
        let you = encrypted_outcome_to_hand(split.next().unwrap(), &opponent);
        score += play(you, opponent);
    }

    Ok(score)
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
