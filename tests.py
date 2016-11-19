"""
This file contains all the tests I ran for the functions while building them
"""

from palindrome import palindrome
from meeting import meeting

#Test cases for has_palindrome
def main():
    print("Test cases for has_palindrom")
    print(palindrome.has_palindrome("civic"))
    print(palindrome.has_palindrome("ivicc"))
    print(not palindrome.has_palindrome("civil"))
    print(palindrome.has_palindrome("sitonapotatopanotis"))
    print(palindrome.has_palindrome("Civic"))
    print(palindrome.has_palindrome(" Civic"))
    print(palindrome.has_palindrome("Sit on a Potato pan Otis"))
    print(not palindrome.has_palindrome(23))
    print(palindrome.has_palindrome("palindrome/trueTest.txt"))
    print(not palindrome.has_palindrome("palindrome/falseTest.txt"))
    print("End\n")

    print("Test cases for condense_meeting_times")
    print(meeting.condense_meeting_times(
        [(20,22), (25,30)])
          == [(20,22), (25,30)])
    print(meeting.condense_meeting_times(
        [(20, 22), (21, 22), (25, 30)])
          == [(20,22), (25,30)])
    print(meeting.condense_meeting_times(
        [(25, 30), (20, 22), (21, 22)])
          == [(25,30), (20,22)])
    print(meeting.condense_meeting_times(
        [(20, 25), (21, 22), (25, 30)])
          == [(20,30)])
    print(meeting.condense_meeting_times([(12341234, 12341237),
                                          (12341228, 12341234),
                                          (12341232, 12341257)])
                                      == [(12341228, 12341257)])
    print(meeting.condense_meeting_times(23) == [])
    print(meeting.condense_meeting_times([]) == [])
    print(meeting.condense_meeting_times([]) == [])
    print(meeting.condense_meeting_times([
        ("2016-09-01T21:22:17-06:00", "2016-09-01T21:31:17-06:00"),
        ("2016-09-01T21:25:17-06:00", "2016-09-01T21:26:17-06:00"),
        ("2016-09-01T21:30:17-06:00", "2016-09-01T21:45:17-06:00")])
          == [("2016-09-01T21:22:17-06:00", "2016-09-01T21:45:17-06:00")])
    print("End")
main()
