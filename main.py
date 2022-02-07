def increaseNumber(text):
    list_of_numbers =['1','2','3','4','5','6','7','8','9','0']
    index = len(text)
    substring_with_numbers =''
    for _ in reversed(range(0, index)):
        if text[_] in list_of_numbers:
            substring_with_numbers = substring_with_numbers + text[_]
        else:
            break
    if len(substring_with_numbers) != 0:
        reversed_substring_with_numbers = substring_with_numbers[len(substring_with_numbers)::-1]
        to_change = int(reversed_substring_with_numbers) +1
        print(text.replace(reversed_substring_with_numbers, str(to_change)))

increaseNumber('aasdfg45667hh003')