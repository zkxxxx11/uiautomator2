import uiautomator2 as u2
import time
d = u2.connect()
from time import sleep
d.press("home")

d.swipe(0.827, 0.619,0.336, 0.622)
d.swipe(0.827, 0.619,0.336, 0.622)
d(text="微信").click()
d(resourceId="com.tencent.mm:id/wc").click()
d(resourceId="com.tencent.mm:id/dy_").click()
sleep(3)


d.click(0.6, 0.56)
d.click(0.6, 0.56)
d.click(0.6, 0.56)
sleep(2)
d.click(0.363, 0.732)
sleep(1)
d.click(0.217, 0.853)
d.click(0.369, 0.443)
