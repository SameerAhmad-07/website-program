import sys

if len(sys.argv) == 5:
    website  = sys.argv[1]
    url      = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
else:
    website  = "google.com"
    url      = "https.google.com"
    username = "Sameer Ahmad"
    password = "sameer@07"

print("Login Details:")
print(f"Website : {website}")
print(f"URL     : {url}")
print(f"Username: {username}")
print(f"Password: {password}")
