use std::collections::HashMap;

fn fizzbuzz(nums_words: &HashMap<u32, &str>) {
    (0..=25).into_iter()
            .collect::<Vec<u32>>()
            .iter()
            .map(
                |x|
                (
                    nums_words.keys()
                              .map(
                                  move |n|
                                  if x%n==0 {
                                      nums_words.get(n)
                                      .unwrap()
                                      .to_string()
                                  } else {
                                      "".to_string()
                                  }
                                )
                              .collect::<Vec<String>>()
                              .join(""),
                    x
                )
            )
            .for_each(
                |x|
                println!(
                    "{}",
                    if x.0!="".to_string() {
                        x.0
                    } else {
                        x.1.to_string()
                    }
                )
            )
}

macro_rules! fb[
    { $($num:expr => $word:expr),+ } => {
        {
            let mut m = ::std::collections::HashMap::new();
            $(
                m.insert($num, $word);
            )+
             m
        }
    };
];

fn main() {
    fizzbuzz(&fb![2=>"Zip",3=>"Fizz",5=>"Buzz",10=>"Zapp",11=>"Zopp"]);
}
