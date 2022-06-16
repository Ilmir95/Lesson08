import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info and found_info[0]:
        name, addr = found_info[0]
    else:
        return ValueError(f'wrong email: {email}')
    return name, addr
print(email_parse('ilmir131313@yandex.ru'))
print(email_parse('ilmir131313@yandexru'))