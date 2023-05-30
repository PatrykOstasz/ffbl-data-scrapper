#this script is for installing dependencies

Write-Host "Downloading python libraries"

Write-Host "Updating pip"
python.exe -m pip install --upgrade pip

pip3.exe install -r configuration/requirements.txt
