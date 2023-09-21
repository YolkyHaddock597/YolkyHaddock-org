import html

def sanitize_input(input_str):
    # Escaping special characters in HTML
    sanitized_str = html.escape(input_str)
    return sanitized_str

print(sanitize_input("SELECT info FROM orders;"))

