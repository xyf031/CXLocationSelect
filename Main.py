# coding:UTF-8

import numpy
import datetime
import gloV
import Community
import ShopHospital


def try_encoding(file_name):
    """
    使用["gb2312", "gbk", "gb18030", "hz", "utf_8", "utf_16"]依次尝试读取CSV文件,返回编码对应的字符串.
    :param file_name: CSV的完整文件名,相对或绝度路径均可.
    :return: 字符串,空字符串表示没有找到匹配的编码方式.
    """
    print('\n### CSV编码尝试 ###')
    print('try_encoding(): CSV文件第一个单元格若不是 "城市" or "经度", 则需手动修改源代码Main.py的 try_encoding(file_name) 函数')

    encoding_lists = ["gb2312", "utf_8", "utf_16", "gbk", "gb18030", "hz"]
    print("目前依次尝试以下编码格式打开文件:")
    print(str(encoding_lists))
    try:
        open(file_name)
    except OSError:
        print('无法打开文件: <%s>' % file_name)
        return 'NO_FILE.'

    for i in encoding_lists:
        file_try = open(file_name, encoding=i)
        try:
            file_try_tmp = file_try.readline().strip().split(',')
        except Exception:
            print("<%s>使用编码<%s>失败,正在尝试其他编码..." % (file_name, i))
            continue
        if file_try_tmp[0] in ["城市", "经度"]:
            print("<%s>成功解码!编码是<%s>" % (file_name, i))
            print('### CSV编码尝试结束 ###\n')
            return i
        print("<%s>使用编码<%s>失败,正在尝试其他编码..." % (file_name, i))
        file_try.close()

    print("<%s>文件解析失败" % file_name)
    print('### CSV编码尝试结束 ###\n')
    return "FAILED."


def clean_data(strData, cleanType):
    """
    1 经度:float, 大小限制为 [LNG_MIN, LNG_MAX]
    2 纬度:float, 大小限制为 [LAT_MIN, LAT_MAX]
    3 正数字:float, 严格大于零
    4 数字:float, 其余无限制
    5 行政区划:字符串, 必须能在gloV.incomeList{}中有匹配字段
    6 字符串:非空
    7 整数:Int 非负
    8 日期:int 或 字符串, 支持4种格式 '36526' '2000/1/1' '2000-1-1' '2000 1 1'

    :param strData: 单个数据的字符串形式,不可以是list
    :param cleanType:
    :return: float or 字符串 or "NULL"
    """
    cleanResult = "NULL"
    if cleanType == 1:
        # 经度
        try:
            cleanResult = float(strData)
        except Exception:
            cleanResult = "NULL"
            return cleanResult
        if not (gloV.CN_LNG_MIN <= cleanResult <= gloV.CN_LNG_MAX):
            cleanResult = "NULL"
            return cleanResult
    elif cleanType == 2:
        # 纬度
        try:
            cleanResult = float(strData)
        except Exception:
            cleanResult = "NULL"
            return cleanResult
        if not (gloV.CN_LAT_MIN <= cleanResult <= gloV.CN_LAT_MAX):
            cleanResult = "NULL"
            return cleanResult
    elif cleanType == 3:
        # 数字float,严格大于零
        try:
            cleanResult = float(strData)
        except Exception:
            cleanResult = "NULL"
            return cleanResult
        if cleanResult <= 0:
            cleanResult = "NULL"
            return cleanResult
    elif cleanType == 4:
        # 数字float,没有大小限制
        try:
            cleanResult = float(strData)
        except Exception:
            cleanResult = "NULL"
            return cleanResult
    elif cleanType == 5:
        # 行政区划
        if len(strData) == 0:
            cleanResult = "NULL"
            return cleanResult
        # if get_income(strData) == 0:
        #     cleanResult = "查无此区:" + str(strData)
        #     return cleanResult
        cleanResult = strData
    elif cleanType == 6:
        # 字符串
        if len(strData) == 0:
            cleanResult = "NULL"
        else:
            cleanResult = strData
    elif cleanType == 7:
        # Int >= 0
        try:
            cleanResult = int(strData)
        except Exception:
            cleanResult = 'NULL'
            return cleanResult
    elif cleanType == 8:
        # Date
        if len(strData) == 0:
            cleanResult = 'NULL'
        else:
            strData = strData.strip()
            tmpDate = 0
            try:
                tmpDate = int(strData)
            except ValueError:
                tmpList = ['/', '-', ' ']
                for i in tmpList:
                    try:
                        tmpDate = datetime.datetime.strptime(strData, '%Y' + i + '%m' + i + '%d')
                        cleanResult = datetime.date.fromordinal(tmpDate.toordinal())
                        return cleanResult
                    except Exception:
                        continue
            try:
                cleanResult = datetime.date.fromordinal(gloV.EXCEL_DATE + tmpDate)
                if gloV.paraYearMin <= cleanResult.year <= gloV.paraYearMax:
                    return cleanResult
                else:
                    return 'NULL'
            except ValueError:
                return 'NULL'

    return cleanResult


