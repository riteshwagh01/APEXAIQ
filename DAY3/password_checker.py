import re 
from concurrent.futures import ThreadPoolExecutor

passwords=[
     "admin123",
    "Password@123",
    "abc",
    "Hello123",
    "Strong#Pass99",
    "welcome",
    "MyPass@2025",
    "12345678"
]

def check(passw):
        length=len(passw)>=8
        upper=bool(re.search(r"[A-Z]",passw))
        lower=bool(re.search(r"[a-z]",passw))
        digit=bool(re.search(r"\d",passw))
        special_char=bool(re.search(r"[!@#$%^&*()_<>:;?/{}]",passw))

        if length and upper and lower and digit and special_char:
            security="strong"
        elif length and special_char:
            security="medium"
        elif length and digit and upper:
            security="medium"
        else:
            security="low"
        
        return{
            "password":passw,
            "security":security
        }
        
def multi():
    with ThreadPoolExecutor(max_workers=5) as executor:
        answer=list(executor.map(check,passwords))
        return answer

answer=multi()
# print(answer)
for i in answer:
    print(i)