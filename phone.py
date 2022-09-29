class Phone:
    def __init__(self, phone_number):
        self.number = phone_number
    
    def call (self, other_number):
        print(f'calling{other_number} from {self.number}')
    
    def text(self, other_number, msg):
        print(f'texting from {self.number} to {other_number}: {msg}')
    
    def get_number(self):
        return self.number

    def set_number(self, new_number):
        self.number = new_number

    def __str__(self):
        return f'This phone number is {self.number}' #This phone number is 555-666-6666

josh = Phone('444-333-2222')
eric = Phone('555-666-6666')

print(eric) # 555-666-6666
# print(dir(eric))
print(eric.__dict__) # {'number': '555-666-6666'} - this is a class of dict

# print(josh.number, 'new phone number') # 444-333-2222 new phone number
# josh.call(eric.number,'555-666-7777') # calling555-666-7777 from 444-333-2222
# josh.text("555-666-6666", "we are almost done! Bring on SQL") # texting from 444-333-2222 to 555-666-6666: we are almost done! Bring on SQL
# josh.call(eric.number)
# josh.call(eric.get_number())

# directly accessing th properties of an instance


#! Phone is essentially the base class, iphone will be derived from Phone

class IPhone(Phone):
    def __init__(self, phone_number):
        # each iphone needs one position argumnet ('phone number')
        # print(super())
        super().__init__(phone_number)
        
        # executing before we set our other properties
        # super is a reference to the parent class
        # the parent __init__() => {}
        # the parent __init__(phone_number) => {number: phone_number}

        self.fingerprint = None

    def set_fingerprint(self, fingerprint):
        pass

    def unlock(self, fingerprint=None):
        pass

    def call(self, phone_number):
        print(f'call or face time? {phone_number}')

troy = IPhone('860-867-5309')

# print(troy.get_number()) # 860-867-5309

# troy.call(eric.get_number()) # call or face time? 555-666-6666

# what is super doing?
# how can I tell if an instance is derived from one class or another?


#! Dunder Methods