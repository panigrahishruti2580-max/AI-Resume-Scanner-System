import re


def extract_email(text):

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    return emails[0] if emails else "Not Found"


def extract_phone(text):

    phones = re.findall(
        r'[\+]?\d[\d\s\-\(\)]{8,15}',
        text
    )

    return phones[0] if phones else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:20]:

        line = line.strip()

        if not line:
            continue

        # Skip email lines
        if "@" in line:
            continue

        # Skip lines containing numbers
        if any(char.isdigit() for char in line):
            continue

        words = line.split()

        # Candidate name usually has 2-4 words
        if (
            2 <= len(words) <= 4
            and len(line) < 35
        ):
            return line.title()

    return "Not Found"