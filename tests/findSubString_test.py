s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
# Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения подстроки в строку и -1, если подстрока не найдена. Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.

# Например, для проверки того, что в текущем url содержится строка login:
assert "login" in browser.current_url, # сообщение об ошибке

# проверка подстроки через функцию

def test_substring(full_string, substring):
        assert substring in full_string, \
            f"expected '{substring}' to be substring of '{full_string}'"