def is_valid(dataTest):
    if isinstance(dataTest, float("3.14").__class__):
        return True
    elif isinstance(dataTest, int("3").__class__):
        return True
    elif isinstance(dataTest, datetime.date):
        return True
    elif isinstance(dataTest, "NULL".__class__) and (dataTest.upper() not in ['NULL', '\\N']):
        return True
    else:
        return False


def is_right_city(lng, lat, variable_name, i, name_position):
    if '城市' not in variable_name:
        return gloV.LNG_MIN <= lng <= gloV.LNG_MAX and gloV.LAT_MIN <= lat <= gloV.LAT_MAX
    else:
        if gloV.LNG_MIN <= lng <= gloV.LNG_MAX and gloV.LAT_MIN <= lat <= gloV.LAT_MAX:
            if i[name_position['城市']].lower() in gloV.currentCity:
                return True
            else:
                return False
        else:
            return False


def get_max(data):
    max_return = data[0][0]
    for i in data:
        tmp_max = max(i)
        max_return = max(max_return, tmp_max)

    return max_return


def get_min(data):
    min_return = data[0][0]
    for i in data:
        tmp_min = min(i)
        min_return = min(min_return, tmp_min)

    return min_return


def get_income(region_name):
    if is_valid(region_name):
        for i in gloV.incomeListKeys:
            if (region_name in i) or (i in region_name):
                return gloV.incomeList[i]
    return 0


def make_zeros(rows, cols):
    tmpZerosMatrix = []
    for i in range(0, rows):
        tmpZeros = []
        for j in range(0, cols):
            tmpZeros.append(0)
        tmpZerosMatrix.append(tmpZeros)
    return tmpZerosMatrix


def make_empty(rows, cols):
    tmpZerosMatrix = []
    for i in range(0, rows):
        tmpZeros = []
        for j in range(0, cols):
            tmpZeros.append([])
        tmpZerosMatrix.append(tmpZeros)
    return tmpZerosMatrix


def zoom_data(data, min_data, max_data):
    if min_data == max_data:
        return 3
    else:
        return 1 + 4 * (data - min_data) / (max_data - min_data)


def zoom_rongjilv(data):
    if data > 4:
        return 1
    elif data > 3:
        return 2
    elif data > 2:
        return 3
    elif data > 1:
        return 4
    return 5


def zoom_family(data, min_data, max_data):
    if min_data >= gloV.paraFamilyMax:
        return zoom_data(data, min_data, max_data)
    else:
        if data >= gloV.paraFamilyMax:
            return 5
        else:
            return 1 + 4 * (data - min_data) / (gloV.paraFamilyMax - min_data)


