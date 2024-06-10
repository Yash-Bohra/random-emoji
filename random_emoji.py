import random
def generate_random_emoji():
    start = 0x1F600  # 😀
    end = 0x1F64F  # 🙏
    code_point = random.randint(start, end)
    # Convert the code point to an emoji --typecasting--
    return chr(code_point)

print(generate_random_emoji())