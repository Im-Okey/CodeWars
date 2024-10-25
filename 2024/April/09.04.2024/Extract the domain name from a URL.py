"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

import re


def domain_name(url: str) -> str:
    pattern = r"(https?://)?(www\d?\.)?([a-zA-Z0-9-]+)\."

    match = re.search(pattern, url)

    if match:
        return match.group(3)


if __name__ == '__main__':
    domain_name("http://google.com")
