#
def find_longest_name(filename):
    with open(filename) as f: return max(f.read().splitlines(), key=len)