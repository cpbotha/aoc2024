from collections import Counter
from testing import assert_true
from time import perf_counter_ns


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


fn part1(col1: List[Int], col2: List[Int]) raises -> Int:
    # https://docs.modular.com/mojo/manual/values/ownership/#argument-conventions
    # we make a mutable copy as sort is in-place
    var col1_local = col1
    sort(col1_local)
    var col2_local = col2
    sort(col2_local)

    var sum = 0
    for i in range(len(col1_local)):
        sum += abs(col1_local[i] - col2_local[i])

    return sum


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

    var s1 = perf_counter_ns()
    var p1 = part1(col1, col2)
    var d1 = (perf_counter_ns() - s1) / 1000
    print("part 1: {} ({} µs)".format(p1, d1))

    var s2 = perf_counter_ns()
    var p2 = part2(col1, col2)
    var d2 = (perf_counter_ns() - s2) / 1000
    print("part 2: {} ({} µs)".format(p2, d2))
