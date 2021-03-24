# !/bin/sh
file_name="fibo.py"
env=$PWD"/"$file_name
touch $env
echo $env > .env
start fibo_test.gh
