from collections import Counter
from testing import assert_true


fn read_file(filename: String) raises -> String:
    with open(filename, "r") as f:
        return f.read()


fn parse_columns(contents: String) raises -> Tuple[List[Int], List[Int]]:
    var col1 = List[Int]()
    var col2 = List[Int]()

    var lines = contents.strip().split("\n")
    for line in lines:
        # mojo list limitation: iterating over the list returns a pointer to each elem which we have to deref here
        # https://docs.modular.com/mojo/manual/control-flow#iterating-over-mojo-collections
        var parts = line[].split()
        if len(parts) == 2:
            col1.append(atol(parts[0]))
            col2.append(atol(parts[1]))

    return (col1, col2)


fn part2(col1: List[Int], col2: List[Int]) raises -> Int:
    var counter = Counter[Int](col2)
    # iterate over col1, get the count of each element from col2
    var sum = 0
    for x in col1:
        sum += x[] * counter[x[]]

    return sum


fn main() raises:
    var contents = read_file("input.txt")
    (col1, col2) = parse_columns(contents)

    print(part2(col1, col2))
