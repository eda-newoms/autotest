import time;
import ChooseEnv;

class Sku():
    random = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()));
    skuName = random;
    skuProdNameCn = '自动化脚本创建';
    skuProdNameEn = 'autoTestCase';
    skuLink = ChooseEnv.url;
    skuExtraBarcode1 = 'ExtraBarcode1' + random;
    skuExtraBarcode2 = 'ExtraBarcode2' + random;
    skuExtraBarcode3 = 'ExtraBarcode3' + random;
    skuKeyword = 'skuKeyword';
    skuFiles = '';
    skuDes = 'comments';

    def createSku(self):
        print()





