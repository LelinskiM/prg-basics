from  import contacts
from contact_list import contact_list

def main():
    contact_list = contact_list()

        # Add contacts
    contact_list.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contact_list.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contact_list.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contact_list.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    # Display contact list
    contact_list.display_contacts()


if __name__ == "__main__":
    main()