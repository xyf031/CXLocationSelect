# coding: utf-8

import gloV
import Main
import pickle
import datetime

LNG_MIN = gloV.CN_LNG_MIN
LNG_MAX = gloV.CN_LNG_MAX
LAT_MIN = gloV.CN_LAT_MIN
LAT_MAX = gloV.CN_LAT_MAX


def readCommunityAll(fileCommunityName):
    """
    临时使用的变量:
    gloV.communityVariableName
    gloV.communityVariableNamePosition
    gloV.communityDataType

    存储的变量
    gloV.communityVariableNameStr
    gloV.communityDataAll
    """

    # ---得到编码
    fileCommunityEncoding = Main.try_encoding(fileCommunityName)
    if fileCommunityEncoding == "NO_FILE.":
        print('<%s> 文件无法打开. 程序退出*********' % fileCommunityName)
        return -1
    if fileCommunityEncoding == "FAILED.":
        print("<%s> 文件编码不明. 程序退出*********" % fileCommunityName)
        return -2
    fileCommunity = open(fileCommunityName, encoding=fileCommunityEncoding)

    # ---读取列标题
    gloV.communityVariableNameStr = fileCommunity.readline().strip()
    gloV.communityVariableName = gloV.communityVariableNameStr.split(',')
    if not (gloV.communityVariableName[0] == "经度" and gloV.communityVariableName[1] == "纬度" and
            gloV.communityVariableName[2] == "区县" and gloV.communityVariableName[3] == "容积率" and
            gloV.communityVariableName[4] == "均价" and gloV.communityVariableName[5] == "现有户数"):
        print("<Community.csv> 前6列不是规定的 [经度,纬度,区县,容积率,均价,现有户数] 顺序,程序退出******")
        return -3

    for i in range(0, len(gloV.communityVariableName)):
        gloV.communityVariableNamePosition[gloV.communityVariableName[i]] = i

    # ---数据读取
    readFailed = False
    communityRead = []
    tmpReadLine = 'Begin'
    tmpReadCount = 1
    while tmpReadLine:
        try:
            tmpReadLine = fileCommunity.readline()
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
        if tmpCountDouHao == (len(gloV.communityVariableName) - 1):
            tmpReadResult = tmpRead.split(",")
            communityRead.append(tmpReadResult)
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
                communityRead.append(tmpReadResult)
            else:
                readFailed = True
                print('文件第 %d 行不符合CSV文件格式: %s' % (tmpReadCount, tmpRead))
        else:
            readFailed = True
            print('文件第 %d 行不符合CSV文件格式: %s' % (tmpReadCount, tmpRead))
    fileCommunity.close()
    if readFailed:
        print("****** 以上内容无法解析, 列出的数据跳过 ******\n")
    print('全国社区数据已读入 <%d> 行数据.\n' % len(communityRead))

    # ---数据清洗
    for i in communityRead:
        tmpData1 = []
        for j in range(0, len(i)):
            tmpData0 = i[j]
            if gloV.communityVariableName[j] in gloV.communityDataType:
                tmpData = Main.clean_data(tmpData0, gloV.communityDataType[gloV.communityVariableName[j]])
            else:
                tmpData = Main.clean_data(tmpData0, 6)
            tmpData1.append(tmpData)
        gloV.communityDataAll.append(tmpData1)

    # ---Save
    gloV.SAVE_COMMUNITY = [""]  # [0]

    gloV.SAVE_COMMUNITY[0] += "communityVariableNameStr,"
    gloV.SAVE_COMMUNITY.append(gloV.communityVariableNameStr)  # [1]

    gloV.SAVE_COMMUNITY[0] += "communityDataAll,"
    gloV.SAVE_COMMUNITY.append(gloV.communityDataAll)  # [2]

    return 0


