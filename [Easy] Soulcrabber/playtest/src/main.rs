use rand::rngs::StdRng;
use rand::{Rng, SeedableRng};
use std::char;
use std::fs;
use std::time::SystemTime;

fn get_rng(seed: u64) -> StdRng {
    return StdRng::seed_from_u64(seed);
}

fn rand_xor(seed: u64, input: &Vec<u8>) -> String {
    let mut rng = get_rng(seed);
    return input
        .into_iter()
        .map(|c| char::from_u32((c ^ rng.gen::<u8>()) as u32).unwrap())
        .collect::<String>();
}

fn brute_seed(input: Vec<u8>) -> String {
    let mut seed = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Time is broken")
        .as_secs();

    loop {
        let flag = rand_xor(seed, &input);

        if flag.contains("CHTB{") {
            return flag;
        } else {
            seed = seed - 1;
        }
    }
}

fn challenge_one() {
    let enc_flag = fs::read_to_string("htb-1.txt").expect("Something went wrong reading the file");
    let enc_flag = hex::decode(enc_flag).expect("Decoding failed");
    let flag = rand_xor(13371337, &enc_flag);

    println!("{}", flag);
}

fn challenge_two() {
    let enc_flag = fs::read_to_string("htb-2.txt").expect("Something went wrong reading the file");
    let enc_flag = hex::decode(enc_flag).expect("Decoding failed");
    let flag = brute_seed(enc_flag);

    println!("{}", flag);
}

fn main() {
    challenge_one();
    challenge_two();
}
