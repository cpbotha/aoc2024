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

    return _bool_vec.reduce_and()

# nelts == number of deltas, which is one less than the number of elements
fn is_safe(s: SIMD[DType.int32, 8], nelts: Int) raises -> Bool:
    var delta = s.shift_left[1]() - s

    return (pad_check_bool_simd(delta < 0, nelts) or pad_check_bool_simd(delta > 0, nelts)) and pad_check_bool_simd(abs(delta) <= 3, nelts) and pad_check_bool_simd(abs(delta) >= 1, nelts)

fn part1(contents: String) raises -> Int:
    var lines = contents.strip().split("\n")
    var sum = 0
    for line in lines:
        # mojo list limitation: iterating over the list returns a pointer to each elem which we have to deref here
        # https://docs.modular.com/mojo/manual/control-flow#iterating-over-mojo-collections
        var parts = line[].split()
        # convert to 8-element SIMD, but we only use the first N
        var s = SIMD[DType.int32, 8]()
        for i in range(len(parts)):
            s[i] = atol(parts[i])

        if is_safe(s, len(parts)-1):
            sum += 1



    return sum 


fn main() raises:
    var contents = read_file("input.txt")
    p1 = part1(contents)
    print(p1)