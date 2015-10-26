# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search,target):
    result = -1
    n = 0
    while search.find(target,search.find(target)+n) != -1:
        result = search.find(target,search.find(target)+n)
#        print result
        n = n + 1
        if len(search) - len(target) == result:
            return result
            break
    return result
        
print find_last('abbaabbabbbaaaabbba','ab')
print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




	
