level=$1
number=$2

echo $level
echo $number
result=($(ls $level/$number; echo $?))

if [[ $result == 0 ]]; then
    echo "Directory exists"
else
    mkdir $level/$number &&
    find . -type f -name "$number.*" -exec mv {} $level/$number \;
fi





