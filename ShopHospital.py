# coding: utf-8

import gloV
import Main
import pickle


def readShopAll(fileShopName):
    """
    使用到的变量:
    gloV.communityVariableName
    gloV.communityVariableNamePosition
    gloV.communityDataType

    存储的变量
    gloV.communityVariableNameStr
    gloV.communityDataAll
    """

    # ---得到编码
    fileShopEncoding = Main.try_encoding(fileShopName)
    if fileShopEncoding == "NO_FILE.":
        print('<%s> 文件无法打开. 程序退出*********' % fileShopName)
        return -1
    if fileShopEncoding == "FAILED.":
        print("<%s> 文件编码不明. 程序退出*********" % fileShopName)
        return -2
    fileShop = open(fileShopName, encoding=fileShopEncoding)

    # ---读取列标题
    gloV.shopVariableNameStr = fileShop.readline().strip()
    gloV.shopVariableName = gloV.shopVariableNameStr.split(',')
    if not (gloV.shopVariableName[0] == '经度' and gloV.shopVariableName[1] == '纬度'):
        print('<全国宠物店.csv> 文件前两列不是规定的 [经度, 纬度] 顺序, 程序退出******')
        return -3

    # ---读取全国数据
    readFailed = False
    shopRead = []

    tmpReadLine = 'Begin'
    tmpReadCount = 1
    while tmpReadLine:
        try:
            tmpReadLine = fileShop.readline()
        except Exception:
            tmpReadCount += 1
            print('文件第 %d 行包含未知汉字, 读取失败, 已跳过.' % tmpReadCount)
            readFailed = True
            continue
        tmpReadCount += 1

        i = tmpReadLine
        # 检测 i 中是否有<引号">,如果有则必须成对出现,而且中间部分必须不以<逗号,>切分
        tmpRead = i.strip()
        tmpCountDouHao = tmpRead.count(',')
        tmpCountYinHao = tmpRead.count('"')
        if tmpCountDouHao == (len(gloV.shopVariableName) - 1):
            tmpReadResult = tmpRead.split(",")
            shopRead.append(tmpReadResult)
        elif tmpCountYinHao == 2:
            # 当恰有一对引号出现, 而且没有引号出现在结尾or开头处时, 这段程序可以解析
            tmpReadList = tmpRead.split('"')
            tmpReadHead = tmpReadList[0][:-1].split(",")
            tmpReadTail = tmpReadList[2][1:].split(',')
            tmpReadHead.append("NULL")
            tmpReadHead.extend(tmpReadTail)
            tmpReadResult = tmpReadHead

            tmpCountDouHaoAgain = 0
            for k in tmpReadResult:
                tmpCountDouHaoAgain += k.count(',')
            if tmpCountDouHaoAgain == 0:
                shopRead.append(tmpReadResult)
            else:
                readFailed = True
                print('文件第 %d 行出错: %s' % (tmpReadCount, tmpRead))
        else:
            readFailed = True
            print('文件第 %d 行出错: %s' % (tmpReadCount, tmpRead))
    fileShop.close()
    if readFailed:
        print("****** 以上内容无法解析, 列出的数据跳过 ******\n")

    # ---数据清洗
    for i in shopRead:
        tmpData = []
        for j in range(0, len(i)):
            tmpData0 = i[j]
            if gloV.shopVariableName[j] in gloV.shopDataType:
                tmpData1 = Main.clean_data(tmpData0, gloV.shopDataType[gloV.shopVariableName[j]])
            else:
                tmpData1 = Main.clean_data(tmpData0, 6)
            tmpData.append(tmpData1)
        gloV.shopDataAll.append(tmpData)

    # ---gloV.SAVE[0] 保存变量名称的字符串
    gloV.SAVE = [""]  # [0]

    gloV.SAVE[0] += "shopVariableNameStr,"
    gloV.SAVE.append(gloV.shopVariableNameStr)  # [1]

    gloV.SAVE[0] += "shopDataAll,"
    gloV.SAVE.append(gloV.shopDataAll)  # [2]

    return 0


