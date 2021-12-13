name1 = "ねずこ"
name2 = "ぜんいつ"

if name2 == "むざん":
    print ("仲間ではありません")

name = ["たんじろう","ぎゆう","ねずこ","むざん"]

for i in name:
    print(i)    

def search(i):
    if i in name:
        print(f"{i}は含まれている")     
    
search("ぎゆう")     
  