def compute_summary(title, name_line, name_list, data_length, valid, data_type, file_way):
    summary_type = ["总计", "有效数据", "Na数据", "缺失率", "最大值", "最小值"]
    summary_data = []
    summary_output = [title + "," + name_line + ',']

    for i in summary_type:
        tmpZero1 = []
        for j in name_list:
            tmpZero1.append(0)
        summary_data.append(tmpZero1)
        summary_output.append(i + ',')

    count_all = data_length
    for i in range(0, len(name_list)):
        summary_data[0][i] = count_all  # 总计
        summary_data[1][i] = len(valid[name_list[i]])               # 有效量
        summary_data[2][i] = count_all - len(valid[name_list[i]])   # 缺失量
        summary_data[3][i] = d1(summary_data[2][i], count_all)         # 缺失率
        if summary_data[1][i] == 0:
            summary_data[4][i] = 'NULL'
            summary_data[5][i] = 'NULL'
        else:
            summary_data[4][i] = max(valid[name_list[i]])  # 最大
            summary_data[5][i] = min(valid[name_list[i]])  # 最小

        summary_output[1] += (str(summary_data[0][i]) + ',')  # 总计
        summary_output[2] += (str(summary_data[1][i]) + ',')  # 有效量
        summary_output[3] += (str(summary_data[2][i]) + ',')  # 缺失量
        summary_output[4] += (str(summary_data[3][i]) + ',')  # 缺失率
        if name_list[i] not in data_type or data_type[name_list[i]] == 6:
            # summary_output[5] += '略,'  # 最小
            # summary_output[6] += '略,'  # 最大
            summary_output[5] += (str(summary_data[4][i]) + ',')  # 最小
            summary_output[6] += (str(summary_data[5][i]) + ',')  # 最大
        else:
            summary_output[5] += (str(summary_data[4][i]) + ',')  # 最小
            summary_output[6] += (str(summary_data[5][i]) + ',')  # 最大

    if file_way not in ['w+', 'a', 'w', 'a+']:
        print('Summary 计算完毕, 但不输出文件.')
        return summary_data

    file = open('Output-Summary.csv', file_way, encoding='gb2312')
    for i in summary_output:
        try:
            file.writelines(i[:-1] + '\n')
        except Exception:
            file.writelines('\n')
            print("Output-Summary 输出编码失败---" + i[:-1])
    file.writelines('\n')
    file.close()
    print(title + ' 变量缺失率 和 基本统计情况输出完成! 详见 Output-Summary.csv')

    return summary_data


def merge_output(output1, label1, output2, label2):

    name1 = output1[0]
    col1 = len(name1)

    name2 = output2[0]

    output3 = [output1[0]]
    col3 = col1

    position = []
    tmpPosi = 0
    for i in name2:
        if i in name1:
            position.append(name1.index(i))
        else:
            col3 += 1
            output3[0].append(i)
            position.append(col1 + tmpPosi)
            tmpPosi += 1

    for i in output1[1:]:
        tmpOutput = []
        for j in i:
            tmpOutput.append(j)
        for j in range(0, col3 - col1):
            tmpOutput.append('<%s>专有字段' % label2)
        output3.append(tmpOutput)

    for i in output2[1:]:
        tmpOutput = []
        for j in range(0, col3):
            tmpOutput.append('')
        for j in range(0, len(i)):
            tmpOutput[position[j]] = i[j]
        for j in range(0, col3):
            if j not in position:
                tmpOutput[j] = ('<%s>专有字段' % label1)
        output3.append(tmpOutput)

    return output3


def d1(a, b):
    if b != 0:
        return a / b
    else:
        return 0


def readHelpCSV(fileHelpName):
    """
    -1: 文件编码不明(以第一个单元格是否可以读取成 "城市" 为准)
    -2: 区县人均可支配收入 不是数字
    """
    fileHelpEncoding = try_encoding(fileHelpName)
    if fileHelpEncoding == 'NO_FILE.':
        print("<%s> 文件不存在. 程序退出**********" % fileHelpName)
        return -1
    if fileHelpEncoding == "FAILED.":
        print("<%s> 文件编码不明. 程序退出**********" % fileHelpName)
        return -2
    fileHelp = open(fileHelpName, encoding=fileHelpEncoding)
    fileHelpTmp = fileHelp.readline().strip().split(',')
    gloV.currentCity = fileHelpTmp[1]
    print("\n\n当前城市:%s" % gloV.currentCity)

    fileHelpTmp = fileHelp.readline().strip().split(',')
    gloV.LNG_MIN = max(float(fileHelpTmp[1]), gloV.LNG_MIN)
    fileHelpTmp = fileHelp.readline().strip().split(',')
    gloV.LNG_MAX = min(float(fileHelpTmp[1]), gloV.LNG_MAX)
    fileHelpTmp = fileHelp.readline().strip().split(',')
    gloV.LAT_MIN = max(float(fileHelpTmp[1]), gloV.LAT_MIN)
    fileHelpTmp = fileHelp.readline().strip().split(',')
    gloV.LAT_MAX = min(float(fileHelpTmp[1]), gloV.LAT_MAX)

    fileHelpTmp = fileHelp.readline().strip()
    if fileHelpTmp != "区县,人均可支配收入":
        print('<%s>不符合模板,第6行不是"区县,人均可支配收入"**********' % fileHelpName)
        # return -1

    for i in fileHelp.readlines():
        fileHelpTmp = i.strip().split(',')
        try:
            tmpFloat = float(fileHelpTmp[1])
        except Exception:
            print("readHelpCSV(): 以下内容含有非法字符, 无法读取其中数字, 程序退出:**********")
            print(fileHelpTmp)
            return -3
        gloV.incomeList[fileHelpTmp[0]] = tmpFloat
    fileHelp.close()

    gloV.incomeListKeys = list(gloV.incomeList.keys())

    print("城市辅助信息Help.csv 读取完毕!")
    print("经度范围: %f - %f" % (gloV.LNG_MIN, gloV.LNG_MAX))
    print("维度范围: %f - %f" % (gloV.LAT_MIN, gloV.LAT_MAX))
    print("本市行政区县个数: %d" % gloV.incomeList.__len__())

    print(gloV.incomeListKeys)
    print()

    return 0


