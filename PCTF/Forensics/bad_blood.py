import socket
import time

def send_data(ip, port, data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(data.encode('utf-8'))
            time.sleep(1)  # Optional: Wait a moment after sending
            response = s.recv(1024)
            print(f"Received: {response.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")

# answers = [
#     "Cobalt Strike",
#     "Metasploit",
#     "Empire",
#     "Pupy",
#     "Gh0st RAT",
#     "Parrot",
#     "Agent Tesla",
#     "AsyncRAT",
#     "NETWIRE",
#     "Zollard"
# ]

# answers = ['Armitage','Starkiller']

answers = ['Sliver']
for answer in answers:
    if __name__ == "__main__":
        target_ip = 'chal.competitivecyber.club'
        target_port = 10001

        questions_answers = [
            ("Q1. Forensics found post exploitation activity present on system, network and security event logs. What post-exploitation script did the attacker run to conduct this activity?\nExample answer: PowerView.ps1\n>> ", "Invoke-P0wnedshell.ps1"),
            ("Q2. Forensics could not find any malicious processes on the system. However, network traffic indicates a callback was still made from his system to a device outside the network. We believe jack used process injection to facilitate this. What script helped him accomplish this?\nExample answer: Inject.ps1\n>> ", "Invoke-UrbanBishop.ps1"),
            ("Q3. We believe Jack attempted to establish multiple methods of persistence. What windows protocol did Jack attempt to abuse to create persistence?\nExample answer: ProtoName\n>> ", "WinRM"),
            ("Q4. Network evidence suggest Jack established connection to a C2 server. What C2 framework is jack using?\nExample answer: C2Name\n>> ", answer),
        ]

        for question, answer in questions_answers:
            print(question)
            input("Press Enter when ready to send the answer...")
            send_data(target_ip, target_port, answer)
            print("That makes sense.\n")
