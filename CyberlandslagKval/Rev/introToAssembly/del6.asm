    main:                         
        endbr64 
        push   rbp  ; pusher rbp på stacken
        mov    rbp,rsp  ; flytter rsp
        sub    rsp,0x20 ; flytter rsp pointeren ned 0x20 så stacken har størrelse 0x20 
        mov    [rbp-0x14],edi ; argc flytter argc inn i [rbp-0x14]
        mov    [rbp-0x20],rsi ; argv flytter argv inn i [rbp-0x20]
        mov    rax,[rbp-0x20] ; flytter den verdien inn i rax, altså rsi som er bruker input
        mov    rax,[rax+0x8]  ; flytter de 8 første bytesene fra userinput til rax
        mov    [rbp-0x8],rax  ; flytter disse bytesene til [rbp-0x8]
        mov    rax,[rbp-0x8]    ; flytter disse bytesene tilbake til rax  
        mov    rdi,rax  ; flytter disse inn i rdi
        call   getLength    ; kaller på funksjonen getlength
    
        cmp    eax, 0x1d ; sjekker om user inputen er like lang som 0x1d
        jne    main.sry ; hvis de ikke er lik så hopper den til main.sry
    
        mov    [rbp-0xc],eax ; flytter denne verdien fra eax til addresse området [rbp-0xc]
        mov    edx,[rbp-0xc] ; flytter addresssen inn i edx
        mov    rax,[rbp-0x8]  ; flytter addressen inn i rax 
        mov    esi,edx  ; flytter den addressen altså [rbp-0xc] inn i esi                  
        mov    rdi,rax  ; flytter den addressen altså [rbp-0x8] inn i rdi 
        call   checkCorrect ; caller på funksjonen checkCorrect             
    
        test   eax,eax                  
        jne    main.sry
    
        main.nice:  ; neste funksjonen 
            mov rax, 0x00216563696e
            mov [rbp-0x20], rax
            lea rax,[rbp-0x20]      
            mov rdi, 1       ; stdout
            lea rsi, [rax]   ; *buffer
            mov rdx, 0x5     ; len
            mov rax, 1       ; write
            syscall
    
            jmp    main.end
    
        main.sry: ; her blir sry! printet ut  
            mov rax, 0x0021797273 
            mov [rbp-0x20], rax
            lea rax,[rbp-0x20]      
            mov rdi, 1       ; stdout
            lea rsi, [rax]   ; *buffer
            mov rdx, 0x5     ; len
            mov rax, 1       ; write
            syscall
    
        main.end:
            mov    eax,0x0
            leave  
            ret    
    
    getLength:
        push   rbp ; pusher den pointeren til stacken
        mov    rbp,rsp  ; pusher denne rsp til stacken
        mov    [rbp-0x18],rdi   ; flytter verdien fra rdi som er de 8 første bytesene inn addresse området [rbp-0x18]
        mov    DWORD  [rbp-0x4],0x0 ; lagrer 0x0 i rbp-0x4 
        jmp    getLength.loopStart  ; hopper til getLength.loopStart
    
        getLength.loop:
            add    DWORD  [rbp-0x4],0x1 ; adderer 0x1 på counteren
    
            getLength.loopStart:
                mov    eax,[rbp-0x4]    ; flytter 0x0 inn i eax
                movsxd rdx,eax  ; kopierer eax inn i rdx, i første loop 0x0 dette blir en slags counter
                mov    rax,[rbp-0x18]   ; flytter verdien fra [rbp-0x18] som er de 8 første bytesene fra userinput inn i rax
                add    rax,rdx  ; adderer counteren inn i rax. 
                movzx  eax,BYTE [rax]   ; flytter byten inn i eax som peker på rax. 
                test   al,al    ; sjekker om eax er 0x0
                jne getLength.loop  ;   hvis de ikke er lik så hopper den til getLength.loop
    
        mov    eax,[rbp-0x4]    ; flytter counteren til eax som er altså vil være lengen på  
        pop    rbp  ; pointeren blir fjernet fra stacken
        ret ; her blir eax returnet
    
    checkCorrect: 
        endbr64 ; nokka sikkerhets greia skit 
        push   rbp ; pusher rbp på stacken 
        mov    rbp,rsp  ; flytter verdien til rsp til rbp
        sub    rsp,0x50 ; trekker fra 0x50 fra rsp, så stacken har størrelse 0x50 
        mov    [rbp-0x48],rdi   ; flytter verdien fra rdi som er de 8 første bytsene fra user input til addresse området til [rbp-0x48]
        mov    [rbp-0x4c],esi   ; flytter verdien fra esi til addresse området til [rbp-0x4c]
        mov    rax, fs:0x28 ; flytter den lagrende verdien i fs til rax
        mov    [rbp-0x8],rax    ; flytter verdien fra rax til addresse området [rbp-0x8]
        xor    eax,eax ; resetter verdien eax til 0  
        mov    rax,0x3d7d3c726e68656f   ; flytter 0x3d7d3c726e68656f til rax 
        mov    rdx,0x70656a387d3c387d   ; flytter 0x70656a387d3c387d til rdx
        mov    [rbp-0x30],rax   ; flytter verdien 0x3d7d3c726e68656f til [rbp-0x30]
        mov    [rbp-0x28],rdx   ; flytter verdien 0x70656a387d3c387d til [rbp-0x28]
        mov    rax,0x7b6e56643d563856   ; flytter verdien 0x7b6e56643d563856 til rax
        mov    [rbp-0x20],rax   ; lagrer denne verdien inn i addresse området [rbp-0x20]
        mov    DWORD  [rbp-0x18],0x287d3d3a ; lagrer 0x287d3d3a inn i [rbp-0x18]
        mov    WORD  [rbp-0x14],0x74    ; flytter 0x74 inn i addresse [rbp-0x14]
        mov    DWORD  [rbp-0x34],0x0    ; flytter 0x0 inn i addresse [rbp-0x34]
        jmp    checkCorrect.whileCondition  ; hopper til checkCorrect.whileCondition
    
        checkCorrect.loop:
            mov    eax,[rbp-0x34] ; flytter verdien fra [rbp-0x34] som er en counter så i første runde er den 0x0 inn i eax  
            movsxd rdx,eax  ; kopierer verdien fra eax i rdx, som i første runde er 0x0 og er counteren 
            mov    rax,[rbp-0x48] ; flytter verdien i [rbp-0x48] som er de første 8 bytesene fra userinput inn i rax  
            add    rax,rdx ; adderer counteren til verdien i [rbp-0x48] som er de første 8 bytesene fra userinput
            movzx  eax,BYTE  [rax] ; kopierer byten som blir pekt på inn i eax som er i første runde [rbp-0x48]
            xor    eax,0x9  ; xorer 0x9 med byten som blir pekt på som er i første runde [rbp-0x48]
            mov    edx,eax  ; flytter verdien eax inn i edx, som altså er den xoret verdien til første byten i userinput i første runde
            mov    eax,DWORD  [rbp-0x34]    ; flytter verdien fra [rbp-0x34] som er counteren inn i eax
            cdqe   ; gjør eax til 64 bit
            movzx  eax,BYTE  [rbp+rax*1-0x30]   ; kopierer den byten i [rbp+rax*1-0x30] inn i eax, som er i første runde [rbp-0x30] denne verdien er 0x3d7d3c726e68656f
            cmp    dl,al ; sammenlikner edx og eax altså den xoret verdien av userinput med 0x9 med verdien lagret i al som er rax altså sammenlignes 6f med først bytes i userinput
            je     checkCorrect.incrementCounter; hopper til checkCorrect.incrementCounter hvis de er lik
    
            mov    eax,0x1 ; hvis de ikke er riktig så blir 0x1 flyttet til eax 
            jmp    checkCorrect.retWrong ; også hopper vi til checkCorrect.retWrong
    
            checkCorrect.incrementCounter:
                add    DWORD  [rbp-0x34],0x1 ; adderer 0x1 på counteren
    
            checkCorrect.whileCondition:
                mov    eax,[rbp-0x34]  ; flytter verdien fra [rbp-0x34] som er 0x0 til eax
                cmp    eax,[rbp-0x4c]   ; sjekker om eax er lik verdien i [rbp-0x4c] som 
                jl     checkCorrect.loop ; hvis den er mindre så hopper vi til checkCorrect.loop
    
            mov    eax,0x0
            
            checkCorrect.retWrong:
                mov    rdx,[rbp-0x8] ; flytter verdien lagret i [rbp-0x8] inn i rdx som er den lagrede verdien i fs:0x28
                sub    rdx,fs:0x28 ; rdx blir trukket fra den lagrede verdien i fs;0x28
    
        checkCorrect.end:
            leave  ; slutten på funksjonen
            ret  ; returnerer eax