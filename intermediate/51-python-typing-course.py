# TYPE HINTS

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("Drive")
else:
    print("please don't")


def greeting(name: str) -> str:
    return "Hello" + name
