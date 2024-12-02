# I'm really missing a nice vector representation and operations in mojo 2024-12-02
# because I'm stubborn, I'm using SIMD with padding to fake this
# copyright charlbotha.com

from collections import Counter
from testing import assert_true
from time import perf_counter_ns
from tensor import Tensor


fn read_file(filename: String) raises -> String:
    with open(filename, "r") as f:
        return f.read()


# UNUSED
# keeping this here as docs of what generic function could look like
fn generic_is_safe[nelts: Int](v: List[String]) raises -> Bool:
    @parameter
    s = SIMD[DType.int32, nelts]()
    for i in range(nelts):
        s[i] = atol(v[i])

    var delta = s.shift_left[1]() - s
    print(delta.slice[nelts-1]() < 0)

    return False

fn pad_check_bool_simd(bool_vec: SIMD[DType.bool, 8], nelts: Int) raises -> Bool:
    # need to make local copy because we're going to pad
    var _bool_vec = bool_vec
    # set unused values to True, so that they don't interfere with this test
    for i in range(nelts, 8):
        _bool_vec[i] = True

    # thanks to rd4com on the Mojo discord for the "all()" suggestion. My .reduce_and() was working, but is not as pretty as all()
    #return _bool_vec.reduce_and()
    return all(_bool_vec)

# nelts == number of deltas, which is one less than the number of elements
fn is_safe(s: SIMD[DType.int32, 8], nelts: Int) raises -> Bool:
    var delta = s.shift_left[1]() - s

    return (pad_check_bool_simd(delta < 0, nelts) or pad_check_bool_simd(delta > 0, nelts)) and pad_check_bool_simd(abs(delta) <= 3, nelts) and pad_check_bool_simd(abs(delta) >= 1, nelts)

fn to_simd(parts: List[String]) raises -> SIMD[DType.int32, 8]:
    var s = SIMD[DType.int32, 8]()
    for i in range(len(parts)):
        s[i] = atol(parts[i])

    return s

fn part1(contents: String) raises -> Int:
    var lines = contents.strip().split("\n")
    var sum = 0
    for line in lines:
        # mojo list limitation: iterating over the list returns a pointer to each elem which we have to deref here
        # https://docs.modular.com/mojo/manual/control-flow#iterating-over-mojo-collections
        var parts = line[].split()
        # convert to 8-element SIMD, but we only use the first N
        s = to_simd(parts)

        if is_safe(s, len(parts)-1):
            sum += 1



    return sum 


fn part2(contents: String) raises -> Int:
    var lines = contents.strip().split("\n")
    var sum = 0
    for line in lines:
        # mojo list limitation: iterating over the list returns a pointer to each elem which we have to deref here
        # https://docs.modular.com/mojo/manual/control-flow#iterating-over-mojo-collections
        var parts = line[].split()
        # convert to 8-element SIMD, but we only use the first N
        var s = to_simd(parts)
        for i in range(len(parts)):
            s[i] = atol(parts[i])

        if is_safe(s, len(parts)-1):
            sum += 1

        else:
            for j in range(len(parts)):
                new_parts = List(other=parts)
                _ = new_parts.pop(j)
                if is_safe(to_simd(new_parts), len(new_parts)-1):
                    sum += 1
                    break



    return sum 

fn main() raises:
    var contents = read_file("input.txt")
    p1 = part1(contents)
    # 421
    print(p1)

    p2 = part2(contents)
    # 476
    print(p2)