def generateGrid(lngKm, latKm, latCenter):
    """
    gloV.lngLeap
    gloV.latLeap

    gloV.lngGrid
    gloV.latGrid

    gloV.gridId

    :param lngKm: 方格宽度(东西方向)
    :param latKm: 方格长度(南北方向)
    :param latCenter: 不同纬度上对经度切分结果不同, 需要指定目标纬度地区
    """
    gloV.lngLeap = lngKm * 360 / (numpy.cos(latCenter / 180 * numpy.pi) * 40000)
    print("\n方格跨越经度: " + str(gloV.lngLeap))
    gloV.latLeap = latKm * 360 / 40000
    print("方格跨越纬度: " + str(gloV.latLeap))

    tmpLng = gloV.LNG_MIN
    gloV.lngGrid = []
    while tmpLng < gloV.LNG_MAX:
        gloV.lngGrid.append(tmpLng)
        tmpLng += gloV.lngLeap
    gloV.lngGrid.append(tmpLng)

    tmpLat = gloV.LAT_MIN
    gloV.latGrid = []
    while tmpLat < gloV.LAT_MAX:
        gloV.latGrid.append(tmpLat)
        tmpLat += gloV.latLeap
    gloV.latGrid.append(tmpLat)

    print("经度被切成的份数: " + str(len(gloV.lngGrid)))
    print("纬度被切成的份数: " + str(len(gloV.latGrid)))

    gloV.gridId = []
    gloV.gridId = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)

    tmpId = 1
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            gloV.gridId[i][j] = tmpId
            tmpId += 1
    print("方格总量: " + str(tmpId - 1))
    print()


