from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import random

FLAG = "flag{REDACTED}"
FLAGNUM = bytes_to_long(FLAG.encode())
G = 2
Q = 232317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
R = random.randint(2,Q)
X = pow(G,FLAGNUM,Q)

def interaction():
    a = pow(G,R,Q)
    print(f"x = {X}")
    print(f"a = {a}")
    print("Give me your challenge: ")
    try:
        c = int(input("> "))
    except:
        print("Invalid input")
        exit(0)
    z = R + c*FLAGNUM
    print(f"z = {z}")

def main():
    print("Welcome! I know the flag and I can prove it without revealing it!")
    while True:
        try:
            print("What do you want to do?")
            print("1) Make me prove it")
            print("2) Tell me my flag (impossible)")
            print("3) Stop talking")
            choice = int(input("> "))    
        except:
            print("Invalid input")
            exit(0)

        if choice == 1:
            interaction()
            continue
        elif choice == 2:
            print("Okay what is it then?")
            try:
                flag_guess = input("> ")
                if flag_guess == FLAG:
                    print("Wow, I should study more")
                else:
                    print("Told you it was impossible!")
                    continue
            except:
                print("Invalid input")
        exit(0)
main()