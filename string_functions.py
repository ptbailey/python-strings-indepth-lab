def say_hello(name):
    return "Hi my name is {}".format(name)
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate

def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace, str_to_insert)
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string

def remove_duplicate_punctuation(string_var):
    import string
    new_string = ''
    punctuation = string.punctuation
    for x in range(1,(len(string_var))):
        if string_var[x-1] not in punctuation:
            new_string = new_string + string_var[x-1]
        elif string_var[x-1] != string_var[x]:
            new_string = new_string + string_var[x-1]
    return new_string + string_var[-1]
    # should remove all duplicate punctuation marks in a given string
    # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
    # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"


def validate_email_format(email):
    import string
    if email.count('@') == 1 and email.count('.com') == 1:
        special_char = string.punctuation
        person_part = (email.split('@'))[0]
        correct_email = ''
        for char in person_part:
            if char not in special_char:
                correct_email = correct_email + char
        if correct_email == person_part:
            return True
        else:
            return False
    else:
        return False

    # should make sure there are no special characters (i.e. *,~,#,$,%,&,(,),`,",',:,;,/,>,<)
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise


def anonymize_credit_card_number(credit_card_number):
    credit_card = credit_card_number[:-4]
    ccn = ''
    for char in credit_card:
        try:
            if type(int(char)) == int:
                ccn = ccn + 'X'
        except:
            ccn = ccn + char
    return ccn + credit_card_number[-4:]
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
