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

fn rand_xor(input : Vec<u8>) -> String {
    let seed = 13371337;
    let mut rng = get_rng(seed);
    return input
        .into_iter()
        .map(|c| char::from_u32((c ^ rng.gen::<u8>()) as u32).unwrap())
        .collect::<String>();
}

pub fn solve() {
    let chal = "1b591484db962f7782d1410afa4a388f7930067bcef6df546a57d9f873";

    let parsed = parse_hex(chal);
    let out = rand_xor(parsed);

    println!("{}", out);

}