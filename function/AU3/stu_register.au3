BlockInput(1) ;禁止用户键盘输入
sleep(1000)
MouseClick("left",766,83,1,1) ;点击空白处
MouseClick("left",1327,85,1,50) ;注册
sleep(1000)
MouseClick("left",585,268,1,1);账号
Send("^a")
Send("{Del}")
sleep(1000)
Send("autotest11")
MouseClick("left",569,328,1,1);密码
Send("^a")
Send("{Del}")
sleep(1000)
Send("12345678")
MouseClick("left",570,390,1,1);确认密码
Send("^a")
Send("{Del}")
sleep(1000)
Send("12345678")
MouseClick("left",565,452,1,1);验证码
sleep(1000)
Send("hrv7")
MouseClick("left",569,511,1,1);电子邮箱
Send("^a")
Send("{Del}")
sleep(1000)
Send("63299i5576@qq.com")
sleep(1000)
MouseClick("left",686,641,1,1);点击注册
MouseClick("left",1080,590,1,20);移开鼠标

