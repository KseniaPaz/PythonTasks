import view
import text_fields as txt
from classes import Contact, PhoneBook


def start():
    phonebook = PhoneBook('Tasks\Phonebook3\sample3.txt')
    while True:
        choice=view.main_menu()
        match choice:
            case 1:
                phonebook.open()
                view.print_info(txt.load_successful)
            case 2:
                phonebook.save()
                view.print_info(txt.save_successfil)
            case 3:
                pb = phonebook.get()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                new_contact=view.new_contact()
                phonebook.add(new_contact)
                view.print_info(txt.new_contact_successful(new_contact.name))
            case 5:
                word = view.enter_keyword()
                result  = phonebook.find(word)
                view.show_contacts(result, txt.not_found(word))
            case 6:
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    edited_contact = view.edit_contact(pb, txt.input_index)
                    phonebook.edit_contact(edited_contact)
                    view.print_message(txt.successful_edited(edited_contact[1].name))
            case 7:
                pb = phonebook.get()
                view.show_contacts(pb, txt.empty_list_or_not_open_file)
                if pb:
                    index = view.input_index(pb, txt.input_delete_index)
                    if view.confirm(txt.confirm_delete(pb[index-1].name)):
                        view.print_message(txt.delete_contact(phonebook.remove(index)))                    
            case 8:
                if phonebook.save_on_exit():
                    if view.confirm(txt.is_changed):
                        phonebook.save()
                view.print_info(txt.bye_bye)
                exit()    