fn part1(input: &str) -> u32 {
    let mut ans: u32 = 0;

    for line in input.split("\n").into_iter() {
        let mut num = 0;
        for c in line.chars() {
            if c.is_numeric() {
                num += 10 * c.to_digit(10).unwrap();
                break;
            }
        }
        for c in line.chars().rev() {
            if c.is_numeric() {
                num += c.to_digit(10).unwrap();
                break;
            }
        }
        ans += num;
    }
    ans
}

fn part2(input: &str) -> u32 {
    let mut ans = 0;

    let v = vec![
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ];
    for line in input.split("\n").into_iter() {
        // Forward.
        let mut l = 0;
        for i in 0..line.len() {
            let c = line.chars().nth(i).unwrap_or(' ');
            if c.is_numeric() {
                l = c.to_digit(10).unwrap();
                break;
            }
            for (pattern, digit) in v.iter() {
                if line[i..].starts_with(pattern) {
                    l = *digit;
                    break
                }
            }
            if l > 0 {
                break;
            }
        }
        // Backward.
        let mut r = 0;
        let line: String = line.chars().rev().collect();
        for i in 0..line.len() {
            let c = line.chars().nth(i).unwrap_or(' ');
            if c.is_numeric() {
                r = c.to_digit(10).unwrap();
                break;
            }
            for (pattern, digit) in v.iter() {
                if line[i..].starts_with(&pattern.chars().rev().collect::<String>()) {
                    r = *digit;
                    break;
                }
            }
            if r > 0 {
                break;
            }
        }
        ans += 10*l + r;
    }
    ans
}

fn main() {
    assert_eq!(part1(include_str!("../../example/day01a.txt")), 142);
    println!("part1 = {}", part1(include_str!("../../input/day01.txt")));

    assert_eq!(part2(include_str!("../../example/day01b.txt")), 281);
    println!("part2 = {}", part2(include_str!("../../input/day01.txt")));
}
