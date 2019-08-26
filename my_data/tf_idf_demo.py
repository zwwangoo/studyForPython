import jieba
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

text = '''
记得废钞令，一夜之间废掉500和1000卢比，让印度社会进入短暂的恐慌，无数底层贱民不懂政策自杀，被我们嘲笑了很久。可真实事情是什么呢？印度一直以来各自为政的地方邦文化语言所困扰，全国几十种语言连身份证制度也好几十种。这根本就不是一个统一的国家该有的制度。于是印度政府准备用用全国统一身份ID来解决这件事情，这个ID还配有一个统一的银行户口。这个计划简称Aadhaar。所有人必须采集面部数据，录入指纹，以及虹膜数据。然后配合ID有一个账户，这个账户政府可以直接打款补助到个人，跳过所有中间环节，印度中间环节腐败不堪，只这一步，就让印度在网络上实现进一步公平。于是莫迪强令全国推广，但是事情进行到一半的时候，就推行不下去了，竟然还有将近六亿人，不肯去开通数字身份ID与账户。因为录入面部，指纹，虹膜十分麻烦，一台设备完成不了，以及印度特有的困难，进度非常难，城市还好说，但是到了农村，事情变难了。因为印度底层人民根本意识不到这是改变印度命运的机会，录入采集十分麻烦，于是无人配合，加上印度人特有的精神，这件事情好像要遥遥无期了。于是废钞令是2016年11月8日晚，印度总理莫迪宣布布，从当日午夜12时起，市面上流通的500卢比和1000卢比面值纸币，将停止流通，但民众仍可将旧版纸币存入银行。大额纸币怎么存入银行，第一必须要开数字身份ID，第二开通全国统一账户。于是印度用了不到半个月，就完成了数字身份ID的普及与推广。目前印度几乎所有的服务都强制要求使用Aadhaa验证，例如，在泰米尔纳德邦，定额物资发放必须使用Aadhaa；因与生物特征识别相关联，法庭事务必须使用Aadhaa；开立银行账户、进行50000卢比以上交易也必须使用Aadhaar。现有账户持有人必须提交Aadhaar信息，否则其账户将被视为无效。随着项目的实施，教育和医疗保健等服务也逐渐纳入其中。印度在2017年初完成了一个全国统一市场的进程，也就是说莫迪完成了困扰印度将近几十年的统一意识问题。而且紧接着在这个基础上，一个比中国还先进的电子支付系统诞生了，原因在于印度央行推进了一个电子货币系统，全国所有的第三方支付都必须在这个系统接口运行，它不同于微信、支付宝，印度所有所有的第三方支付都必须与央行的电子支付系统挂钩。这样所有的第三方支付都印度央行控制，也就是说，印度在这一方面，对第三方控制已经超越中国这种各自为政的局面。
'''

sentences = text.split('。')
sent_words = [list(jieba.cut(x)) for x in sentences]
documents = [' '.join(send0) for send0 in sent_words]

# 停用词表
stop_words = ['的', '是', '吗', '呗', '有', '印度']

tfidf_model = TfidfVectorizer(
    token_pattern=r"(?u)\b\w+\b", max_df=0.6, stop_words=stop_words)
result = tfidf_model.fit_transform(documents)

km = KMeans(n_clusters=3, init='k-means++')
km.fit(result)
order_centroids = km.cluster_centers_.argsort()[:, ::-1]

terms = tfidf_model.get_feature_names()
for i in range(3):
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

re = km.predict(result)
print(-km.score(result))
