from exert import adb
import os
import unittest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_path(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        d = adb.get_devices()[0]
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = adb.get_version(d)
        desired_caps['deviceName'] = d
        desired_caps['autoGrantPermissions'] = True  # 自动赋权
        desired_caps['noReset'] = True  # 不重置，避免多次登录
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        # 如果有 apk 包，可以代替 app 的配置参数，直接通过 apk 读取信息。
        # desired_caps['app'] = get_path('your.apk')
        # 部分 APP 进去后会马上切换 Activity 所以需要设置这个值用 adb shell dumpsys window windows 找到特定的 Activity
        # desired_caps['appWaitActivity'] = ''
        # desired_caps['appWaitPackage'] = ''
        # desired_caps['appWaitDuration'] = ''

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_simple_actions(self):
        '''
        '''
        el = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath('''//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]''')
        )
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
