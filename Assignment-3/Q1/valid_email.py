
import re

# Question 1:
#-----------------------------------------------------
# The function receives a name of file and searches for emails addresses in it.
# The function prints 2 lists:
#   1. list of Valid emails 
#   2. list of Invalid emails 
#-----------------------------------------------------

# return true if the email valid, otherwise return false
def get_emails(email: str) -> bool:
    '''
    >>> get_emails('abc.def@mail.com')
    True
    >>> get_emails('abc@mail.com')
    True
    >>> get_emails('abc-@mail.com')
    False
    >>> get_emails('abc..def@mail.com')
    False
    '''

    # Make a regular expression for validating an Email
    # https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    # check if the emails match - True if re.fullmatch(regex, email) else False
    return re.fullmatch(regex, email) is not None
    
# function that searches emails and checks if the email is valid or invalid
def search_emails(file: str):
    '''
    >>> search_emails('emails_address')
    Valid emails:
    [abc.def@mail.com, abc@mail.com, abc_def@mail.com, abc.def@mail.cc, abc.def@mail-archive.com, abc.def@mail org, abc.def@mail.com ]

    Invalid emails:
    [abc-@mail.com, abc..def@mail.com, .abc@mail.com, abc#def@mail.com, abc.def@mail.c, abc.def@mail#archive.com, abc.def@mail, abc.def@mail..com ]
    '''
    valid_emails = list()
    invalid_emails = list()

    with open(file, "r") as f:
        emails = f.read()
        lst_emails = list(emails.split("\n")) # split a new line

        for email in lst_emails:
            if get_emails(email):
                if email is not None:
                    valid_emails.append(email)
            else:
                if email is not None:
                    invalid_emails.append(email)
    
    # print Valid emails
    print("Valid emails:")
    print_emails(valid_emails)

    # print Invalid emails
    print("\nInvalid emails:")
    print_emails(invalid_emails)

# function that print the emails in the list
def print_emails(emails: list):
    print("[", end="")
    for i in range(len(emails)):
        if i < len(emails)-1:
            if emails[i] != "":
                print(emails[i], end = ", ")
        else:
            print(emails[i], "]")

# main function
if __name__ == '__main__':
    import doctest
    #print(get_emails('abc.def@mail#archive.com'))
    search_emails('emails_address')
    