def computeGrid():
    gloV.gridCommunityCount = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridCommunityScoreS = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridCommunityVillaCount = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridCommunityBefore2000Count = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    # gloV.gridCommunityFamilyS = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gridCommunityValidName = ['容积率', '均价', '现有户数', '总户数']
    gloV.gridCommunityValid = {}
    for i in gridCommunityValidName:
        if i not in gloV.communityVariableName or gloV.communityDataType[i] not in [1, 2, 3, 4, 7]:
            # 确保被统计的变量在原始数据中存在, 而且是数字, 可以被min() sum()等函数接受.
            gridCommunityValidName.remove(i)
            continue
        gloV.gridCommunityValid[i] = make_empty(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)

    gloV.gridShopCount = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gridShopValidName = []
    gloV.gridShopValid = {}
    for i in gridShopValidName:
        if i not in gloV.shopVariableName:
            gridShopValidName.remove(i)
            continue
        gloV.gridShopValid[i] = make_empty(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)

    gloV.gridHospitalCount = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    # gloV.gridHospitalRemarkS = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gridHospitalValidName = ['点评数']
    gloV.gridHospitalValid = {}
    for i in gridHospitalValidName:
        if i not in gloV.hospitalVariableName:
            gridHospitalValidName.remove(i)
            continue
        gloV.gridHospitalValid[i] = make_empty(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)

    gridDemandTmp = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gridHospitalRemarkS = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridDemand = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridCompete = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    gloV.gridValue = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)

    for i in range(0, len(gloV.communityData)):
        tmpData = gloV.communityData[i]
        if is_valid(tmpData[0]) and is_valid(tmpData[1]):
            lngId = int((tmpData[0] - gloV.LNG_MIN) / gloV.lngLeap)
            latId = int((tmpData[1] - gloV.LAT_MIN) / gloV.latLeap)
            gloV.gridCommunityCount[latId][lngId] += 1
            gloV.gridCommunityScoreS[latId][lngId] += gloV.communityScore[i]
            gloV.gridCommunityVillaCount[latId][lngId] += gloV.communityIsVilla[i]
            gloV.gridCommunityBefore2000Count[latId][lngId] += gloV.communityIsBefore2000[i]
            # if is_valid(tmpData[5]):
            #     gloV.gridCommunityFamilyS[latId][lngId] += tmpData[5]
            for j in gridCommunityValidName:
                if is_valid(tmpData[gloV.communityVariableNamePosition[j]]):
                    gloV.gridCommunityValid[j][latId][lngId].append(tmpData[gloV.communityVariableNamePosition[j]])

    for i in range(0, len(gloV.shopData)):
        tmpData = gloV.shopData[i]
        if is_valid(tmpData[0]) and is_valid(tmpData[1]):
            lngId = int((tmpData[0] - gloV.LNG_MIN) / gloV.lngLeap)
            latId = int((tmpData[1] - gloV.LAT_MIN) / gloV.latLeap)
            gloV.gridShopCount[latId][lngId] += 1
            for j in gridShopValidName:
                if is_valid(tmpData[gloV.shopVariableNamePosition[j]]):
                    gloV.shopValid[j][latId][lngId].append(tmpData[gloV.shopVariableNamePosition[j]])

    for i in range(0, len(gloV.hospitalData)):
        tmpData = gloV.hospitalData[i]
        if is_valid(tmpData[0]) and is_valid(tmpData[1]):
            lngId = int((tmpData[0] - gloV.LNG_MIN) / gloV.lngLeap)
            latId = int((tmpData[1] - gloV.LAT_MIN) / gloV.latLeap)
            gloV.gridHospitalCount[latId][lngId] += 1
            gridHospitalRemarkS[latId][lngId] += gloV.hospitalScore[i]
            for j in gridHospitalValidName:
                if is_valid(tmpData[gloV.hospitalVariableNamePosition[j]]):
                    gloV.gridHospitalValid[j][latId][lngId].append(tmpData[gloV.hospitalVariableNamePosition[j]])

    paraDemandSum = gloV.paraDemandScore + gloV.paraDemandShop
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            gridDemandTmp[i][j] = (gloV.gridCommunityScoreS[i][j] * gloV.paraDemandScore +
                                   gloV.gridShopCount[i][j] * gloV.paraDemandShop) / paraDemandSum

    demandTmpMin = get_min(gridDemandTmp)
    demandTmpMax = get_max(gridDemandTmp)
    competeMin = get_min(gridHospitalRemarkS)
    competeMax = get_max(gridHospitalRemarkS)
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            gloV.gridDemand[i][j] = zoom_data(gridDemandTmp[i][j], demandTmpMin, demandTmpMax)
            gloV.gridCompete[i][j] = zoom_data(gridHospitalRemarkS[i][j], competeMin, competeMax)
            gloV.gridValue[i][j] = gloV.gridDemand[i][j] * gloV.paraFinalDemand - \
                                   gloV.gridCompete[i][j] * gloV.paraFinalCompete

    gloV.gridOutput = make_zeros(len(gloV.latGrid) - 1, len(gloV.lngGrid) - 1)
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            # '社区-%s-求和,社区-%s-平均值,社区-%s-缺失率,'
            wc = ''
            for k in gloV.gridCommunityValid:
                wc += (str(sum(gloV.gridCommunityValid[k][i][j])) + ',')
                wc += (str(d1(sum(gloV.gridCommunityValid[k][i][j]), len(gloV.gridCommunityValid[k][i][j]))) + ',')
                wc += (str(d1((gloV.gridCommunityCount[i][j] - len(gloV.gridCommunityValid[k][i][j])), gloV.gridCommunityCount[i][j])) + ',')

            ws = ''
            for k in gloV.gridShopValid:
                ws += (str(sum(gloV.gridShopValid[k][i][j])) + ',')
                ws += (str(d1(sum(gloV.gridShopValid[k][i][j]), len(gloV.gridShopValid[k][i][j]))) + ',')
                ws += (str(d1(gloV.gridShopCount[i][j] - len(gloV.gridShopValid[k][i][j]), gloV.gridShopCount[i][j])) + ',')

            wh = ''
            for k in gloV.gridHospitalValid:
                wh += (str(sum(gloV.gridHospitalValid[k][i][j])) + ',')
                wh += (str(d1(sum(gloV.gridHospitalValid[k][i][j]), len(gloV.gridHospitalValid[k][i][j]))) + ',')
                wh += (str(d1((gloV.gridHospitalCount[i][j] - len(gloV.gridHospitalValid[k][i][j])), gloV.gridHospitalCount[i][j])) + ',')

            # "社区个数,宠物店个数,医院个数," +
            # "社区-评分-求和,社区-评分-平均值," +
            # wC + wS + wH +
            # "Demand,Compete,Value," +
            # "社区-2000年前竣工-总计,社区-2000年前竣工-比例," +
            # "社区-别墅-总计,社区-别墅-比例" + "\n"
            w1 = str(gloV.gridCommunityCount[i][j]) + ',' + str(gloV.gridShopCount[i][j]) + ',' + str(gloV.gridHospitalCount[i][j]) + ',' + \
                str(gloV.gridCommunityScoreS[i][j]) + ',' + str(d1(gloV.gridCommunityScoreS[i][j], gloV.gridCommunityCount[i][j])) + ',' + \
                wc + ws + wh + \
                str(gloV.gridDemand[i][j]) + ',' + str(gloV.gridCompete[i][j]) + ',' + str(gloV.gridValue[i][j]) + ',' + \
                str(gloV.gridCommunityVillaCount[i][j]) + ',' + str(d1(gloV.gridCommunityVillaCount[i][j], gloV.gridCommunityCount[i][j])) + ',' + \
                str(gloV.gridCommunityBefore2000Count[i][j]) + ',' + str(d1(gloV.gridCommunityBefore2000Count[i][j], gloV.gridCommunityCount[i][j])) + ',' + str(gloV.generateTime) + '\n'
            gloV.gridOutput[i][j] = w1


