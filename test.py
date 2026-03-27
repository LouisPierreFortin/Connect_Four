from typing import overload, Union

# --- Overload type signatures (for static type checkers only) ---
@overload
def greet(name: str) -> str: ...
@overload
def greet(first_name: str, last_name: str) -> str: ...
@overload
def greet(title: str, name: str) -> str: ...

# --- Single runtime implementation ---
def greet(*args: str, **kwargs: str) -> str:
    """
    Greet a person in different ways:
    1. greet("Alice")
    2. greet("John", "Doe")
    3. greet(title="Dr.", name="Smith")
    """
    if args and not kwargs:
        if len(args) == 1:
            return f"Hello, {args[0]}!"
        elif len(args) == 2:
            return f"Hello, {args[0]} {args[1]}!"
        else:
            raise TypeError("Too many positional arguments.")
    elif kwargs:
        if "title" in kwargs and "name" in kwargs:
            return f"Hello, {kwargs['title']} {kwargs['name']}!"
        else:
            raise TypeError("Missing 'title' or 'name' in keyword arguments.")
    else:
        raise TypeError("Invalid arguments.")

# --- Example usage ---
print(greet("Alice"))                  # Hello, Alice!
print(greet("John", "Doe"))             # Hello, John Doe!
print(greet(title="Dr.", name="Smith")) # Hello, Dr. Smith!
