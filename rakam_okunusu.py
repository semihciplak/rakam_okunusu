#bu program "Online Programlama Dersleri" youtube kanalından alınmıştır. kodlarla ilgili videoya bu linkten ulaşabilirsiniz.
#https://www.youtube.com/watch?v=W2KA1VOp3P8

#dictionary

def rakam_okunuşu(rakam):
    assert rakam >(-1), "Negatif rakam olamaz."
    assert rakam <10, "Sadece rakam olabilir."
    sayılar= {0:"sıfır", 1:"bir", 2:"iki", 3:"üç", 4:"dört", 5:"beş", 6:"altı", 7:"yedi", 8:"sekiz", 9:"dokuz"}
    return sayılar.get(rakam, "bilinmiyor")


def rakam_işareti(rakam):
    if rakam==0:
        return ""
    elif rakam < 0:
        return "eksi"
    else:
        return "artı"

def işaretli_rakamlar(rakam):
    return rakam_işareti(rakam) + " "+ rakam_okunuşu(abs(rakam))



for x in range(10):
    if x % 2 ==0:
        x=-x
    print(x,"->", işaretli_rakamlar(x))