def create_Community_SAVE(fileCommunityName):
    """
    -1 表示 <Community.csv> 文件编码不明
    -2 表示 文件前6列不是规定的 [经度,纬度,区县,容积率,均价,现有户数] 顺序
    """

    tmpLngMin = gloV.LNG_MIN
    tmpLngMax = gloV.LNG_MAX
    tmpLatMin = gloV.LAT_MIN
    tmpLatMax = gloV.LAT_MAX

    gloV.LNG_MIN = LNG_MIN
    gloV.LNG_MAX = LNG_MAX
    gloV.LAT_MIN = LAT_MIN
    gloV.LAT_MAX = LAT_MAX

    returnCommunity = readCommunityAll(fileCommunityName)
    if returnCommunity < 0:
        return returnCommunity

    pickle.dump(gloV.SAVE_COMMUNITY, open('Save-CommunityAll.data', 'wb'))
    print('全国社区 变量已存储在 <Save-CommunityAll.data>')

    gloV.LNG_MIN = tmpLngMin
    gloV.LNG_MAX = tmpLngMax
    gloV.LAT_MIN = tmpLatMin
    gloV.LAT_MAX = tmpLatMax

    return 0


def readDiskData():
    """
    初始化赋值:
    gloV.communityVariableNameStr
    gloV.communityVariableName
    gloV.communityVariableNamePosition

    gloV.communityOutput --- 只添加了第一行内容
    gloV.communityDataAll
    """
    try:
        f = open("Save-CommunityAll.data", "rb")
    except Exception:
        return 'NO_SAVE.'

    gloV.SAVE_COMMUNITY = pickle.load(f)
    # print(gloV.SAVE_COMMUNIYT[0])
    gloV.communityVariableNamePosition = {}
    gloV.communityOutput = []

    gloV.communityVariableNameStr = gloV.SAVE_COMMUNITY[1]
    gloV.communityDataAll = gloV.SAVE_COMMUNITY[2]

    gloV.communityVariableName = gloV.communityVariableNameStr.split(',')
    for i in range(0, len(gloV.communityVariableName)):
        gloV.communityVariableNamePosition[gloV.communityVariableName[i]] = i

    tmpOutput = []
    for i in gloV.communityVariableName:
        tmpOutput.append(i)
    gloV.communityOutput.append(tmpOutput)

    print('<Save-CommunityAll.data> 文件已读入, 得到全国社区数据')

    return 0


def computeCommunity():
    """
    需要:
    gloV.communitySummary

    初始化赋值了:
    gloV.communityScore

    修改了:
    gloV.communityOutput
    """

    communityIncome = []
    communityRongjilv = []
    communityPrice = []
    communityFamily = []
    communityScoreTmp = []

    paraPaySum = gloV.paraPayIncome + gloV.paraPayPrice + gloV.paraPayRongjilv

    for i in range(0, len(gloV.communityData)):
        tmpData = gloV.communityData[i]

        # ---对4列参与计算的数据Zoom
        # 人均可支配收入
        if Main.is_valid(tmpData[2]) and Main.get_income(tmpData[2]) > 0:
            communityIncome.append(Main.zoom_data(Main.get_income(tmpData[2]), gloV.communitySummary[5][2], gloV.communitySummary[4][2]))
        else:
            communityIncome.append(0)

        # 容积率
        if Main.is_valid(tmpData[3]):
            communityRongjilv.append(Main.zoom_rongjilv(tmpData[3]))
        else:
            communityRongjilv.append(0)

        # 均价
        if Main.is_valid(tmpData[4]):
            communityPrice.append(Main.zoom_data(tmpData[4], gloV.communitySummary[5][4], gloV.communitySummary[4][4]))
        else:
            communityPrice.append(0)

        # 现有户数
        if Main.is_valid(tmpData[5]):
            communityFamily.append(Main.zoom_family(tmpData[5], gloV.communitySummary[5][5], gloV.communitySummary[4][5]))
        else:
            communityFamily.append(0)

        communityScoreTmp.append(gloV.paraCommunityPay *
                                 (gloV.paraPayIncome * communityIncome[i] +
                                  gloV.paraPayPrice * communityPrice[i] +
                                  gloV.paraPayRongjilv * communityRongjilv[i]) / paraPaySum +
                                 gloV.paraCommunityFamily * communityFamily[i])

    # ---计算社区评分
    gloV.communityScore = []
    gloV.communityOutput[0].append("Score")
    communityScoreMin = min(communityScoreTmp)
    communityScoreMax = max(communityScoreTmp)
    for i in range(0, len(communityScoreTmp)):
        gloV.communityScore.append(Main.zoom_data(communityScoreTmp[i], communityScoreMin, communityScoreMax))
        gloV.communityOutput[i + 1].append(str(Main.zoom_data(communityScoreTmp[i], communityScoreMin, communityScoreMax)))


