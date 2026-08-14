import hashlib
import os


p = input("중복 파일을 검사할 폴더 경로를 입력하세요: ")

dic = {}

for filename in os.listdir(p):
    f1 = open(os.path.join(p,filename), "rb")
    data1 = f1.read()
    f1.close()

    data1sha = hashlib.sha256(data1).hexdigest()

    if data1sha not in dic:
        dic[data1sha] = [filename]

    else:
        dic[data1sha].append(filename)
        
    
print(dic)

print("\n========== 중복 파일 ==========")
for f in dic:
    if len(dic[f]) >= 2:
        print("\n중복 파일 그룹:")

        for num, filename in enumerate(dic[f],1):
            print("-",num,".", filename)

        keep = int(input("보존할 파일 번호: "))
        delFile = []

        for num,filename in enumerate(dic[f],1):
            if num != keep:
                delFile.append(filename)

        print("\n삭제 대상: ")
        for filename in delFile:
            print("-", filename)

        ask = input("\n삭제하시겠습니까?(y/n): ")

        if ask.lower() in ["y", "yes", "예", "네"]:
            for filename in delFile:
                print(filename," 제거")
                os.remove(os.path.join(p,filename))
        
        else:
            print("파일 제거 취소")
print("\n중복 파일 검사 완료")
            
