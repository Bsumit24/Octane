def compress_string(s: str) -> str:
    # If input string is empty, it will return an empty string
    # Input value as shown in example.
    if not s:
        return ""

    compressed = []
    count = 1

    #  This module is for count value iterate through string from second value
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Append and Count
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    compressed.append(s[-1] + str(count))

    # Join the list into a single string
    compressed_string = ''.join(compressed)
    # Compress the value
    return compressed_string if len(compressed_string) < len(s) else s


# Example usage
input_str = "aabcccccaaaddddfffgggeeewww"
result = compress_string(input_str)
print(result)