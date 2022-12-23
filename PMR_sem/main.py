# This is a sample Python script.
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def writeToDic(word, pword, file):
    file.write(word.upper() + pword + "\n")


def writeToWlist(word, file):
    file.write(word.upper() + "\n")


def writeToGrammar(word, file):
    file.write(word.upper() + "|")


def ToPhonem(sentence):
    ZPS = 'bdďgzžvhCČŘ'
    JS = 'mnňljr'
    SA = 'aáeiíoóuúů'
    NPS = 'ptťksšfXcčř'





    sentence = sentence.replace('di', 'ďi')
    sentence = sentence.replace('ti', 'ťi')
    sentence = sentence.replace('ni', 'ňi')
    sentence = sentence.replace('dí', 'ďí')
    sentence = sentence.replace('tí', 'ťí')
    sentence = sentence.replace('ní', 'ňí')
    sentence = sentence.replace('ch', 'X')
    sentence = sentence.replace('ů', 'ú')
    sentence = sentence.replace('w', 'v')
    sentence = sentence.replace('q', 'kv')
    sentence = sentence.replace('y', 'i')
    sentence = sentence.replace('ý', 'í')
    sentence = sentence.replace('bě', 'bje')
    sentence = sentence.replace('pě', 'pje')
    sentence = sentence.replace('fě', 'fje')
    sentence = sentence.replace('vě', 'vje')
    sentence = sentence.replace('dě', 'ďe')
    sentence = sentence.replace('tě', 'ťe')
    sentence = sentence.replace('ně', 'ňe')
    sentence = sentence.replace('mě', 'mňe')
    sentence = sentence.replace('nk', 'Nk')
    sentence = sentence.replace('ng', 'Ng')
    sentence = sentence.replace('mf', 'Mf')
    sentence = sentence.replace('mv', 'Mv')
    sentence = sentence.replace('ts', 'c')
    sentence = sentence.replace('tš', 'č')
    sentence = sentence.replace('ds', 'c')
    sentence = sentence.replace('dš', 'č')
    sentence = sentence.replace('dz', 'C')
    sentence = sentence.replace('dž', 'Č')
    sentence = sentence.replace(' ex', ' egz')

    sentence = remDup(sentence)
    sentence = "__" + sentence + "__"

    sentence = NPS2ZPS(sentence)
    sentence = remDup(sentence)
    sentence = "_" + sentence + "_"
    sentence = r2R(sentence)
    sentence = remDup(sentence)
    sentence = "_" + sentence + "_"
    sentence = ZPS2NPS(sentence)
    sentence = remDup(sentence)
    sentence = "_" + sentence + "_"

    while (True):
        index = sentence.find('x')
        if index == -1:
            break

        if sentence[index + 1] in ZPS:
            sentence = sentence.replace('x', 'gz')
        elif sentence[index + 1] in JS:
            sentence = sentence.replace('x', 'gz')

        if sentence[index + 1] in NPS:
            sentence = sentence.replace('x', 'ks')
        elif sentence[index + 1] == ' ':
            sentence = sentence.replace('x', 'ks')

        if sentence[index + 1] in SA and sentence[index - 1] == ' ':
            sentence = sentence.replace('x', 'ks')
        elif sentence[index + 1] in SA and sentence[index - 1] in SA:
            sentence = sentence.replace('x', 'ks')
        else:
            sentence = sentence.replace('x', 'ks')


    return (sentence)


def remDup(text):
    result = []
    for x in text:
        if not result or result[-1] != x:
            result.append(x)
    return ''.join(result)


def ZPS2NPS(sentence):
    ZPS = 'bdďgzžvhCČř'
    NPS = 'ptťksšfXcčŘ'
    for i in range(0, len(ZPS)):
        for index in range(2, len(sentence) - 2):
            if sentence[index] == ZPS[i]:
                if sentence[index + 1] in ZPS and sentence[index + 1] == '_' or sentence[index + 2] == '_' or sentence[
                    index + 1] in NPS:
                    sentence = sentence[:index] + NPS[i] + sentence[index + 1:]
    return (sentence)


def NPS2ZPS(sentence):
    ZPS = 'bdďgzžvhCČř'
    NPS = 'ptťksšfXcčŘ'
    for i in range(0, len(ZPS)):
        for index in range(2, len(sentence) - 2):
            if sentence[index] == NPS[i]:
                if sentence[index + 1] in ZPS:
                    sentence = sentence[:index] + ZPS[i] + sentence[index + 1:]
    return sentence


def r2R(sentence):
    ZPS = 'bdďgzžvhCČř'
    NPS = 'ptťksšfXcčŘ'
    for index in range(2, len(sentence) - 2):
        if sentence[index] == 'ř':
            if sentence[index + 1] in ZPS and sentence[index + 2] == ' ' or sentence[index + 2] == ' ' or sentence[
                index - 1] in NPS:
                sentence = sentence[:index] + 'Ř' + sentence[index + 1:]
    return sentence


