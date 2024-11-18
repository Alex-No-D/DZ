with open('story.txt', 'r') as f:
    a = []

    with open('new_story.txt', 'w') as f1:
        for i in f:
            print(i)


            b = i.replace('Python', 'Java')

            f1.write(b)
