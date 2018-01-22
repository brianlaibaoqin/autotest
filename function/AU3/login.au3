BlockInput(1) ;禁止用户键盘输入
sleep(1000)
MouseClick("left",766,83,1,1) ;点击空白处
sleep(1000);等待1S
MouseClick("left",1285,87,1,1);点击登录按钮
sleep(1000)
MouseClick("left",572,295,1,1);点击账号输入框
Send("^a")
Send("{Del}")
sleep(2000)
Send("autotest11")
sleep(1000)
MouseClick("left",554,366,1,1);点击密码输入框
Send("^a")
Send("{Del}")
sleep(2000)
Send("12345678")
sleep(1000)
MouseClick("left",683,438,1,1);点击登录按钮
sleep(2000)
MouseClick("left",1323,85,1,1) ;点击用户名
sleep(1000)
MouseClick("left",1318,113,1,30) ;点击个人中心

