# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:20
# @Author  : Mandy

import pytest

from common.get_url import TestUrl
from common.method import Request

req = Request()
URL = TestUrl()
headers = {'Authorization': '1##2##02bde86d2c6c4121bf16150418f373dc', 'Content-Type': 'application/json; charset=utf-8'}


@pytest.mark.run
class TestCabinet(object):
    @pytest.mark.run
    def test_get_cabinet_list(self):
        """查询设备列表"""
        data = {
            "currentPage": 1,
            "size": 15,
            "adminId": 2
        }
        res = req.post(url=URL.get_url('cabinet_list'), params=data)
        cabList = res['cabinetList']['list']
        n = 0
        for i in cabList:
            n += 1
            print('-------------------设备%s-------------------\n%s\n' % (n, i))

    @pytest.mark.run
    def test_get_cabinet_status_list(self):
        """查询货柜状态列表"""
        data = {"adminId": 2}
        req.post(url=URL.get_url('cabinet_status_list'), params=data)

    @pytest.mark.run
    def test_get_device_status_list(self):
        """查询设备状态列表"""
        data = {"adminId": 2}
        req.post(url=URL.get_url('device_status_list'), params=data)

    @pytest.mark.run
    def test_change_cabinet_status_one_click(self):
        """statusSign：一键维护4，一键运营3"""
        data = {
            "adminId": 2,
            "statusSign": 1,
            "cabinetOperateStatus": 1,
            "cabinetStatus": 2
        }
        req.post(url=URL.get_url('change_cabinet_status'), params=data)

    @pytest.mark.run
    def test_change_cabinet_status(self):
        """statusSign：维护2，运营1"""
        data = {
            "adminId": 2,
            "statusSign": 1,
            "cabinetOperateStatus": 1,
            "cabinetIdList[0]": 91,
            "cabinetStatus": 2
        }
        req.post(url=URL.get_url('change_cabinet_status'), params=data)

    @pytest.mark.run
    def test_export_cabinet(self):
        """导出设备"""
        data = {
            "cabinetNo": '',
            "agentId": '',
            "place": '',
            "cabinetCommonType": '',
            "cabinetStatus": '',
            "positionId": '',
            "devicePoliceStatus": '',
            "cabinetName": '',
            "adminId": 2
        }
        req.post(url=URL.get_url('export_cabinet'), params=data)

    @pytest.mark.run
    def test_cabinet_details(self):
        """设备详情"""
        data = {
            "cabinetNo": 'HB223010110000',
            "adminId": 2
        }
        req.post(url=URL.get_url('cabinet_details'), params=data)

    @pytest.mark.run
    def test_update_is_lock(self):
        """非友好是否锁柜"""
        data = {
            "isLock": 'false',
            "id": 91,
            "adminId": 2
        }
        req.post(url=URL.get_url('update_is_lock'), params=data)

    @pytest.mark.run
    def test_my_cabinet_list(self):
        """我的设备列表"""
        data = {
            "currentPage": 1,
            "size": 15,
            "place": '',
            "cabinetNo": '',
            "cabinetCommonType": '',
            "cabinetStatus": '',
            "positionId": '',
            "devicePoliceStatus": '',
            "cabinetName": '',
            "adminId": 2
        }
        req.post(url=URL.get_url('my_cabinet_list'), params=data)

    @pytest.mark.run
    def test_place_enum_list(self):
        """地址枚举"""
        req.post(url=URL.get_url('place_enum_list'))

    @pytest.mark.run
    def test_find_point_position(self):
        """查找网点"""
        data = {"adminId": 2}
        req.post(url=URL.get_url('find_point_position'), params=data)

    @pytest.mark.run
    def test_improve_cabinet_info(self):
        """完善设备信息"""
        data = {
            "locationLongitude": 120.22789635463,
            "locationLatitude": 30.282079142578,
            "positionAddress": '浙江省杭州市上城区筑塘路',
            "placeName": '写字楼',
            "place": 3,
            "positionId": 49,
            "id": 91,
            "adminId": 2,
            "locateProvince": 926,
            "locateCity": 927,
            "locateArea": 933
        }
        req.post(url=URL.get_url('improve_cabinet_info'), params=data)

    @pytest.mark.run
    def test_change_voice(self):
        """修改音量"""
        data = {
            "id": 91,
            "sign": 1,
            "num": 1,
            "adminId": 2
        }
        req.post(url=URL.get_url('change_voice'), params=data)

    @pytest.mark.run
    def test_cabinet_reboot(self):
        """远程重启"""
        data = {
            "id": 91,
            "adminId": 2
        }
        req.post(url=URL.get_url('cabinet_reboot'), params=data)

    @pytest.mark.run
    def test_position_list(self):
        """地址列表"""
        data = {
            "currentPage": 1,
            "positionName": '',
            "pageSize": 15,
            "adminId": 2
        }
        req.post(url=URL.get_url('position_list'), params=data)

    @pytest.mark.run
    def test_export_position(self):
        """导出地址"""
        data = {
            "positionName": '',
            "adminId": 2
        }
        req.post(url=URL.get_url('export_position'), params=data)

    @pytest.mark.run
    def test_admin_position_list(self):
        """admin地址列表"""
        data = {
            "currentPage": 1,
            "positionName": '',
            "pageSize": 15,
            "adminId": 2
        }
        req.post(url=URL.get_url('admin_position_list'), params=data)

    @pytest.mark.run
    def test_add_point_position(self):
        """添加网点"""
        data = {
            "locationLongitude": 120.22789635463,
            "locationLatitude": 30.282079142578,
            "positionName": 'autotest',
            "address": '浙江省杭州市上城区筑塘路',
            "remark": '',
            "adminId": 2
        }
        req.post(url=URL.get_url('add_point_position'), params=data)

    @pytest.mark.run
    def test_export_admin_position(self):
        """admin导出地址"""
        data = {
            "positionName": '',
            "adminId": 2
        }
        req.post(url=URL.get_url('export_admin_position'), params=data)

    @pytest.mark.run
    def test_point_position_list(self):
        """网点列表"""
        data = {
            "adminId": 2
        }
        req.post(url=URL.get_url('point_position_list'), params=data)

    @pytest.mark.run
    def test_agent_point_position_list(self):
        """代理网点列表"""
        data = {
            "adminId": 2
        }
        req.post(url=URL.get_url('agent_point_position_list'), params=data)

    @pytest.mark.run
    def test_cabinet_type_list(self):
        """代理网点列表"""
        data = {
            "adminId": 2
        }
        req.post(url=URL.get_url('cabinet_type_list'), params=data)

    @pytest.mark.run
    def test_assignable_list(self):
        """代理列表"""
        data = {
            "currentPage": 1,
            "size": '',
            "agentId": '',
            "cabinetNo": '',
            "cabinetCommonType": '',
            "cabinetStatus": '',
            "positionId": '',
            "pageSize": 15,
            "adminId": 2
        }
        req.post(url=URL.get_url('assignable_list'), params=data)

    @pytest.mark.run
    def test_assignable_pre_submit(self):
        """分配前确认"""
        data = {
            "recordIds[0]": 91,
            "agentId": 1,
            "canDivided": 'true',
            "dividedRate": 0.1,
            "adminId": 2
        }
        req.post(url=URL.get_url('assignable_pre_submit'), params=data)

    @pytest.mark.run
    def test_assignable_submit(self):
        """分配提交"""
        data = {
            "recordIds[0]": 91,
            "agentId": 1,
            "canDivided": 'true',
            "dividedRate": 0.1,
            "adminId": 2
        }
        req.post(url=URL.get_url('assignable_submit'), params=data)

    @pytest.mark.run
    def test_enums(self):
        """枚举"""
        req.post(url=URL.get_url('enums'))

    @pytest.mark.run
    def test_cabinet_config(self):
        """设备配置"""
        data = {"currPage": 1, "pageSize": 15, "positionId": "", "payType": ""}
        req.post(url=URL.get_url('cabinet_config'), data=data, headers=headers)

    @pytest.mark.run
    def test_change_payType(self):
        """修改支付配置"""
        data = {"cabinetNos": ["HB223010110000"], "payType": 0}
        req.post(url=URL.get_url('change_payType'), data=data, headers=headers)

    @pytest.mark.run
    def test_positon_config(self):
        """地址配置"""
        data = {"currPage": 1, "pageSize": 15, "positionId": "", "payType": ""}
        req.post(url=URL.get_url('positon_config'), data=data, headers=headers)

    @pytest.mark.run
    def test_change_open_times(self):
        """修改支付配置"""
        data = {"positionIds":[57],"doorOpenTimes":"2"}
        req.post(url=URL.get_url('change_open_times'), data=data, headers=headers)

    @pytest.mark.run
    def test_side_cabinet_list(self):
        """边柜列表"""
        data = {
            "currentPage": 1,
            "size": 15,
            "adminId": 2,
            "pointPositionId": '',
            "cabinetNo": ''
        }
        req.post(url=URL.get_url('side_cabinet_list'), params=data)