def ToHTK(sentence):
    rep = ""
    for i in range(0, len(sentence)):
        rep = rep + " " + sentence[i]
    sentence = rep
    sentence = sentence.replace('á', 'aa')
    sentence = sentence.replace('c', 'ts')
    sentence = sentence.replace('C', 'dz')
    sentence = sentence.replace('č', 'ch')
    sentence = sentence.replace('Č', 'dg')
    sentence = sentence.replace('ď', 'dj')
    sentence = sentence.replace('é', 'ee')
    sentence = sentence.replace('X', 'x')
    sentence = sentence.replace('í', 'ii')
    # sentence = sentence.replace( 'j', 'y')
    sentence = sentence.replace('M', 'mg')
    sentence = sentence.replace('N', 'ng')
    sentence = sentence.replace('ň', 'nj')
    sentence = sentence.replace('ó', 'oo')
    sentence = sentence.replace('ř', 'rz')
    sentence = sentence.replace('Ř', 'rs')
    sentence = sentence.replace('š', 'sh')
    sentence = sentence.replace('ť', 'tj')
    sentence = sentence.replace('ú', 'uu')
    sentence = sentence.replace('ž', 'zh')
    return (sentence)


def removeDia(w):
    w = w.lower()
    w = w.replace("š", "s")
    w = w.replace("ě", "e")
    w = w.replace("ř", "r")
    w = w.replace("č", "c")
    w = w.replace("í", "i")
    w = w.replace("á", "a")
    w = w.replace("ď", "d")
    w = w.replace("é", "e")
    w = w.replace("ň", "n")
    w = w.replace("ó", "o")
    w = w.replace("ť", "t")
    w = w.replace("ú", "u")
    w = w.replace("ů", "u")
    w = w.replace("ž", "z")
    w = w.replace("ý", "y")
    return w

def remove_non_letters(string):
    return re.sub(r'[^a-zA-Z]', '', string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import unicodedata
    n = 20000
    path = 'D:/Matlab_skripts/PMR/sem/train_text_korpus.txt'
    wnum = 0
    wlist = {}
    with open(path, mode="r", encoding="CP1250") as file:
        txt = file.read()
    txt = txt.split()
    for word in txt:
        # word = word.replace('/','')
        # word = word.replace('.','')
        # word = word.replace(',','')
        # word = word.replace('-','')
        # word = word.replace('_','')
        # word = word.replace('+','')
        # word = word.replace('-','')
        # word = word.replace('*','')
        # word = word.replace('%','')
        # word = word.replace('÷','')
        # word = word.replace('&','')
        # word = word.replace('@','')
        # word = word.replace('1','')
        # word = word.replace('2','')
        # word = word.replace('3','')
        # word = word.replace('4','')
        # word = word.replace('5','')
        # word = word.replace('6','')
        # word = word.replace('7','')
        # word = word.replace('8','')
        # word = word.replace('9','')
        # word = word.replace('0','')
        # word = word.replace('^','')
        # word = word.replace('"','')
        # word = word.replace('!','')
        # word = word.replace('(','')
        # word = word.replace(')','')
        # word = word.replace('[','')
        # word = word.replace(']','')
        # word = word.replace('{','')
        # word = word.replace('}','')
        # word = word.replace('\'','')
        # word = word.replace('ß','')
        # word = word.replace('$','')
        # word = word.replace('¤','')
        # word = word.replace('?','')
        # word = word.replace(':','')
        # word = word.replace('=','')
        # word = word.replace('÷','')
        word = re.sub('[^aábcčdďeéěfghiíjklmnňoópqrřsštťuůúvwxyýzžAÁBCČDĎEÉĚFGHIÍJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYÝZŽ]', '', word)

        wnum += 1
        word = word.lower()
        if word in wlist.keys():

            wlist[word] = wlist[word] + 1
        else:
            wlist[word] = 1

    # print(wlist)
    plist = []
    path = 'C:/Users/Horky/PycharmProjects/PMR_experiment/lexicon'
    path2 = 'C:/Users/Horky/PycharmProjects/PMR_experiment/wlist'
    path3 = 'C:/Users/Horky/PycharmProjects/PMR_experiment/grammar'
    for key, value in dict(sorted(wlist.items(), key=lambda item: item[1],reverse=True)).items():
        if n>len(plist):
            # print(str(len(plist)))
            pword = ToPhonem(key)
            pword = pword.replace('_', '')
            pword = ToHTK(pword)
            # plist[removeDia(key)] = pword
            item = [removeDia(key),pword]
            plist.append(item)
    plist.sort()

    # musí se umazat poslední "|"
    with open(path3, mode="w", encoding="CP1250") as file:
        file.write("$digit = ")
        for item in plist:
            writeToGrammar(item[0], file)
        file.write(";\n( SENT-START < $digit {SENT-START} > SENT-END )\n")

    item = ["sent-start", " si"]
    plist.append(item)
    item = ["sent-end", " si"]
    plist.append(item)
    plist.sort()
    wwlist = []
    with open(path, mode="w", encoding="CP1250") as file:
        for item in plist:
            writeToDic(item[0], item[1], file)
            wwlist.append(item[0])
    wwlist = list(dict.fromkeys(wwlist))

    with open(path2, mode="w", encoding="CP1250") as file2:
        for word in wwlist:
            writeToWlist(word, file2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
