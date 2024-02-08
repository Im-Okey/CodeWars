"""
Karan's company makes software that provides different features based on the version of operating system of the user.

To compare versions, Karan currently parses both version numbers as floats.

While this worked for OS versions 10.6, 10.7, 10.8 and 10.9, the operating system company just released OS version 10.10. This causes his method to fail, as 10.9 is greater than 10.10 when interpreting both as numbers, despite being a lesser version.

Help Karan by writing him a function which compares two versions, and returns whether or not the first one is greater than or equal to the second.

Specification notes:

Versions are provided as strings of one or more integers separated by ..
The version strings will never be empty.
The two versions are not guaranteed to have an equal amount of sub-versions, when this happens assume that all missing sub-versions are zero.
"""


def compare_versions(version1: str, version2: str) -> bool:
    v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))

    while len(v1) < len(v2):
        v1.append(0)
    while len(v2) < len(v1):
        v2.append(0)

    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return True
        elif v1[i] < v2[i]:
            return False
    return True


if __name__ == '__main__':
    print(compare_versions("11", "10"))
