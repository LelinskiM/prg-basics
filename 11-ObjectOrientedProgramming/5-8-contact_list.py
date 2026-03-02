class contact_list:
    def __init__(self,):
        self.contacts = []

    def add_con(self, contacts):
        self.contacts.append(contacts)
    
    def display(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("contact list:")
        for contact in self.contacts:
            print(contact)
    
