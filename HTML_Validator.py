def par_checker(symbol_string):
    '''
    >>> par_checker('<></>')
    True
    >>> par_checker('<></')
    False
    '''
    s = _extract_tags(html)
    balanced = True
    i = 0
    while i < len(s)-1:
        opening = s[i]
        closing = "<" + "/" + opening[1:]
        if s[i+1] != closing:
            opening = s[i+1]
            closing = "<" + "/" + opening[1:]
            i+=1
        else:
            s.remove(opening)
            s.remove(closing)
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
                top = s.pop()
                if not matches(opening,closing):
                    balanced = False
        index += 1
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
    for i in range(len(html)):     #makes i a number unlike for i in html, so helps in indexing
        temp = ''
        character = html[i]
        if character == '<' :
            while character != '>':
                temp += character
                i = i+1
                character = html[i]
            temp += '>'
            s.append(temp)
    return s
