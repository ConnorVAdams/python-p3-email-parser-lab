import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        split_regex = r'\s|,\s|,'
        emails_to_parse = sorted(re.split(split_regex, self.email_addresses))
        validate_regex = re.compile(r"[A-z][A-z.0-9]*@[a-z]*.[a-z]*\b")
        return [email for email in emails_to_parse if validate_regex.match(email)]
