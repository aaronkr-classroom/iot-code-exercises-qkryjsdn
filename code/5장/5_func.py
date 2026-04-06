#5_func.py

def return_info(name, phone, address, email):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    return f"이름:\t{name}\n{contact_info}\n주소:\t{address}"


def print_info(name, phone, address, email=""):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    print(f"이름:\t{name}\n{contact_info}\n주소:\t{address}")
    
print_info("박선우", "010-7777-7777", "증평")
person = return_info(
    email="hello@ut.ac.kr", phone = "010-1234-5678",
    address="교통대학교", name="박선우"
    )
print()
print(person)