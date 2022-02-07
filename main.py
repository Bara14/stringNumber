def increaseNumber(text):
    index = len(text)
    substring_with_numbers =''
    for _ in reversed(range(0, index)):
        if text[_].isdigit():
            substring_with_numbers = substring_with_numbers + text[_]
        else:
            break
    if len(substring_with_numbers) != 0:
        reversed_substring_with_numbers = substring_with_numbers[len(substring_with_numbers)::-1]
        increased = str(int(reversed_substring_with_numbers)+1).zfill(len(reversed_substring_with_numbers))
        print(text.replace(reversed_substring_with_numbers, str(increased)))
    else:
        print(text +'1')

increaseNumber('foo00001')