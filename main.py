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
        numbers_of_zero = reversed_substring_with_numbers[:-1].count('0')
        if numbers_of_zero <= 1:
            to_change = str(int(reversed_substring_with_numbers)+1)
        if numbers_of_zero == 2:
            to_change = '0'+ str(int(reversed_substring_with_numbers)+1)
        if numbers_of_zero > 2:
            to_change = numbers_of_zero*'0' + str(int(reversed_substring_with_numbers)+1)

    print(text.replace(reversed_substring_with_numbers, str(to_change)))

increaseNumber('aasdfg45667hh000010')