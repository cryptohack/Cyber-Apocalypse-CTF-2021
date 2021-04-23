use rand::{Rng,SeedableRng};
use rand::rngs::StdRng;
use std::time::SystemTime;
use std::char;

fn parse_hex(hex_asm: &str) -> Vec<u8> {
    let mut hex_bytes = hex_asm.as_bytes().iter().filter_map(|b| {
        match b {
            b'0'..=b'9' => Some(b - b'0'),
            b'a'..=b'f' => Some(b - b'a' + 10),
            b'A'..=b'F' => Some(b - b'A' + 10),
            _ => None,
        }
    }).fuse();

    let mut bytes = Vec::new();
    while let (Some(h), Some(l)) = (hex_bytes.next(), hex_bytes.next()) {
        bytes.push(h << 4 | l)
    }
    bytes
}

fn get_rng(seed : u64) -> StdRng {
    return StdRng::seed_from_u64(seed);
}

fn brute_xor(input : Vec<u8>) -> String {
    let mut i = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Time is broken")
        .as_secs();
    loop {
        let rng = get_rng(i);
        i -= 1;
        let xored = rand_xor(input.to_vec(), rng);
        if xored.contains("CHTB") {
            return xored;
        }
    }
}

fn rand_xor(input : Vec<u8>, mut rng: StdRng) -> String {
    return input
        .into_iter()
        .map(|c| char::from_u32((c ^ rng.gen::<u8>()) as u32).unwrap())
        .collect::<String>();
}

pub fn solve() {
    let chal = "5e4865b8232fadf1d10c6a36d599c043e06f226d60deed28e194fd49a22cbb8a66e714bf5e2ab732cd";

    let parsed = parse_hex(chal);
    let out = brute_xor(parsed);

    println!("{}", out);
}