def run():
    """
    需要:
    gloV.LNG_MIN  gloV.LNG_MAX
    gloV.LAT_MIN  gloV.LAT_MAX
    gloV.gridId
    gloV.incomeList

    初始化赋值了:
    gloV.communityData
    gloV.communityValid

    gloV.communityIsVilla
    gloV.communityIsBefore2000

    gloV.communityGridId
    gloV.communitySummary

    修改了:
    gloV.communityOutput
    """

    # -------------------- Get communityDataAll --------------------
    # 运行 readDiskData() 之后拥有的变量:
    # gloV.communityVariableNameStr
    # gloV.communityVariableName
    # gloV.communityVariableNamePosition
    # gloV.communityOutput
    # gloV.communityDataAll
    noSave = readDiskData()
    if noSave == 'NO_SAVE.':
        return noSave

    gloV.communityData = []
    gloV.communityGridId = []
    gloV.communityValid = {}
    gloV.communityIsVilla = []
    gloV.communityIsBefore2000 = []
    for i in gloV.communityVariableName:
        gloV.communityValid[i] = []
    gloV.communityOutput[0].append('是否别墅')
    gloV.communityOutput[0].append('是否早于2000年竣工')
    gloV.communityOutput[0].append('Type')
    gloV.communityOutput[0].append('GridId')
    gloV.communityOutput[0].append('GenerateTime')

    for i in gloV.communityDataAll:
        if Main.is_valid(i[0]) and Main.is_valid(i[1]):
            if Main.is_right_city(i[0], i[1], gloV.communityVariableName, i, gloV.communityVariableNamePosition):
                tmpDataStr = []

                # 处理 gloV.communityData
                tmpData = []
                for j in range(0, len(i)):
                    tmpData.append(i[j])
                    tmpDataStr.append(str(i[j]))
                    if j == 2:
                        if Main.is_valid(i[j]) and Main.get_income(i[j]) != 0:
                            gloV.communityValid["区县"].append(Main.get_income(i[j]))
                    elif Main.is_valid(i[j]):
                        gloV.communityValid[gloV.communityVariableName[j]].append(i[j])
                gloV.communityData.append(tmpData)

                # 处理 gloV.communityGridId
                lngId = int((i[0] - gloV.LNG_MIN) / gloV.lngLeap)
                latId = int((i[1] - gloV.LAT_MIN) / gloV.latLeap)
                gloV.communityGridId.append(gloV.gridId[latId][lngId])

                # 处理 gloV.communityIsVilla
                villaVariableList = ['小区类型', '小区特点', '建筑类别', '建筑结构']
                villa = False
                for k in villaVariableList:
                    if k in gloV.communityVariableName and '别墅' in i[gloV.communityVariableNamePosition[k]]:
                        villa = True
                        break
                if villa:
                    gloV.communityIsVilla.append(1)
                    tmpDataStr.append('是')
                else:
                    gloV.communityIsVilla.append(0)
                    tmpDataStr.append('否')

                # 处理 gloV.communityIsBefore2000
                if '竣工时间' in gloV.communityVariableName:
                    tmpDate = i[gloV.communityVariableNamePosition['竣工时间']]
                    if Main.is_valid(tmpDate) and tmpDate.year < 2000:
                        gloV.communityIsBefore2000.append(1)
                        tmpDataStr.append('是')
                    else:
                        gloV.communityIsBefore2000.append(0)
                        tmpDataStr.append('否')
                else:
                    gloV.communityIsBefore2000.append(0)
                    tmpDataStr.append('否')

                # 处理 gloV.communityOutput
                tmpDataStr.append('社区')
                tmpDataStr.append(str(gloV.gridId[latId][lngId]))
                tmpDataStr.append(gloV.generateTime)
                gloV.communityOutput.append(tmpDataStr)

    if len(gloV.communityData) == 0:
        return 'NO_DATA.'

    # ---------- 社区数据归一化, 计算"综合评分"
    gloV.communitySummary = Main.compute_summary('<社区>', gloV.communityVariableNameStr, gloV.communityVariableName,
                            len(gloV.communityData), gloV.communityValid, gloV.communityDataType, "no-write")
    computeCommunity()

    return 0


if __name__ == "__main__":
    create_Community_SAVE("Community-UTF8.csv")
