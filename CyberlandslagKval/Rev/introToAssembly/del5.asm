    main:
        endbr64 
        push   rbp  ; plasserer rbp på stacken
        mov    rbp,rsp  ; flytter adressen rsp til rbp
        sub    rsp,0x60 ; trekker fra 0x60 fra rsp 
        mov    rax, [rsi+8] ; flytter input til rax 
        mov    [rbp-0x48],rax   ; lagrer denne input verdien i addressen rpb-0x48 
        mov    QWORD [rbp-0x50],0x1d   ; flytter 0x1d inn i addresse området [rbp-0x50]                       ; Length, i
        mov    rax, fs:0x28 ; henter den lagrende verdien i fs flytter til rax
        mov    [rbp-0x8],rax    ; lagrer denne i addresse området [rbp-0x8]
        xor    eax,eax  ; nullstiller eax
        mov    rax,0x4d42434041464744   ; flytter 0x4d42434041464744 til rax
        mov    rdx,0x554a4b48494e4f4c   ; flytter 0x554a4b48494e4f4c til rdx
        mov    [rbp-0x30],rax   ; lagrer rax i addresse området [rbp-0x30], altså er 0x4d42434041464744 lagret her
        mov    [rbp-0x28],rdx   ; lagrer rdx i addresse området [rbp-0x20], altså er 0x554a4b48494e4f4c lagret her
        mov    rax,0x5d52535051565754   ; flytter 0x5d52535051565754 til rax
        mov    [rbp-0x20],rax   ; lagrer rax i addresse området [rbp-0x20], altså verdien 0x5d52535051565754
        mov    DWORD  [rbp-0x18],0x67645f5c ; lagrer verdien 0x67645f5c i addresse området [rbp-0x18]
        mov    WORD  [rbp-0x14],0x66    ; lagrer verdien 0x66 i addresse området [rbp-0x14]
        mov    DWORD  [rbp-0x34],0x0                ; counter lagrer verdien 0x0 i addresse området [rbp-0x34]
        jmp    main.whileCondition  ; hopper til main.whileCondition 
    
        main.loop:  ; hoppet hit fra main.whileCondition
            mov    eax,[rbp-0x34]   ; flytter verdien fra counteren lagret i addresse området [rbp-0x34] som i første runde er 0x0
            movsxd rdx,eax  ; kopierer verdien til eax, som er counteren, til rdx
            mov    rax,[rbp-0x48]   ; flytter verdien i addresse området [rbp-0x48] til rax, som er i dette tilfelle userinput
            add    rax,rdx  ; legger til rdx, altså verdien til counteren
            movzx  eax,BYTE  [rax]  ; flytter første byte i rax til eax, som kommer fra user input
            xor    eax,0x5  ; xor eax med 0x5
            mov    edx,eax  ; flytter den xoret verdien til edx
            mov    eax,DWORD  [rbp-0x34]    ; flytter verdien lagret i [rbp-0x34] som er counteren i eax 
            cdqe   ; flytter de 32 bitsene i eax, til de 32 øvereste bitsene i rax
            movzx  eax,BYTE  [rbp+rax*1-0x30]   ; flytter verdien til [rbp+rax*1-0x30] som er i første runde er [rpb-0x30] og her er denne lagret 0x4d42434041464744 i siste runde vil dette være -0x1d
            cmp    dl,al    ; sjekker om den xoret verdien er lik eax verdien
            je     main.incrementCounter    ; hvis de er lik så hopper den til main.incrementCounter
    
            mov    eax,0x1  ; ellers blir eax satt til 0x1
            jmp    main.retWrong    ; og vi hopper til main.retWrong
    
            main.incrementCounter:
                add    DWORD  [rbp-0x34],0x1
    
            main.whileCondition:    ; hoppet hit fra main
                mov    eax,[rbp-0x34]   ; flytter den lagrede verdien i [rbp-0x34] til eax, altså 0x0, sistste verdien vil være 0x1d
                cmp    eax,[rbp-0x50]   ; sammenlikner denne verdien med verdien i [rbp-0x50], altså 0x1d
                jl     main.loop    ; hopper til main.loop hvis eax er mindre enn [rbp-0x50], vil gjøre det helt til eax er 0x1d
    
            mov    eax,0x0
            
            main.retWrong:
                mov    rdx,[rbp-0x8]    ; rdx får verdien til den lagrede verdien
                sub    rdx,fs:0x28  ; og rdx blir trukket fra den verdien så den forsvinner
    
        main.end:
            leave  ; så går funksjonen hit og tømmer stacken
            ret ; så returnere den eax