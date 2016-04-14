# coding: utf-8

# -------------------- 可调节参数 --------------------
LNG_MIN = 73.5
LNG_MAX = 135.1
LAT_MIN = 18.0
LAT_MAX = 53.6

lngKm = 2  # 单位是千米
latKm = 2

generateTime = '2016/3/4'

paraFamilyMax = 3000

paraHospitalRemarkCut = 10

paraPayIncome = 1
paraPayPrice = 6
paraPayRongjilv = 3

paraCommunityPay = 1
paraCommunityFamily = 2

paraDemandScore = 9
paraDemandShop = 1

paraFinalDemand = 1
paraFinalCompete = 0.3

paraYearMin = 1900
paraYearMax = 2050

# -------------------- 全局变量 --------------------
# ---------- Help Data and Grid Basic
currentCity = ''
incomeList = {}                 # 人均可支配收入词典
incomeListKeys = []

lngLeap = 0                     # 每个方格跨越的经度有多大, 2Km -> 0.02度
latLeap = 0

lngGrid = []                    # 列向量, 经度上的切分点, 比切成的段数多1个
latGrid = []
gridId = []                     # 矩阵, 每个方格的编号, 600行 * 400列


# ---------- Community Data
# 经度,纬度,区县,容积率,均价,现有户数,小区名,管理费,绿化率,开发商,街道名称,物业公司,小区类型,地址,
# 小区特点,竣工时间,环线位置,建筑类别,建筑结构,建筑面积,占地面积,价格环比增长,价格同比增长,总户数

communityVariableNameStr = ""   # 社区.csv 文件的列标题split之前的字符串, 已strip
communityVariableName = []      # 列向量, 社区.csv 文件的列标题List. 24列
communityVariableNamePosition = {}  # 每个列名对应的是第几列, 从0开始记

communityDataAll = []           # 矩阵, 全国社区.csv 文件中的所有原始数据. 已清洗(数字 和 "NULL" 混合). 3000000行 * 24列
communityData = []              # 矩阵, 社区.csv 文件中的所有原始数据. 已清洗(数字 和 "NULL" 混合). 3000行 * 24列
communityOutput = []            # 矩阵, 刚开始形状同communityData, 每个格子内都是字符串, 没有逗号. 最特殊的一点是 区县 那一列
communityValid = {}             # 各变量的有效数据List, 以 <变量名communityVariableName> 为词典索引

communityIsVilla = []           # 列向量, 3000行. 0-1变量. 1-是别墅, 0-不是别墅
communityIsBefore2000 = []      # 列向量, 3000行. 0-1变量. 1-竣工时间早于2000年, 0-没那么早

communitySummary = []

communityGridId = []            # 列向量, 每个社区的Grid-Id
communityScore = []             # 列向量, 每个社区的"综合评分", <1.1居民支付能力> + 2*<1.2居民数量> => 转换成1~5之后的结果


# ---------- Shop Data
shopVariableNameStr = ""
shopVariableName = []
shopVariableNamePosition = {}

shopDataAll = []
shopData = []
shopOutput = []
shopValid = {}

shopSummary = []

shopGridId = []


# ---------- Hospital Data
hospitalVariableNameStr = ""
hospitalVariableName = []
hospitalVariableNamePosition = {}

hospitalDataAll = []
hospitalData = []
hospitalOutput = []
hospitalValid = {}

hospitalSummary = []

hospitalGridId = []
hospitalScore = []

# ---------- Grid Data
# --- Community
gridCommunityCount = []             #
gridCommunityValid = {}             # 以变量名称进入后, 是一个矩阵, 存储每个Grid内的 该变量 的有效数据.

gridCommunityScoreS = []            # 矩阵, 小区评分求和
gridCommunityVillaCount = []        #
gridCommunityBefore2000Count = []   #

# --- Shop
gridShopCount = []                  # 矩阵, Shop个数求和
gridShopValid = {}

# --- Hospital
gridHospitalCount = []              #
gridHospitalValid = {}              # 以变量名称进入后, 是一个矩阵, 存储每个Grid内的 该变量 的有效数据.

gridDemand = []                 # 矩阵, zoom到1~5
gridCompete = []                # 矩阵, zoom到1~5
gridValue = []                  # 矩阵, Demand - Compete结果
gridOutput = []

# ---------- Other
SAVE = []
SAVE_COMMUNITY = []

CN_LNG_MIN = 73.5
CN_LNG_MAX = 135.1
CN_LAT_MIN = 18.0
CN_LAT_MAX = 53.6

EXCEL_DATE = 693594
EXCEL_2000_DATE = 36526

# 1 经度:float, 大小限制为 [LNG_MIN, LNG_MAX]
# 2 纬度:float, 大小限制为 [LAT_MIN, LAT_MAX]
# 3 正数字:float, 严格大于零
# 4 数字:float, 其余无限制
# 5 行政区划:字符串, 必须能在gloV.incomeList{}中有匹配字段
# 6 字符串:非空
# 7 整数:int, 非负
# 8 日期:字符串 或 int, 支持4种格式 '36526' '2000/1/1' '2000-1-1' '2000 1 1'
communityDataType = {
    '经度': 1,
    '纬度': 2,
    '区县': 6,  # 之前这里设置的是5
    '容积率': 3,
    '均价': 3,
    '现有户数': 3,

    '名称': 6,
    '城市': 6,
    '竣工时间': 8,
    '总户数': 3,

    '管理费': 3,
    '绿化率': 3,
    '开发商': 6,
    '区域': 6,
    '物业公司': 6,
    '小区类型': 6,
    '地址': 6,
    '小区特点': 6,

    '环线位置': 6,
    '建筑类别': 6,
    '建筑结构': 6,
    '建筑面积': 3,
    '占地面积': 3,
    '价格环比增长': 4,
    '价格同比增长': 4,

    '创建时间': 8,
    '更新时间': 8
}

shopDataType = {
    '经度': 1,
    '纬度': 2,
    '点评数': 7,

    '名称': 6,
    '是否连锁': 7,
    '全国连锁关联同名数': 7,
    '关联店名': 6,
    '地址': 6,
    '区域': 6,
    '区县': 6,
    '平均消费': 7,
    '评分': 7,
    '创建时间': 8,

    '电话': 6
}
hospitalDataType = {
    '经度': 1,
    '纬度': 2,
    '点评数': 7,

    '名称': 6,
    '是否连锁': 7,
    '全国连锁关联同名数': 7,
    '关联店名': 6,
    '地址': 6,
    '区域': 6,
    '区县': 6,
    '平均消费': 7,
    '评分': 7,
    '创建时间': 8,

    '电话': 6
}

