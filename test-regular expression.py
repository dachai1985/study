# -*- coding: utf-8 -*-

import re

def is_valid_email(addr):
    re_email = re.compile(r'([0-9a-zA-Z\.]+)@(\w+.com)$')
    if re_email.match(addr):
        return True

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert not is_valid_email('bill.gates@microsoft.com111')

print('ok1')

#=====================
def name_of_email(addr):
    re_email1 = re.compile(r'([0-9a-zA-Z.]+)@([0-9a-zA-Z.]+?)(com|org)')
    re_email2 = re.compile(r'<([a-zA-Z]+\s[a-zA-Z]+)>\s([0-9a-zA-Z.])+@([0-9a-zA-Z.]+?org)')

    if re_email1.match(addr):
        return re_email1.match(addr).group(1)
    elif re_email2.match(addr):
        return re_email2.match(addr).group(1)
    else:
        return None

print('111111111111==', name_of_email('<Tom Paris> tom@voyager.org'))
print('222222222222=', name_of_email('tom@voyager.org'))
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok2')