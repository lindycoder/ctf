from hashlib import sha512

from tools import open_html, first

PHPSESSID = '...'

doc = open_html("https://ringzer0ctf.com/challenges/13", cookies={
    'PHPSESSID': PHPSESSID
})

content = first(doc.select("div.message")).text.strip().split('\n')

print(content)

sha = sha512(content[1].strip().encode()).hexdigest()

result = open_html(f"https://ringzer0ctf.com/challenges/13/{sha}", cookies={
    'PHPSESSID': PHPSESSID
})

print(result.prettify())
