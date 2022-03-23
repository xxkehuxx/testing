strng = 'foo00'
import re
def increment_string(strng):
    num = re.findall(r'[0-9]+', strng)
    if num == []:
        return strng+'1'
    else:

        num = num[0]
        strng = strng.replace(num, '')

        new_num = int(num)+1
        new_num = num.replace(str(int(num)), str(new_num))
        return strng+new_num
