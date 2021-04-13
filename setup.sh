# installing pip
sudo apt install python3-pip

pip3 --version

# seting up venv
pip3 install -y virtualenv

python3 -m venv env
echo "setup done for virtualenv"

# activate venv
source env/bin/activate

# install requirements
pip3 install -r requirements.txt


