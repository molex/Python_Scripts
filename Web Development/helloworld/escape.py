def escape_html(s):
    s = s.replace(">","&gt;")
    s = s.replace("<","&lt;")
    s = s.replace('"',"&quot;")
    s = s.replace("&","&amp;")
    return s


print escape_html("1 > 2")
print escape_html("1 < 2")
print escape_html("1 & 2")
print escape_html('1 " 2')
