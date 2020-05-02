from sklearn.ensemble import RandomForestClassifier



domainlist = []

testDomainlist = []

class Domain:#训练数据类

    def __init__(self, _name, _label, _length, _entropy):

        self.name = _name

        self.label = _label

        self.length = _length

        self.entropy = _entropy



    def returnData(self):

        return [self.length, self.entropy]



    def returnLabel(self):

        if self.label == "dga":

            return "dga"

        else:

            return "nodga"







def initData(filename):#初始化训练数据

    with open(filename) as f:

        for line in f:

            line = line.strip()

            if line.startswith("#") or line == "":

                continue

            tokens = line.split(",")

            name = tokens[0]

            label = tokens[1]

            length = len(tokens[0]) 

            entropy = Entropy(tokens[0])

            domainlist.append(Domain(name,label,length,entropy))



class Testdomain:#测试数据类

    def __init__(self, _name, _length, _entropy):

        self.name = _name

        self.length = _length

        self.entropy = _entropy



    def returnTestdata(self):

        return [self.length, self.entropy]





def initTestdata(filename):#初始化测试数据

    with open(filename) as f:

        for line in f:

            line = line.strip()

            if line.startswith("#") or line == "":

                continue

            tokens = line.split(",")

            name = tokens[0]            

            length = len(tokens[0]) 

            entropy = Entropy(tokens[0])

            testDomainlist.append(Testdomain(name,length,entropy))



def Entropy(domain):#计算数字所占熵

    length = len(domain)

    amount = 0

    for letter in domain:

        if 48 <= ord(letter) <= 57:

            amount = amount+1

    entropyOfdomain = amount/length

    return entropyOfdomain





initData("train.txt")#初始化训练数据

featureMatrix = []

labelList = []

for item in domainlist:

    featureMatrix.append(item.returnData())

    labelList.append(item.returnLabel())



clf = RandomForestClassifier(random_state=0)#执行训练

clf.fit(featureMatrix,labelList)





initTestdata("test.txt")#初始化测试文件

testFeatureMatrix = []

testLabelList = []

for item in testDomainlist:

    testFeatureMatrix.append(item.returnTestdata())



resultList = clf.predict(testFeatureMatrix)#进行判决



fresult = open("result.txt","w")#打开result文件并将结果以特定格式写入

for i in range(len(resultList)):

    fresult.write(testDomainlist[i].name)

    fresult.write(",")

    fresult.write(resultList[i])

    fresult.write("\n")

fresult.close()







