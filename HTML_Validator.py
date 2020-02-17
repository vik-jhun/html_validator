#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    s = _extract_tags(html)
    balanced = True
    index = 0
    while i < len(s)-1:
#n   for index in range(len(symbol_string)):
        opening = s[i]
        closing = "<" + "/" + opening[1:]
        if s[i+1] != closing:
            opening = s[i+1]
            closing = "<" + "/" + opening[1:]
            i+=1
            if opening[1:2] == '/':
                return False
        else:
            s.remove(opening)
            s.remove(closing)
            i = 0
        print(s)
    print(s)

    if (len(s) != 0):
        return False
    else:
        return True
        if symbol in "<":
            s.append(symbol)
        else:
            if s == []:
                balanced = False
            else:
                first = s.pop()
                if not matches(first,symbol):
                    balanced = False
        index = index + 1
    if balanced and s == []:
        return True
    else:
        return False

def _matches(opening, closing):
    openings = "<"
    closings = ">"
    return openings.index(opening) == closings.index(closing)




def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.
    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    s=[]
    for i in range(len(html)):
        temp = ''
        symbol = html[i]
        if symbol == '<' :
            while symbol != '>':
                temp += symbol
                i = i+1
                symbol = html[i]
            temp += '>'
            s.append(temp)
    return s

print(_extract_tags('<whatever>hello<whatever/>'))
