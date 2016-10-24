ssh zs "pkill python"
scp ./* zs:Alex_Personal_Bot/
ssh zs "nohup python Alex_Personal_Bot/main.py >/dev/null 2>&1 &"
