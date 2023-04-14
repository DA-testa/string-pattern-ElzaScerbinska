# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    text = input()
    if "F" in text:
        #filename = input()
        #if "a" not in filename:
        path = "./tests/" + "06"#filename
        with open(path, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return (pattern, text)
    if "I" in text:
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

B = 13
Q = 256

def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    pattern_len = len(pattern)
    text_len = len(text)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * B) % Q

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])

    occurances = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_len]:
                occurances.append(i)
        if i < text_len - pattern_len:
            text_hash = ((text_hash - ord(text[i]) * multiplier) * B +ord(text[i+pattern_len])) % Q

    # and return an iterable variable
    return occurances

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

