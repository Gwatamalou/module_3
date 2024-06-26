calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s: str):
    count_calls()
    return (len(s), s.upper(), s.lower())


def is_contains(s: str, a: list):
    count_calls()
    for i in a:
        if s.lower() == i.lower():
            return True
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)