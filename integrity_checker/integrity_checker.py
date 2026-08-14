import hashlib
import os
import json

p = input("검사할 폴더 경로: ")
hashDic = {}

for filename in os.listdir(p):
    file = open(os.path.join(p, filename), "rb")
    data = file.read()
    file.close()

    sha = hashlib.sha256(data).hexdigest()

    print(filename, "->", sha)
    
    hashDic[filename] = sha


if os.path.exists("hash.json"):
    ask = input("번호를 입력해주세요.\n1. 무결성 검사 시작\n2. 프로그램 종료\n")

    if ask == "1":
        with open("hash.json", "r") as file:
            oldHashDic = json.load(file)

            for filename in hashDic:
                if filename not in oldHashDic:
                    print("새로운 파일: ", filename)
                    
                elif hashDic[filename] != oldHashDic[filename]:
                    print("무결성 불일치: ", filename)
                
                else:
                    print("정상: ", filename)
            for filename in oldHashDic:
                if filename not in hashDic:
                    print("삭제된 파일: ", filename)
        
    
    else:
        print("프로그램을 종료합니다.")
                    

else:
    # json에 hashDic 저장 <- 프로그램 종료해도 hashDic 데이터 유지
    with open("hash.json", "w") as file:
        json.dump(hashDic, file, indent = 4)
    
    
    
