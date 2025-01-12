    main:
        push   rbp     ; plasserer rbp på stacken
        mov    rbp,rsp             ; flytter verdien til rsp til rbp
        sub    rsp, 0x50    ; rsp har ny addresse rsp-0x59
        mov    rax, 0x00    ; rax har ny verdi 0x00
        mov    [rbp-0x10],rax   ; verdien til rax blir flyttet til addresse området rbp-0x10 og det blir 0x00
        mov    rax, 0x4746454443424140  ; flytter 0x4746454443424140 til rax
        mov    rdx, 0x4f4e4d4c4b4a4948  ; flytter 0x4f4e4d4c4b4a4948 til rdx
        mov    [rbp-0x30],rax   ; flytter verdien til rax i addresse området rbp-0x30 og blir 0x4746454443424140
        mov    [rbp-0x28],rdx   ; flytter verdien til rdx i addresse området rbp-0x28 og blir 0x4f4e4d4c4b4a4948
        mov    rax, 0x555453525150  ; flytter verdien 0x555453525150 til rax
        mov    [rbp-0x20], rax  ; flytter verdien til rax i addresse området rbp-0x20 og blir 0x555453525150
        jmp    main.loopStart   ; hopper til main.loopstart
    
        main.loop:
            add    DWORD  [rbp-0x10],0x1
    
            main.loopStart: ; hopper hit
                mov    eax,[rbp-0x10]   ; flytter verdien som ligger i [rbp-0x10] inn i eax verdien er 0x00 så eax = 0x00 
                movsxd rdx,eax  ; kopierer eax verdien til rdx så rdx er 0x00
                lea    rax,[rbp-0x30]   ; tar adressen til [rbp-0x30] til rax så rax sin verdi er nå den
                add    rax,rdx  ; legger til rdx i rax i første omgang er den 0x00, så rax er fortsatt [rbp-0x30]
                movzx  eax,BYTE [rax]   ; flytter verdien i den addressen til eax, i dette tilfelle er den 0x40 
                test   al,al    ;
                jne main.loop
    
        mov    eax,[rbp-0x10]
        leave
        ret