def readHospitalAll(fileHospitalName):
    """
    使用到的变量:
    gloV.communityVariableName
    gloV.communityVariableNamePosition
    gloV.communityDataType

    存储的变量
    gloV.communityVariableNameStr
    gloV.communityDataAll
    """

    # ---得到编码
    fileHospitalEncoding = Main.try_encoding(fileHospitalName)
    if fileHospitalEncoding == "NO_FILE.":
        print('<%s> 文件无法打开. 程序退出*********' % fileHospitalName)
        return -10

    if fileHospitalEncoding == "FAILED.":
        print("<%s> 文件编码不明. 程序退出*********" % fileHospitalName)
        return -11
    fileHospital = open(fileHospitalName, encoding=fileHospitalEncoding)

    # ---读取列标题
    gloV.hospitalVariableNameStr = fileHospital.readline().strip()
    gloV.hospitalVariableName = gloV.hospitalVariableNameStr.split(',')
    if not (gloV.hospitalVariableName[0] == '经度' and gloV.hospitalVariableName[1] == '纬度' and
            gloV.hospitalVariableName[2] == '点评数'):
        print('<全国宠物医院.csv> 文件前两列不是规定的 [经度, 纬度] 顺序, 程序退出******')
        return -12

    # ---读取全国数据
    readFailed = False
    hospitalRead = []

    tmpReadLine = 'Begin'
    tmpReadCount = 1
    while tmpReadLine:
        try:
            tmpReadLine = fileHospital.readline()
        except Exception:
            tmpReadCount += 1
            print('文件第 %d 行包含未知汉字, 读取失败, 已跳过.' % tmpReadCount)
            readFailed = True
            continue
        tmpReadCount += 1

        i = tmpReadLine
        # 检测 i 中是否有<引号">,如果有则必须成对出现,而且中间部分必须不以<逗号,>切分
        tmpRead = i.strip()
        tmpCountDouHao = tmpRead.count(',')
        tmpCountYinHao = tmpRead.count('"')
        if tmpCountDouHao == (len(gloV.hospitalVariableName) - 1):
            tmpReadResult = tmpRead.split(",")
            hospitalRead.append(tmpReadResult)
        elif tmpCountYinHao == 2:
            # 当恰有一对引号出现, 而且没有引号出现在结尾or开头处时, 这段程序可以解析
            tmpReadList = tmpRead.split('"')
            tmpReadHead = tmpReadList[0][:-1].split(",")
            tmpReadTail = tmpReadList[2][1:].split(',')
            tmpReadHead.append("NULL")
            tmpReadHead.extend(tmpReadTail)
            tmpReadResult = tmpReadHead

            tmpCountDouHaoAgain = 0
            for k in tmpReadResult:
                tmpCountDouHaoAgain += k.count(',')
            if tmpCountDouHaoAgain == 0:
                hospitalRead.append(tmpReadResult)
            else:
                readFailed = True
                print('文件第 %d 行出错: %s' % (tmpReadCount, tmpRead))
        else:
            readFailed = True
            print('文件第 %d 行出错: %s' % (tmpReadCount, tmpRead))
    fileHospital.close()
    if readFailed:
        print("****** 以上内容无法解析, 列出的数据跳过 ******\n")

    # ---数据清洗
    for i in gloV.hospitalVariableName:
        gloV.hospitalValid[i] = []

    for i in hospitalRead:
        tmpData = []
        for j in range(0, len(i)):
            tmpData0 = i[j]
            if gloV.hospitalVariableName[j] in gloV.hospitalDataType:
                tmpData1 = Main.clean_data(tmpData0, gloV.hospitalDataType[gloV.hospitalVariableName[j]])
            else:
                tmpData1 = Main.clean_data(tmpData0, 6)
            tmpData.append(tmpData1)
        gloV.hospitalDataAll.append(tmpData)

    gloV.SAVE[0] += "hospitalVariableNameStr,"
    gloV.SAVE.append(gloV.hospitalVariableNameStr)  # [3]
    gloV.SAVE[0] += "hospitalDataAll,"
    gloV.SAVE.append(gloV.hospitalDataAll)  # [4]

    return 0


