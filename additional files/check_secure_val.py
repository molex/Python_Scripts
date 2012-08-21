import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
    return h[:h.find(",")] if h == make_secure_val(h[:h.find(",")]) else None



print check_secure_val("mike,18126e7bd3f84b3f3e4df094def5b7de")
