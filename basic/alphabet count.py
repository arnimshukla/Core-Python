name = "arnim shukla"
for ch in "abcdefghijklmnopqrst":
    count = 0
    for letter in name:
        if ch == letter:
            count += 1

    if count > 0:
       print(ch, "Count ", count)