def create_ShopHospital_SAVE(fileShopName, fileHospitalName):
    """
    :return:
    -1,-2,-3 表示 <宠物店.csv> 文件无法打开, 文件编码不明, 或文件前两列不是规定的 [经度, 纬度] 顺序
    -10,-11,-12 表示 <宠物医院.csv> 文件无法打开, 文件编码不明, 或文件前两列不是规定的 [经度, 纬度] 顺序
    """

    tmpLngMin = gloV.LNG_MIN
    tmpLngMax = gloV.LNG_MAX
    tmpLatMin = gloV.LAT_MIN
    tmpLatMax = gloV.LAT_MAX

    gloV.LNG_MIN = gloV.CN_LNG_MIN
    gloV.LNG_MAX = gloV.CN_LNG_MAX
    gloV.LAT_MIN = gloV.CN_LAT_MIN
    gloV.LAT_MAX = gloV.CN_LAT_MAX

    returnShop = readShopAll(fileShopName)
    if returnShop < 0:
        return returnShop

    returnHospital = readHospitalAll(fileHospitalName)
    if returnHospital < 0:
        return returnHospital

    pickle.dump(gloV.SAVE, open('Save-ShopHospitalAll.data', 'wb'))
    print('全国宠物店 全国宠物医院 变量已存储在 <Save-ShopHospitalAll.data>')

    gloV.LNG_MIN = tmpLngMin
    gloV.LNG_MAX = tmpLngMax
    gloV.LAT_MIN = tmpLatMin
    gloV.LAT_MAX = tmpLatMax

    return 0


def readDiskData():
    """
    读取 "Save-ShopHospitalAll.data" 文件
    对 gloV 中的下列变量赋值:

    gloV.shopVariableNameStr
    gloV.shopVariableName
    gloV.shopVariableNamePosition
    gloV.shopOutput --- 只添加了第一行内容
    gloV.shopDataAll

    gloV.hospitalVariableNameStr
    gloV.hospitalVariableName
    gloV.hospitalOutput
    gloV.hospitalVariableNamePosition
    gloV.hospitalDataAll
    """
    try:
        f = open("Save-ShopHospitalAll.data", "rb")
    except Exception:
        return 'NO_SAVE.'

    gloV.SAVE = pickle.load(f)
    # print(gloV.SAVE[0])

    # --- Shop
    gloV.shopVariableNameStr = gloV.SAVE[1]
    gloV.shopVariableName = gloV.shopVariableNameStr.split(',')

    gloV.shopOutput = []
    gloV.shopVariableNamePosition = {}
    tmpOutput = []
    for i in gloV.shopVariableName:
        tmpOutput.append(i)
    gloV.shopOutput.append(tmpOutput)

    for i in range(0, len(gloV.shopVariableName)):
        gloV.shopVariableNamePosition[gloV.shopVariableName[i]] = i

    gloV.shopDataAll = gloV.SAVE[2]

    # --- Hospital
    gloV.hospitalVariableNameStr = gloV.SAVE[3]
    gloV.hospitalVariableName = gloV.hospitalVariableNameStr.split(',')

    gloV.hospitalOutput = []
    gloV.hospitalVariableNamePosition = {}
    tmpOutput = []
    for i in gloV.hospitalVariableName:
        tmpOutput.append(i)
    gloV.hospitalOutput.append(tmpOutput)

    for i in range(0, len(gloV.hospitalVariableName)):
        gloV.hospitalVariableNamePosition[gloV.hospitalVariableName[i]] = i

    gloV.hospitalDataAll = gloV.SAVE[4]
    print('<Save-ShopHospitalAll.data> 文件已读入, 得到全国宠物店数据 和 全国宠物医院数据')


