import sys

def main():
    stack = bytearray(0x30)  # Allocate space for stack
    rdi = id(stack) + 8  # Get address of stack + 8
    rsi = 0x40
    rcx = 0
    r8 = 0

    result = bytearray()

    while r8 < 0x18:
        rcx += 1
        rsi += 1
        if rcx % 2 == 0:
            result.append(rsi & 0xFF)
            r8 += 1

    result.append(0x00)

    # Print the result
    sys.stdout.buffer.write(result)

if __name__ == "__main__":
    main()
