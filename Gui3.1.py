# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import gloV
import Main
import Community
import ShopHospital

class Ui_DemoDia(object):
    isReadHelp = False
    isReadCommunity = False
    isReadShop = False
    isReadHospital = False

    def setupUi(self, DemoDia):
        DemoDia.setObjectName("DemoDia")
        DemoDia.resize(1090, 648)
        self.cancelAndOk = QtWidgets.QDialogButtonBox(DemoDia)
        self.cancelAndOk.setGeometry(QtCore.QRect(900, 590, 164, 32))
        self.cancelAndOk.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.cancelAndOk.setObjectName("cancelAndOk")
        self.helpButton = QtWidgets.QPushButton(DemoDia)
        self.helpButton.setGeometry(QtCore.QRect(240, 590, 113, 32))
        self.helpButton.setObjectName("helpButton")
        self.console = QtWidgets.QTextBrowser(DemoDia)
        self.console.setGeometry(QtCore.QRect(10, 10, 711, 551))
        self.console.setObjectName("console")
        self.communityButton = QtWidgets.QPushButton(DemoDia)
        self.communityButton.setGeometry(QtCore.QRect(760, 530, 141, 32))
        self.communityButton.setObjectName("communityButton")
        self.groupBox = QtWidgets.QGroupBox(DemoDia)
        self.groupBox.setGeometry(QtCore.QRect(750, 10, 321, 511))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lngKm = QtWidgets.QLineEdit(self.groupBox)
        self.lngKm.setGeometry(QtCore.QRect(120, 30, 31, 21))
        self.lngKm.setObjectName("lngKm")
        self.latKm = QtWidgets.QLineEdit(self.groupBox)
        self.latKm.setGeometry(QtCore.QRect(120, 60, 31, 21))
        self.latKm.setObjectName("latKm")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 21, 16))
        self.label_4.setObjectName("label_4")
        self.paraFamilyMax = QtWidgets.QLineEdit(self.groupBox)
        self.paraFamilyMax.setGeometry(QtCore.QRect(210, 110, 91, 21))
        self.paraFamilyMax.setObjectName("paraFamilyMax")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 181, 16))
        self.label_6.setObjectName("label_6")
        self.paraHospitalRemarkCut = QtWidgets.QLineEdit(self.groupBox)
        self.paraHospitalRemarkCut.setGeometry(QtCore.QRect(210, 140, 51, 21))
        self.paraHospitalRemarkCut.setObjectName("paraHospitalRemarkCut")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 161, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 151, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 141, 16))
        self.label_10.setObjectName("label_10")
        self.paraPayIncome = QtWidgets.QLineEdit(self.groupBox)
        self.paraPayIncome.setGeometry(QtCore.QRect(190, 200, 31, 20))
        self.paraPayIncome.setObjectName("paraPayIncome")
        self.paraPayPrice = QtWidgets.QLineEdit(self.groupBox)
        self.paraPayPrice.setGeometry(QtCore.QRect(190, 220, 31, 20))
        self.paraPayPrice.setObjectName("paraPayPrice")
        self.paraPayRongjilv = QtWidgets.QLineEdit(self.groupBox)
        self.paraPayRongjilv.setGeometry(QtCore.QRect(190, 240, 31, 20))
        self.paraPayRongjilv.setObjectName("paraPayRongjilv")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(0, 280, 131, 16))
        self.label_11.setObjectName("label_11")
        self.paraCommunityPay = QtWidgets.QLineEdit(self.groupBox)
        self.paraCommunityPay.setGeometry(QtCore.QRect(120, 280, 31, 21))
        self.paraCommunityPay.setObjectName("paraCommunityPay")
        self.paraCommunityFamily = QtWidgets.QLineEdit(self.groupBox)
        self.paraCommunityFamily.setGeometry(QtCore.QRect(260, 280, 31, 21))
        self.paraCommunityFamily.setObjectName("paraCommunityFamily")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(160, 280, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 320, 251, 16))
        self.label_13.setObjectName("label_13")
        self.paraDemandScore = QtWidgets.QLineEdit(self.groupBox)
        self.paraDemandScore.setGeometry(QtCore.QRect(270, 320, 31, 21))
        self.paraDemandScore.setObjectName("paraDemandScore")
        self.paraDemandShop = QtWidgets.QLineEdit(self.groupBox)
        self.paraDemandShop.setGeometry(QtCore.QRect(270, 340, 31, 21))
        self.paraDemandShop.setObjectName("paraDemandShop")
        self.paraFinalDemand = QtWidgets.QLineEdit(self.groupBox)
        self.paraFinalDemand.setGeometry(QtCore.QRect(60, 370, 31, 21))
        self.paraFinalDemand.setObjectName("paraFinalDemand")
        self.paraFinalCompete = QtWidgets.QLineEdit(self.groupBox)
        self.paraFinalCompete.setGeometry(QtCore.QRect(170, 370, 31, 21))
        self.paraFinalCompete.setObjectName("paraFinalCompete")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(80, 340, 161, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 370, 51, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(100, 370, 81, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(10, 470, 91, 18))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(10, 410, 131, 18))
        self.label_18.setObjectName("label_18")
        self.paraYearMin = QtWidgets.QLineEdit(self.groupBox)
        self.paraYearMin.setGeometry(QtCore.QRect(140, 410, 51, 25))
        self.paraYearMin.setObjectName("paraYearMin")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(210, 410, 21, 18))
        self.label_19.setObjectName("label_19")
        self.paraYearMax = QtWidgets.QLineEdit(self.groupBox)
        self.paraYearMax.setGeometry(QtCore.QRect(240, 410, 51, 25))
        self.paraYearMax.setObjectName("paraYearMax")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 470, 101, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.computeButton = QtWidgets.QPushButton(DemoDia)
        self.computeButton.setGeometry(QtCore.QRect(410, 590, 121, 32))
        self.computeButton.setObjectName("computeButton")
        self.shopHospitalButton = QtWidgets.QPushButton(DemoDia)
        self.shopHospitalButton.setGeometry(QtCore.QRect(940, 530, 131, 32))
        self.shopHospitalButton.setObjectName("shopHospitalButton")

        self.retranslateUi(DemoDia)
        self.cancelAndOk.accepted.connect(DemoDia.accept)
        self.cancelAndOk.rejected.connect(DemoDia.reject)

        self.helpButton.clicked.connect(self.help_button)
        self.computeButton.clicked.connect(self.sf)

        self.communityButton.clicked.connect(self.community_button)
        self.shopHospitalButton.clicked.connect(self.shopHospital_button)

        QtCore.QMetaObject.connectSlotsByName(DemoDia)

    def retranslateUi(self, DemoDia):
        _translate = QtCore.QCoreApplication.translate
        DemoDia.setWindowTitle(_translate("DemoDia", "DemoDia"))
        self.helpButton.setText(_translate("DemoDia", "Help.csv"))
        self.communityButton.setText(_translate("DemoDia", "Community.csv"))
        self.groupBox.setTitle(_translate("DemoDia", "参数调节"))
        self.label.setText(_translate("DemoDia", "方格 沿经度长度："))
        self.label_2.setText(_translate("DemoDia", "方格 沿纬度长度："))
        self.lngKm.setText(_translate("DemoDia", "2"))
        self.latKm.setText(_translate("DemoDia", "2"))
        self.label_3.setText(_translate("DemoDia", "Km"))
        self.label_4.setText(_translate("DemoDia", "Km"))
        self.paraFamilyMax.setText(_translate("DemoDia", "3000"))
        self.label_5.setText(_translate("DemoDia", "现有户数 上限："))
        self.label_6.setText(_translate("DemoDia", "医院点评数 切分点："))
        self.paraHospitalRemarkCut.setText(_translate("DemoDia", "10"))
        self.label_7.setText(_translate("DemoDia", "居民支付能力="))
        self.label_8.setText(_translate("DemoDia", "可支配收入评分 *"))
        self.label_9.setText(_translate("DemoDia", "+ 小区售价评分 *"))
        self.label_10.setText(_translate("DemoDia", "+ 容积率评分 *"))
        self.paraPayIncome.setText(_translate("DemoDia", "1"))
        self.paraPayPrice.setText(_translate("DemoDia", "6"))
        self.paraPayRongjilv.setText(_translate("DemoDia", "3"))
        self.label_11.setText(_translate("DemoDia", "居民支付能力*"))
        self.paraCommunityPay.setText(_translate("DemoDia", "1"))
        self.paraCommunityFamily.setText(_translate("DemoDia", "2"))
        self.label_12.setText(_translate("DemoDia", "+居民数量*"))
        self.label_13.setText(_translate("DemoDia", "(居民支付能力+居民数量*2) *"))
        self.paraDemandScore.setText(_translate("DemoDia", "9"))
        self.paraDemandShop.setText(_translate("DemoDia", "1"))
        self.paraFinalDemand.setText(_translate("DemoDia", "1"))
        self.paraFinalCompete.setText(_translate("DemoDia", "0.3"))
        self.label_14.setText(_translate("DemoDia", "+ 相关行业支持*"))
        self.label_15.setText(_translate("DemoDia", "需求*"))
        self.label_16.setText(_translate("DemoDia", "- 竞争*"))
        self.label_17.setText(_translate("DemoDia", "当前日期："))
        self.label_18.setText(_translate("DemoDia", "竣工时间范围："))
        self.paraYearMin.setText(_translate("DemoDia", "1900"))
        self.label_19.setText(_translate("DemoDia", "至"))
        self.paraYearMax.setText(_translate("DemoDia", "2500"))
        self.lineEdit_3.setText(_translate("DemoDia", "2016/4/7"))
        self.computeButton.setText(_translate("DemoDia", "生成TableAu"))
        self.shopHospitalButton.setText(_translate("DemoDia", "Shop-Hos.csv"))

    def help_button(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        print(path)
        if len(path[0]) <= 0:
            self.console.append("未选择任何文件.")
            self.isReadHelp = False
            return -1
        if path[0][-4:] != ".csv":
            self.console.append(str(path[0]) + " 不是CSV文件")
            self.isReadHelp = False
            return -2

        # ---------- 辅助信息 清洗与检验
        fileHelpName = path[0]
        gloV.LNG_MIN = gloV.CN_LNG_MIN
        gloV.LNG_MAX = gloV.CN_LNG_MAX
        gloV.LAT_MIN = gloV.CN_LAT_MIN
        gloV.LAT_MAX = gloV.CN_LAT_MAX
        gloV.incomeList = {}
        gloV.incomeListKeys = []

        returnHelp = Main.readHelpCSV(fileHelpName)
        if returnHelp < 0:
            self.console.append(str(path[0]) + " 文件读取错误, 代码:" + str(returnHelp))
            self.console.append("-1表示文件不存在, -2表示文件编码不明, -3表示人均可支配收入不是数字")
            self.console.append(" ")
            self.isReadHelp = False
            return returnHelp

        self.isReadHelp = True
        self.console.append("Help.csv文件 <" + str(path[0]) + "> 打开成功!\n")
        self.console.append("经度范围: %f  -  %f" % (gloV.LNG_MIN, gloV.LNG_MAX))
        self.console.append("纬度范围: %f  -  %f" % (gloV.LAT_MIN, gloV.LAT_MAX))

        self.console.append("")
        self.console.append("人均可支配收入列表:")
        for i in gloV.incomeListKeys:
            tmpOut = ("%s : \t%f" % (i, gloV.incomeList[i]))
            self.console.append(tmpOut)
        self.console.append(" \n")

        return 0

    def community_button(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        print(path)
        if len(path[0]) <= 0:
            self.console.append("未选择任何文件.")
            self.isReadCommunity = False
            return -1
        if path[0][-4:] != ".csv":
            self.console.append(str(path[0]) + " 不是CSV文件")
            self.isReadCommunity = False
            return -2

        # ---------- Community 清洗与检验
        fileCommunityName = path[0]
        gloV.communityDataAll = []
        gloV.SAVE_COMMUNITY = []

        returnCommunity = Community.create_Community_SAVE(fileCommunityName)
        if returnCommunity < 0:
            self.console.append(str(fileCommunityName) + " 文件打开错误, 代码是: " + str(returnCommunity))
            self.console.append('-1表示文件不存在, -2表示文件编码不明, -3表示前6列顺序不对')
            self.console.append(' ')
            self.isReadCommunity = False
            return returnCommunity

        self.isReadCommunity = True
        self.console.append("文件 <" + str(fileCommunityName) + "> 打开成功!")
        self.console.append(str(len(gloV.communityDataAll)) + " 行数据已读入.")
        self.console.append("")
        self.console.append("原始字段包含:  " + str(gloV.communityVariableNameStr))
        self.console.append("")
        self.console.append('全国社区 变量已存储在 <Save-CommunityAll.data>')

    def shopHospital_button(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        print(path)
        if len(path[0]) <= 0:
            self.console.append("未选择任何文件.")
            self.isReadShop = False
            return -1
        if path[0][-4:] != ".csv":
            self.console.append(str(path[0]) + " 不是CSV文件")
            self.isReadShop = False
            return -2
        fileShopName = path[0]

        path1 = QtWidgets.QFileDialog.getOpenFileName()
        print(path1)
        if len(path1[0]) <= 0:
            self.console.append("未选择任何文件.")
            self.isReadHospital = False
            return -1
        if path1[0][-4:] != ".csv":
            self.console.append(str(path1[0]) + " 不是CSV文件")
            self.isReadHospital = False
            return -2
        fileHospitalName = path1[0]

        # ---------- Shop + Hospital 清洗与检验
        gloV.SAVE = []
        gloV.shopDataAll = []
        gloV.hospitalDataAll = []

        returnShopHospital = ShopHospital.create_ShopHospital_SAVE(fileShopName, fileHospitalName)
        if -9 <= returnShopHospital < 0:
            self.console.append(str(fileShopName) + " 文件打开错误, 代码是: " + str(returnShopHospital))
            self.console.append('-1表示文件不存在, -2表示文件编码不明, -3表示前2列顺序不对')
            self.console.append(' ')
            self.isReadShop = False
            return returnShopHospital
        if returnShopHospital < -9:
            self.console.append(str(fileHospitalName) + " 文件打开错误, 代码是: " + str(returnShopHospital))
            self.console.append('-10表示文件不存在, -11表示文件编码不明, -12表示前2列顺序不对')
            self.console.append(' ')
            self.isReadHospital = False
            return returnShopHospital

        self.isReadShop = True
        self.console.append("文件 <" + str(fileShopName) + "> 打开成功!")
        self.console.append(str(len(gloV.shopDataAll)) + " 行数据已读入.")
        self.console.append("")
        self.console.append("原始字段包含:  " + str(gloV.shopVariableNameStr))
        self.console.append("")

        self.isReadHospital = True
        self.console.append("文件 <" + str(fileHospitalName) + "> 打开成功!")
        self.console.append(str(len(gloV.hospitalDataAll)) + " 行数据已读入.")
        self.console.append("")
        self.console.append("原始字段包含:  " + str(gloV.hospitalVariableNameStr))
        self.console.append("")

        self.console.append('全国Shop+Hospital 变量已存储在 <Save-ShopHospitalAll.data>')

    def sf(self):
        self.console.append("*********************")
        self.console.append("---------------------")
        self.console.append("$$$$$$$ 开始执行 $$$$$$$")
        self.console.append("---------------------")
        self.console.append("*********************")

        # ---------- 生成网格
        if not self.isReadHelp:
            QtWidgets.QMessageBox.information(self.label, "文件未读取", "请先读取Help.csv")
            tmpButton = self.help_button()
            if tmpButton < 0:
                return tmpButton
        aa = self.read_para()

        Main.generateGrid(gloV.lngKm, gloV.latKm, (gloV.LAT_MIN + gloV.LAT_MAX) / 2)
        if aa < 0:
            return aa

        # ---------- 宠物店 宠物医院 抽取
        readSaveCommunity = Community.run()
        if readSaveCommunity == 'NO_SAVE.':
            tmpButton = self.community_button()
            if tmpButton < 0:
                return tmpButton
        if readSaveCommunity == 'NO_DATA.':
            self.console.append("*********** 没有本城市 社区 数据点 **********")
            return -1

        readSaveShopHospital = ShopHospital.run()
        if readSaveShopHospital == 'NO_SAVE.':
            tmpButton = self.help_button()
            if tmpButton < 0:
                return tmpButton
        if readSaveShopHospital == 'NO_DATA.':
            self.console.append("*********** 没有本城市 ShopHospital 数据点 **********")
            return -1

        # ---------------------------------------------Compute--------------------------------------------------
        # ---------- 数据缺失率统计 与 基本统计量
        gloV.communitySummary = Main.compute_summary('<社区>', gloV.communityVariableNameStr,
                gloV.communityVariableName, len(gloV.communityData), gloV.communityValid, gloV.communityDataType, "w+")
        gloV.shopSummary = Main.compute_summary('<宠物店>', gloV.shopVariableNameStr,
                gloV.shopVariableName, len(gloV.shopData), gloV.shopValid, gloV.shopDataType, "a")
        gloV.hospitalSummary = Main.compute_summary('<宠物医院>', gloV.hospitalVariableNameStr,
                gloV.hospitalVariableName, len(gloV.hospitalData), gloV.hospitalValid, gloV.hospitalDataType, "a")

        self.print_summary('<社区>', gloV.communityVariableName, gloV.communitySummary)
        self.print_summary('<宠物店>', gloV.shopVariableName, gloV.shopSummary)
        self.print_summary('<宠物医院>', gloV.hospitalVariableName, gloV.hospitalSummary)

        # ---------- 基于Grid的计算: 得到gridCommunity, gridDemand, gridCompete, gridValue
        Main.computeGrid()

        # -------------------------------------------Write----------------------------------------------------
        shopHospitalOutput = Main.merge_output(gloV.shopOutput, 'Shop', gloV.hospitalOutput, '医院')
        allOutput = Main.merge_output(gloV.communityOutput, '社区', shopHospitalOutput, 'Shop或医院')

        filePointName = "Output-Point.csv"
        filePoint = open(filePointName, 'w+', encoding='gb2312')
        print('\n开始输出散点图数据:')
        for i in allOutput:
            for j in i:
                try:
                    filePoint.writelines(j)
                except Exception:
                    print('Point输出编码失败:--- ' + str(j))
                filePoint.writelines(',')
            filePoint.writelines('\n')
        filePoint.close()
        self.console.append("----------<Output-Point.csv> 输出完毕!")
        print('\n<Output-Point.csv> 输出完毕!')

        fileGridName = "Output-Grid.csv"
        Main.writeGrid(fileGridName)
        self.console.append("----------<Output-Grid.csv> 输出完毕!")
        self.console.append("---------- 程序完成! ----------")

        # DemoDia.accept()
        self.helpButton.setEnabled(False)
        self.computeButton.setEnabled(False)
        return 0

    def try_float(self, strData):
        try:
            data = int(strData)
        except ValueError:
            try:
                data = float(strData)
            except ValueError:
                QtWidgets.QMessageBox.information(self.label, "参数设置错误", "参数设置不是数字: " + strData)
                raise ValueError
        if data < 0:
            QtWidgets.QMessageBox.information(self.label, "参数 < 0", "参数设置不能是负数: " + strData)
            raise ValueError
        return data

    def print_para(self):
        self.console.append("")
        self.console.append("********** 参数设置 **********")

        self.console.append("方格 沿经度长度: \t" + str(gloV.lngKm))
        self.console.append("方格 沿纬度长度: \t" + str(gloV.latKm))
        self.console.append("竣工时间有效区间: \t%s年 - %s年" % (str(gloV.paraYearMin), str(gloV.paraYearMax)))

        self.console.append("")
        self.console.append("现有户数 上限: \t" + str(gloV.paraFamilyMax))
        self.console.append("医院点评数 切分点: \t" + str(gloV.paraHospitalRemarkCut))

        self.console.append("")
        self.console.append("居民支付能力 = ")
        self.console.append("可支配收入评分 * \t" + str(gloV.paraPayIncome))
        self.console.append("+ 小区售价评分 * \t" + str(gloV.paraPayPrice))
        self.console.append("+ 容积率评分 * \t" + str(gloV.paraPayRongjilv))

        self.console.append("")
        self.console.append("小区综合评分 = ")
        self.console.append("居民支付能力 * \t" + str(gloV.paraCommunityPay))
        self.console.append("+ 居民数量 *   \t" + str(gloV.paraCommunityFamily))

        self.console.append("")
        self.console.append("市场需求得分 = ")
        self.console.append("小区综合评分 * \t" + str(gloV.paraDemandScore))
        self.console.append("+ 宠物店数量 * \t" + str(gloV.paraDemandShop))

        self.console.append("")
        self.console.append("选址综合得分 = ")
        self.console.append("市场需求得分 * \t" + str(gloV.paraFinalDemand))
        self.console.append("- 市场竞争得分 * \t" + str(gloV.paraFinalCompete))
        self.console.append('')
        self.console.append("制作TableAu时间: \t" + str(gloV.generateTime))

        self.console.append("********** **********")
        self.console.append("")

    def print_summary(self, title, name_list, summary_data):
        tmpSummary = ["字段\t总计\t缺失率"]
        for i in name_list:
            tmpSummary.append(i)
        for i in range(0, len(name_list)):
            tmpSummary[i+1] += ("\t" + str(summary_data[0][i]) + "\t" + str(summary_data[3][i]))

        self.console.append("\n")
        self.console.append(title + "  数据缺失统计:")
        for i in tmpSummary:
            self.console.append(i)

    def read_para(self):
        try:
            gloV.lngKm = self.try_float(self.lngKm.text())
            gloV.latKm = self.try_float(self.latKm.text())

            gloV.paraFamilyMax = self.try_float(self.paraFamilyMax.text())
            gloV.paraHospitalRemarkCut = self.try_float(self.paraHospitalRemarkCut.text())

            gloV.paraPayIncome = self.try_float(self.paraPayIncome.text())
            gloV.paraPayPrice = self.try_float(self.paraPayPrice.text())
            gloV.paraPayRongjilv = self.try_float(self.paraPayRongjilv.text())

            gloV.paraCommunityPay = self.try_float(self.paraCommunityPay.text())
            gloV.paraCommunityFamily = self.try_float(self.paraCommunityFamily.text())

            gloV.paraDemandScore = self.try_float(self.paraDemandScore.text())
            gloV.paraDemandShop = self.try_float(self.paraDemandShop.text())

            gloV.paraFinalDemand = self.try_float(self.paraFinalDemand.text())
            gloV.paraFinalCompete = self.try_float(self.paraFinalCompete.text())

            gloV.paraYearMin = self.try_float(self.paraYearMin.text())
            gloV.paraYearMax = self.try_float(self.paraYearMax.text())
            gloV.generateTime = self.lineEdit_3.text()
        except ValueError:
            return -1

        self.print_para()
        return 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DemoDia = QtWidgets.QDialog()
    ui = Ui_DemoDia()
    ui.setupUi(DemoDia)
    DemoDia.show()
    sys.exit(app.exec_())

