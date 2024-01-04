from project import convert_symbols_to_emoji, number_of_active_users, check_messages_for_bad_words, bad_word_list_creator
from emoji_dictionary import emoji

def test_convert_symbols_to_emoji():
    assert convert_symbols_to_emoji("<3") == "❤️"
    assert convert_symbols_to_emoji("Hello, my dear friend 8)") == "Hello, my dear friend 😎"
    assert convert_symbols_to_emoji(":D:D:D") == "😀😀😀"
    assert convert_symbols_to_emoji("0adfgjhasdfjh:O:") == "0adfgjhasdfjh😮:"

def test_number_of_active_users():
    assert number_of_active_users([]) == 0
    assert number_of_active_users([1,2,3]) == 3
    assert number_of_active_users([("Vlad", "Socket", "blah blah blah")]) == 1

def test_check_messages_for_bad_words():
    assert check_messages_for_bad_words("wtf", bad_word_list_creator) == "***"
    assert check_messages_for_bad_words("fuck, we have lot's of homework", bad_word_list_creator) == "****, we have lot's of homework"
    assert check_messages_for_bad_words("0123 Vlad help me you dumbass", bad_word_list_creator) == "0123 Vlad help me you dumb***"