"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: David Soliven
Date:   4/5/2022
"""
import introcs

APIKEY = '88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    #assert that s is a string
    assert type(s) == str
    
    assert introcs.count_str(s,' ') >= 1
    #find the index of the first space
    first_space = introcs.index_str(s,' ')
    #print(f'Index of first space: {first_space}')
    #find the substring of s before the first space
    substring_before = str(s[0:first_space])
    #print(f'The substring before space is: {substring_before}')
    return substring_before


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str
    
    assert introcs.count_str(s,' ') >= 1
    #find the index of the first space
    first_space = introcs.index_str(s,' ')
    #print(f'Index of first space: {first_space}')
    #find the substring of s before the first space
    substring_after = s[first_space+1:]
    #print(f'The substring after space is: {substring_after}')
    return substring_after


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str
    assert introcs.count_str(s,'"') >= 2

    #index of first quote of s
    first_quote = introcs.index_str(s,'"')
    
    #index of second quote of s 
    second_quote = introcs.index_str(s,'"', start=first_quote+1, end=None)
    #substring inside the first pair of quotes
    substring_inside_quotes = s[first_quote+1:second_quote]
    return substring_inside_quotes


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    #assert type(s) == str
    #assert introcs.count_str(s,'"') >= 2
    #JSON Parameter
    #assert introcs.count_str(s,'"src"') == 1

    #get index after src
    #index_src = introcs.index_str(s,'\"src\"') + 5
    #print(index_src)

    #get value of key src using first_inside_quotes
    #src = first_inside_quotes(s[index_src:])
    #return src
    #my code above is incorrect. was generating errors. Jose's starter code below:
    
    assert type(json) == str
    assert '"src":' in json
    assert introcs.count_str(json[introcs.find_str(json,'"src":')+6:],'"') >= 2
    
    index = introcs.find_str(json,'src')
    index = introcs.find_str(json,':',index) # So we do not capture the src quotes
    return first_inside_quotes(json[index+1:])

    #assert type string
    #assert '"src":' must be in json
    #assert introcs.count_str(json[introcs.find_str(json,'"src":')+6:],'"')

    #index = find 'src' in jason
    #index = find ":" in json. Use index as third argument (start)

    #return use first_inside_quotes() as helper function


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str
    assert '"dst":' in json
    assert introcs.count_str(json[introcs.find_str(json,'"src":')+6:],'"') >= 2
    
    index = introcs.find_str(json,'dst')
    index = introcs.find_str(json,':',index) # So we do not capture the dst quotes
    return first_inside_quotes(json[index+1:])

    #assert type string
    #assert '"dst":' must be in json
    #assert introcs.count_str(json[introcs.find_str(json,'"dst":')+6:],'"')

    #index = find 'dst' in json
    #index = find ":" in json. Use index as third argument (start)

    #return use first_inside_quotes() as helper function


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
        
        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
        
        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON
        
        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str
    assert '"error":' in json
    assert introcs.count_str(json[introcs.find_str(json,'"error":')+8:],'"') >= 2
    
    index = introcs.find_str(json,'error')
    index = introcs.find_str(json,':',index) # So we do not capture the error quotes
    errmsg = first_inside_quotes(json[index+1:])
    
    
    return len(errmsg) > 0
    #print(errmsg)
    

    #assert type string
    #assert '"error":' must be in json
    #assert introcs.count_str(json[introcs.find_str(json,'"error":')+6:],'"')

    #index = find 'error' in json
    #index = find ":" in json. Use index as third argument (start)

    #return use first_inside_quotes() as helper function


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    #asserting preconditions of parameters
    assert introcs.isalpha(src) == True
    assert len(src) > 0
    
    assert introcs.isalpha(dst) == True
    assert len(dst) > 0

    #assert type(amt) == int or type(amt) == float
    assert introcs.isfloat(amt) or introcs.isint(amt)

    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+src+'&dst='+dst+'&amt='+str(amt)+'&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e'
    json = introcs.urlread(url)
    
    return(json)


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """

    assert introcs.isalpha(currency) == True
    assert len(currency) > 0

    assert len(currency) == 3 

    currency_check = service_response(currency, currency, 1)

    return has_error(currency_check) == False


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    assert iscurrency(src) == True
    assert iscurrency(dst) == True
    assert introcs.isfloat(amt) or introcs.isint(amt)

    #json string of exchange arguments
    json = service_response(src, dst, amt)
    
    #get string value of key 'dst'
    index = introcs.find_str(json,'dst')
    index = introcs.find_str(json,':',index) # So we do not capture the error quotes
    currency_to = first_inside_quotes(json[index+1:])

    currency_to = float(before_space(currency_to))
    
    #print(currency_to)
    return currency_to
