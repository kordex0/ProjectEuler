
struct Fibonacci {
    curr: u32,
    next: u32,
}

impl Iterator for Fibonacci {
    type Item = u32;
    fn next(&mut self) -> Option<u32> {
        let new_next = self.curr + self.next;
        
        self.curr = self.next;
        self.next = new_next;
        
        Some(self.curr)
    }
}

fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 1, next: 1 }
}

fn p0001(n: u32) -> u32 {
    (1..n).filter(|n| n % 3 == 0 || n % 5 == 0).sum()
}

fn p0002(n: u32) -> u32 {
    fibonacci().take_while(|&x| x < n).filter(|x| x % 2 == 0).sum()
}

fn main() {
    println!("{}", p0001(1000));
    println!("{}", p0002(4000000));
}

