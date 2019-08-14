#! /bin/bash
git config credentials.helper store
git add .
git commit -m "Automatic commit"
git push

ssh bloomingmath@ssh.pythonanywhere.com "cd mysite && git pull"

source venv/bin/activate
python reload.py