def run():
    """
    gloV.shopData
    gloV.shopGridId
    gloV.shopValid
    gloV.shopOutput
    """

    # -------------------- Get shopDataAll and hospitalDataAll --------------------
    # gloV.shopVariableNameStr
    # gloV.shopVariableName
    # gloV.shopOutput
    # gloV.shopDataAll

    # gloV.LNG_MIN  gloV.LNG_MAX
    # gloV.LAT_MIN  gloV.LAT_MAX

    noSave = readDiskData()
    if noSave == 'NO_SAVE.':
        return noSave

    # -------------------- Compute Shop --------------------
    gloV.shopData = []
    gloV.shopGridId = []
    gloV.shopValid = {}
    for i in gloV.shopVariableName:
        gloV.shopValid[i] = []
    gloV.shopOutput[0].append('Type')
    gloV.shopOutput[0].append('GridId')
    gloV.shopOutput[0].append('Score')
    gloV.shopOutput[0].append('GenerateTime')

    for i in gloV.shopDataAll:
        if Main.is_valid(i[0]) and Main.is_valid(i[1]):
            if gloV.LNG_MIN <= i[0] <= gloV.LNG_MAX and gloV.LAT_MIN <= i[1] <= gloV.LAT_MAX:
                tmpDataStr = []

                # --- gloV.shopValid + gloV.shopData
                tmpData = []
                for j in range(0, len(i)):
                    tmpData.append(i[j])
                    tmpDataStr.append(str(i[j]))
                    if Main.is_valid(i[j]):
                        gloV.shopValid[gloV.shopVariableName[j]].append(i[j])
                gloV.shopData.append(tmpData)

                # --- gloV.shopGridId
                lngId = int((i[0] - gloV.LNG_MIN) / gloV.lngLeap)
                latId = int((i[1] - gloV.LAT_MIN) / gloV.latLeap)
                gloV.shopGridId.append(gloV.gridId[latId][lngId])

                tmpDataStr.append('宠物店')
                tmpDataStr.append(str(gloV.gridId[latId][lngId]))
                tmpDataStr.append('1.5')
                tmpDataStr.append(gloV.generateTime)
                gloV.shopOutput.append(tmpDataStr)

    # -------------------- Compute Hospital --------------------
    gloV.hospitalData = []
    gloV.hospitalGridId = []
    gloV.hospitalValid = {}
    for i in gloV.hospitalVariableName:
        gloV.hospitalValid[i] = []
    gloV.hospitalOutput[0].append('Type')
    gloV.hospitalOutput[0].append('GridId')
    gloV.hospitalOutput[0].append('Score')
    gloV.hospitalOutput[0].append('GenerateTime')

    for i in gloV.hospitalDataAll:
        if Main.is_valid(i[0]) and Main.is_valid(i[1]):
            if gloV.LNG_MIN <= i[0] <= gloV.LNG_MAX and gloV.LAT_MIN <= i[1] <= gloV.LAT_MAX:
                tmpDataStr = []

                # --- gloV.hospitalValid + gloV.hospitalData
                tmpData = []
                for j in range(0, len(i)):
                    tmpData.append(i[j])
                    tmpDataStr.append(str(i[j]))
                    if Main.is_valid(i[j]):
                        gloV.hospitalValid[gloV.hospitalVariableName[j]].append(i[j])
                gloV.hospitalData.append(tmpData)

                # --- gloV.hospitalGridId
                lngId = int((i[0] - gloV.LNG_MIN) / gloV.lngLeap)
                latId = int((i[1] - gloV.LAT_MIN) / gloV.latLeap)
                gloV.hospitalGridId.append(gloV.gridId[latId][lngId])

                tmpDataStr.append('宠物医院')
                tmpDataStr.append(str(gloV.gridId[latId][lngId]))

                # --- gloV.hospitalScore
                if Main.is_valid(i[2]):
                    if i[2] > 10:
                        gloV.hospitalScore.append(2)
                        tmpDataStr.append('2')
                    else:
                        gloV.hospitalScore.append(1)
                        tmpDataStr.append('1')
                else:
                    gloV.hospitalScore.append(0)
                    tmpDataStr.append('0')
                tmpDataStr.append(gloV.generateTime)
                gloV.hospitalOutput.append(tmpDataStr)
    if len(gloV.shopData) == 0 or len(gloV.hospitalData) == 0:
        return 'NO_DATA.'


if __name__ == '__main__':
    create_ShopHospital_SAVE("Shop-UTF8.csv", "Hospital-UTF8.csv")
