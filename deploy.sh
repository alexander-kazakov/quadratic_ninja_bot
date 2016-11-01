ssh zs "pkill python"
scp ./* zs:Alex_CST_Bot/
ssh zs "nohup python Alex_CST_Bot/main.py >/dev/null 2>&1 &"
