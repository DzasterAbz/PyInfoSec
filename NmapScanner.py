import nmap
import sys

targetIP = str(sys.argv[1])
ports = [20,21,22,23,25,53,67,68,80,110,135,139,443,3389]
nmapscan = nmap.PortScanner()
print("\nScanning ",targetIP,".\n for the important ports.\n")
for port in ports:
    portscan = nmapscan.scan(targetIP,str(sys.argv[1]))
    print("Port ",port," is ",portscan['scan'][targetIP]['tcp'][port]['state'])
print("\nHost ",targetIP," is ",portscan['scan'][target]['status']['state']) 

