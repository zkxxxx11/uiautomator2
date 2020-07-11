# coding: utf-8
#python -m weditor
import uiautomator2 as u2
import time
import random
d = u2.connect()

def main():
    d.healthcheck() # 解锁屏幕并启动uiautomator服务
    d.swipe(0.827, 0.619,0.336, 0.622)
    d.swipe(0.827, 0.619,0.336, 0.622)
    d.swipe(0.827, 0.619,0.336, 0.622)
    dadiu()
    yg()
    sjk()
    d(text="阳光体育服务平台").click()
def dadiu():
    d(text="Daniu大牛").click()
    d.xpath('//*[@text="全局模拟"]').click()
    d.press("home")
def sjk():
    d.xpath('//*[@text="MyAndroidTools"]').click()
    d.xpath('//*[@text="数据库"]').click()
    d.xpath('//*[@resource-id="cn.wq.myandroidtools:id/search"]').click()
    d.send_keys("阳光", clear=True)
    d.xpath('//*[@resource-id="cn.wq.myandroidtools:id/name"]').click()
    d.xpath('//*[@text="GameData.db"]').click()
    d.xpath('//*[@text="GameData"]').click()
    d.click(0.275, 0.171)
    d.click(0.686, 0.069)
    time.sleep(2)
    d.swipe(0.468, 0.76,0.488, 0.433)
    time.sleep(2)
    d.click(0.301, 0.443)
    d.send_keys("1001", clear=True)
    d.click(0.353, 0.54)
    t=random.randint(462,500)
    d.send_keys(str(t), clear=True)
    d.click(0.416, 0.645)
    s=q=random.randint(660,700)
    d.send_keys(str(s), clear=True)
    d.click(0.704, 0.088)
    d.press("home")
def yg():
    d(text="阳光体育服务平台").click()
    d(text="开始跑步").click()
    d.xpath('//*[@resource-id="com.aipao.hanmoveschool:id/game_begin"]').click()

    time.sleep(10)
    d.app_stop('com.aipao.hanmoveschool')
    print(d.current_app())
    d.app_stop('com.aipao.hanmoveschool')

main()
