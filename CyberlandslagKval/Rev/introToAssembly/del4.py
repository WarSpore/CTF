def main():
    rbp = 0
    rsp = 0
    rax = 0
    rdx = 0

    # Function prologue
    rbp = rsp
    rsp -= 0x50

    # Local variable initialization
    rax = 0x00
    stack_memory = bytearray(0x50)  # Using a bytearray for byte-level access
    stack_memory[-0x10] = rax
    stack_memory[-0x30] = 0x40
    stack_memory[-0x2F] = 0x41
    stack_memory[-0x2E] = 0x42
    stack_memory[-0x2D] = 0x43
    stack_memory[-0x2C] = 0x44
    stack_memory[-0x2B] = 0x45
    stack_memory[-0x2A] = 0x46
    stack_memory[-0x29] = 0x47
    stack_memory[-0x28] = 0x48
    stack_memory[-0x27] = 0x49
    stack_memory[-0x26] = 0x4A
    stack_memory[-0x25] = 0x4B
    stack_memory[-0x24] = 0x4C
    stack_memory[-0x23] = 0x4D
    stack_memory[-0x22] = 0x4E
    stack_memory[-0x21] = 0x4F
    stack_memory[-0x20] = 0x50
    stack_memory[-0x1F] = 0x51
    stack_memory[-0x1E] = 0x52
    stack_memory[-0x1D] = 0x53
    stack_memory[-0x1C] = 0x54
    stack_memory[-0x1B] = 0x55

    # Loop
    while True:
        # Incrementing loop counter
        stack_memory[-0x10] += 1

        # Start of loop
        eax = stack_memory[-0x10]
        rdx = eax
        rax = stack_memory[-0x30]
        rax += rdx
        al = stack_memory[rax]
        if al != 0:
            continue
        else:
            break

    # Function epilogue
    ret_value = stack_memory[-0x10]
    rsp = rbp
    return ret_value


if __name__ == "__main__":
    ret = main()
    print(ret)