def writeGrid(fileGridName):
    fileGrid = open(fileGridName, 'w+', encoding='gb2312')

    wC = ''
    for i in gloV.gridCommunityValid:
        wC += ('社区-%s-求和,社区-%s-平均值,社区-%s-缺失率,' % (i, i, i))
    wS = ''
    for i in gloV.gridShopValid:
        wS += ('Shop-%s-求和,Shop-%s-平均值,Shop-%s-缺失率,' % (i, i, i))
    wH = ''
    for i in gloV.gridHospitalValid:
        wH += ('Hospital-%s-求和,Hospital-%s-平均值,Hospital-%s-缺失率,' % (i, i, i))

    fileGrid.writelines("Pic-Group,Path,Grid-Id,Latitude,Longitude," +
                        "Draw," +
                        "社区个数,宠物店个数,医院个数," +
                        "社区-评分-求和,社区-评分-平均值," +
                        wC + wS + wH +
                        "Demand,Compete,Value," +
                        "社区-2000年前竣工-总计,社区-2000年前竣工-比例,社区-别墅-总计,社区-别墅-比例,GenerateTime" + "\n")

    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridCommunityScoreS[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "1-社区评分,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "1-社区评分,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "1-社区评分,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "1-社区评分,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()

    fileGrid = open(fileGridName, 'a', encoding='gb2312')
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridShopCount[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "2-宠物店,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "2-宠物店,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "2-宠物店,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "2-宠物店,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()
    print('Writing Grid.csv ...20%')

    fileGrid = open(fileGridName, 'a', encoding='gb2312')
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridHospitalCount[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "3-医院数,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "3-医院数,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "3-医院数,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "3-医院数,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()
    print('Writing Grid.csv ...40%')

    fileGrid = open(fileGridName, 'a', encoding='gb2312')
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridDemand[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "4-Demand,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "4-Demand,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "4-Demand,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "4-Demand,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()
    print('Writing Grid.csv ...60%')

    fileGrid = open(fileGridName, 'a', encoding='gb2312')
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridCompete[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "5-Compete,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "5-Compete,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "5-Compete,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "5-Compete,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()
    print('Writing Grid.csv ...80%')

    fileGrid = open(fileGridName, 'a', encoding='gb2312')
    for i in range(0, len(gloV.latGrid) - 1):
        for j in range(0, len(gloV.lngGrid) - 1):
            w1 = str(gloV.gridValue[i][j]) + ',' + gloV.gridOutput[i][j]
            w = "6-Value,1," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j]) + "," + w1

            w += "6-Value,2," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "6-Value,3," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j + 1]) + "," + w1

            w += "6-Value,4," + str(gloV.gridId[i][j]) + "," + str(gloV.latGrid[i + 1]) + "," + str(gloV.lngGrid[j]) + "," + w1
            fileGrid.writelines(w)

    fileGrid.close()
    print('<Output-Grid.csv> 输出完毕!')


def run():
    """
    :return:
    -1 表示<辅助信息.csv>编码不明,或人均可支配收入无法转换成数字;
    -2 表示<小区信息.csv>编码不明,或文件前6列列标题不是 [经度,纬度,区县,容积率,均价,现有户数] 顺序;
    """

    # -------------------------------------------Read----------------------------------------------------
    # ---------- 辅助信息 清洗与检验
    fileHelpName = "Help.csv"
    returnHelp = readHelpCSV(fileHelpName)
    if returnHelp < 0:
        # -1: 文件无法打开
        # -2: 文件编码不明(以第一个单元格是否可以读取成 "城市" 为准)
        # -3: 区县人均可支配收入 不是数字
        return returnHelp

    # ---------- 生成网格
    generateGrid(gloV.lngKm, gloV.latKm, (gloV.LAT_MIN + gloV.LAT_MAX) / 2)

    # ---------- Community Shop Hospital 信息 读取与清洗
    readSaveCommunity = Community.run()
    if readSaveCommunity == 'NO_SAVE.':
        print('\n\n******* 重要错误 ********\n\n未读取 Community.csv, 需先运行 Community.py.\n\n*********\n')
        return -1
    if readSaveCommunity == 'NO_DATA.':
        print('\n\n******* 重要错误 ********\n\n没有本城市的 社区 数据点\n\n*********\n')
        return -1

    readSaveShopHospital = ShopHospital.run()
    if readSaveShopHospital == 'NO_SAVE.':
        print('\n\n******** 重要错误 *******\n\n未读取 Shop.csv 和 Hospital.csv, 需先运行 ShopHospital.py.\n\n*********\n')
        return -1
    if readSaveShopHospital == 'NO_DATA.':
        print('\n\n******** 重要错误 *******\n\n\n\n*****没有本城市的 ShopHospital 数据点****\n')
        return -1

    # ---------------------------------------------Compute--------------------------------------------------
    # ---------- 数据缺失率统计 与 基本统计量
    gloV.communitySummary = compute_summary('<社区>', gloV.communityVariableNameStr, gloV.communityVariableName,
                                            len(gloV.communityData), gloV.communityValid, gloV.communityDataType, "w+")
    gloV.shopSummary = compute_summary('<宠物店>', gloV.shopVariableNameStr, gloV.shopVariableName, len(gloV.shopData),
                                       gloV.shopValid, gloV.shopDataType, "a")
    gloV.hospitalSummary = compute_summary('<宠物医院>', gloV.hospitalVariableNameStr, gloV.hospitalVariableName,
                                           len(gloV.hospitalData), gloV.hospitalValid, gloV.hospitalDataType, "a")

    # ---------- 基于Grid的计算: 得到gridCommunity, gridDemand, gridCompete, gridValue
    computeGrid()

    # -------------------------------------------Write----------------------------------------------------
    shopHospitalOutput = merge_output(gloV.shopOutput, 'Shop', gloV.hospitalOutput, '医院')
    allOutput = merge_output(gloV.communityOutput, '社区', shopHospitalOutput, 'Shop或医院')

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
    print('\n<Output-Point.csv> 输出完毕!')

    fileGridName = "Output-Grid.csv"
    writeGrid(fileGridName)

    return 0


if __name__ == "__main__":
    run()
