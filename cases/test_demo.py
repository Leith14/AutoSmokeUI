#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_demo.py
# @Author: Xuewen Lei
# @Date  : 2021/9/7
# @Desc  :
import allure

import uiautomator2 as u2

from devices_info import DevicesInfo


class TestDemo:
    def setup_class(self):
        self.d = u2.connect(DevicesInfo.MPC_SERIALNO)
        self.d.implicitly_wait(5)

    def teardown_class(self):
        pass

    def setup(self):
        # Only enter on Homepage
        self.sess = self.d.session("com.android.car.overview")

    def teardown(self):
        # reset com.ff.vehicle
        self.d.app_clear("com.ff.vehicle")

    @allure.step
    def test_connect_wifi(self):
        # connect wifi
        # click vehicle button
        self.d.xpath(
            '//*[@resource-id="com.android.systemui:id/ff_car_navigation_bar_button_vehicle"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
        # click settings button
        self.d(text="SETTINGS").click()
        self.d(resourceId="com.ff.vehicle:id/tv_list_title", text="Connectivity").click()
        self.d(resourceId="com.ff.vehicle:id/wifi_name_tv", text="FF-Web").click()
        # input password for wifi FF-Web
        self.d(description="f").click()
        self.d(description="f").click()
        self.d(description="c").click()
        self.d(description="n").click()
        self.d(description=".").click()
        self.d(description="2").click()
        self.d(description="0").click()
        self.d(description="2").click()
        self.d(description="0").click()
        self.d(resourceId="com.ff.vehicle:id/ok_btn").click()
        self.d.sleep(5)
        text = self.d(resourceId="com.ff.vehicle:id/wifi_state_tv").get_text()
        assert "Edit" == text

    # @pytest.mark.dependency(depends=["TestDemo::test_connect_wifi"])
    @allure.step
    def test_disconnect_wifi(self):
        # disconnect wifi
        self.d.xpath(
            '//*[@resource-id="com.android.systemui:id/ff_car_navigation_bar_button_vehicle"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
        self.d(text="SETTINGS").click()
        self.d(resourceId="com.ff.vehicle:id/tv_list_title", text="Connectivity").click()
        self.d(resourceId="com.ff.vehicle:id/wifi_state_tv", text="Edit").click()
        self.d(resourceId="com.ff.vehicle:id/ok_btn").click()

    def test_shell(self):
        print(self.d.shell("ls -l"))
        shell_response = self.d.shell("ifconfig")
        str_sr = str(shell_response)
        assert "eth0" in str_sr and "inet addr:172.26.200.2" in str_sr
        # r = self.d.shell("ifconfig", stream=True)
        # # r: requests.models.Response
        # try:
        #     for line in r.iter_lines():  # r.iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
        #         print(line.decode('utf-8'))
        # finally:
        #     r.close()  # this method must be called
