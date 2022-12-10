use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;
use std::io::Read;
use std::io::Seek;
use std::io::SeekFrom;

fn main() {
    let file = File::open("input.txt").unwrap();
    let mut reader = BufReader::new(file);

    let max_calories = part_one(&mut reader).unwrap();
    println!("Part one answer: {max_calories}");

    // Back up to the beginning of the file.
    reader.by_ref().seek(SeekFrom::Start(0)).unwrap();
    let top_three_calories = part_two(&mut reader).unwrap();
    println!("Part two answer: {top_three_calories}");
}

fn part_one(reader: &mut impl BufRead) -> Result<i32, std::io::Error> {
    let mut max_calories = 0;
    let mut current = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if line == "" {
            if current > max_calories {
                max_calories = current;
            }

            current = 0;
            continue
        }

        let parsed_line = line.parse::<i32>().unwrap();
        current += parsed_line;
    }

    Ok(max_calories)
}

fn part_two(reader: &mut impl BufRead) -> Result<i32, std::io::Error> {
    let mut top_three = [0, 0, 0];
    let mut current = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if line == "" {
            if current > top_three[0] {
                top_three[0] = current;
                top_three.sort();
            }

            current = 0;
            continue
        }

        let parsed_line = line.parse::<i32>().unwrap();
        current += parsed_line;
    }

    let mut total = 0;
    for cal in top_three {
        total += cal;
    }

    Ok(total)
}
