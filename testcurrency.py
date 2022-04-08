"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: David Soliven
Date:   3/17/2022
"""
import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)
        
    result = currency.before_space('Hell oWor ld')
    introcs.assert_equals('Hell', result)

    result = currency.before_space(' HelloWorld')
    introcs.assert_equals('', result)

    result = currency.before_space('HelloWorld ')
    introcs.assert_equals('HelloWorld', result)

    result = currency.before_space('HelloWorld ')
    introcs.assert_equals('HelloWorld', result)

    result = currency.before_space('HelloW  orld')
    introcs.assert_equals('HelloW', result)

    
def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")
    result = currency.after_space('Hello World')
    introcs.assert_equals('World', result)
        
    result = currency.after_space('Hell oWor ld')
    introcs.assert_equals('oWor ld', result)

    result = currency.after_space(' HelloWorld')
    introcs.assert_equals('HelloWorld', result)

    result = currency.after_space('HelloWorld ')
    introcs.assert_equals('', result)

    result = currency.after_space('HelloW  orld')
    introcs.assert_equals(' orld', result) 


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    # Example: first_inside_quotes('A "B C" D') returns 'B C'
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes("A \"B C\" D")
    introcs.assert_equals('B C', result)

    # Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C' 
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('""')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes("\"A B\" C\" D")
    introcs.assert_equals('A B', result)

    result = currency.first_inside_quotes("A B \"C D\"")
    introcs.assert_equals('C D', result)

    result = currency.first_inside_quotes('A B "C D" "E F" G "H I" J K')
    introcs.assert_equals('C D', result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

    result = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("2 United States Dollars", result)

    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals("", result)
    
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals("2 United States Dollars", result)

    result = introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed')
    result = currency.get_src(result)
    introcs.assert_equals("", result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("1.772814 Euros", result)

    result = currency.get_dst('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals("", result)
    
    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals("1.772814 Euros", result)

    result = introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed')
    result = currency.get_dst(result)
    introcs.assert_equals("", result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")
    
    #print("Test case #1")
    result = currency.has_error('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    #print(result)
    introcs.assert_equals(True, result)
    
    #print("Test case #2")
    result = currency.has_error('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    #print(result)
    introcs.assert_equals(False, result)
    
    #print("Test case #3")
    result = currency.has_error('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    #print(result)
    introcs.assert_equals(False, result)

    result = introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed')
    result = currency.has_error(result)
    introcs.assert_equals(True, result)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")


    result = currency.service_response('USD','EUR',2.5) #('https://ecpyfac.ecornell.com/python/currency/fixed?src=USD&dst=EUR&amt=2.5&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e')
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}',result)

    result = currency.service_response('RUB','USD',100.0) #introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed?src=RUB&dst=USD&amt=100&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e')
    introcs.assert_equals('{"success": true, "src": "100.0 Russian Rubles", "dst": "1.586017668236824 United States Dollars", "error": ""}',result)

    result = currency.service_response('ERR','JPY',76) #introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed?src=ERR&dst=JPY&amt=76&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e')
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency ERR is not present."}',result)

    result = currency.service_response('PHP','JPY',-20) #introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed?src=PHP&dst=JPY&amt=-20&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e')
    introcs.assert_equals('{"success": true, "src": "-20.0 Philippine Pesos", "dst": "-42.28001716667037 Japanese Yen", "error": ""}',result)

    result = currency.service_response('USD','ERR',6.7) #introcs.urlread('https://ecpyfac.ecornell.com/python/currency/fixed?src=USD&dst=ERR&amt=6.7&key=88Jjdz806EvmjTaefOvrUAVG37hXwcjGnnBRufNSvo0e')
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency ERR is not present."}',result)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")

    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    result = currency.iscurrency('ERR')
    introcs.assert_equals(False, result)


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")

    result = currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175, result)
    
    result = currency.exchange('JPY', 'RUB', 100)
    introcs.assert_floats_equal(58.42653940601399,result)

    result = currency.exchange('JPY', 'RUB', -100)
    introcs.assert_floats_equal(-58.42653940601399,result)

test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print('All tests completed successfully.')