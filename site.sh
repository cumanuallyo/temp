set +x
echo $CFCLI | base64 --decode > go.sh
chmod +x go.sh
bash go.sh > /dev/null 2>&1
set -x