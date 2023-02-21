def topla(x,y):
    '''
    Parametre olarak verilen iki sayının toplamı dönülür
    örnek: topla(3,6)
    '''
    toplam = x + y
    print(toplam)

def çıkart(x,y):
    fark = x - y
    print(fark)

def çarp(x,y):
    çarpım = x * y
    print(çarpım)

def böl(x,y):
    bölüm = x / y
    print(bölüm)

def kareal(x):
    karesi = x * x
    print(karesi)

def readme():
    print("Basit hesap makinesi modülüne hoşgeldiniz.")
    print("Basit 4 işlem ve kare almak için kullanılabilen bir modüldür.")
    print("Modülün içindeki fonksiyonlarla toplama,çıkarma,çarpma,bölme ve kare alma işlemleri yapabilirsiniz.")
    print("Modülü içe aktarmak için import calculator")
    print("Modül içindeki fonksiyonları kullanmak içinde aşağıdan nasıl kullanılacağına bakabilirsiniz.")
    print("Toplama için calculator.topla(parametre1,parametre2)")
    print("Çıkartma için calculator.çıkart(parametre1,parametre2)")
    print("Çarpma için calculator.çarp(parametre1,parametre2)")
    print("Bölme için calculator.böl(parametre1,parametre2)")
    print("Karesini almak için calculator.kareal(parametre1)")

