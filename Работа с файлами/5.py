with open('part1.txt', 'r') as f:
    with open('part2.txt', 'r') as f1:
        with open('full_text.txt', 'w') as f2:
            for i in f:
                f2.write(i)
            for i1 in f1:
                f2.write(i1)