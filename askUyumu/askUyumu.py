loop = True
while loop == True:
    try:
        import random as r

        qstn = "e"
        while qstn == "e":

            male = input("Erkek: ")
            female = input("Kadın: ")
            percent = r.randint(1, 100)
            male = male.capitalize()
            female = female.capitalize()
            if male == "Berk" and female == "Buse":
                print("Aşk Uyumunuz: Ölçülemeyecek Kadar Yüksek")
                qstn = input("Tekrar Denemek İster Misiniz? (e/h): ")
                if qstn == "h":
                    loop = False
                while qstn != "e" and qstn != "h":
                    print("Yanlış Komut Girdiniz!")
                    qstn = input("Tekrar Denemek İster Misiniz? (e/h): ")
                    if qstn == "h":
                        loop = False
            else:
                print("Aşk Uyumunuz: %", percent)
                qstn = input("Tekrar Denemek İster Misiniz? (e/h): ")
                if qstn == "h":
                    loop = False
                while qstn != "e" and qstn != "h":
                    print("Yanlış Komut Girdiniz!")
                    qstn = input("Tekrar Denemek İster Misiniz? (e/h): ")
                    if qstn == "h":
                        loop = False
    except:
        print("Hata Oluştu!")
        loop = True



    
