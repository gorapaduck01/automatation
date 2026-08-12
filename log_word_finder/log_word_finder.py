p = input("로그 파일 경로: ")
word = input("검색할 단어: ")
wordCnt = 0
ipDic = {}
# arr = []을 사용하려 했으나 set으로 변경
ipSet = set()
total = 0

# 각 ip별 로그 발생 건수
with open(p,"r") as file:
    for line in file:
        # ip만 분리
        LS = line.split()
        ip = LS[2]

        # ipDic에 있는 ip인지 아닌지에 따라 =1 or +=1
        if ip not in ipDic:
            ipDic[ip] = 1
        else:
            ipDic[ip] += 1
            
            
print("\n")
print("-----------각 ip별 로그 발생 건수-------------")
for ip, ipCnt in ipDic.items():
    print(ip,": ", ipCnt, "건")
    total+= ipCnt

print("총 로그 발생 건수: ", total, " 건")

print("----------------------------------------------")    

# 입력한 word 존재하는 line 찾기
with open(p, "r") as file:
    for line in file:
        if word in line:
            LS = line.split()
            ip = LS[2]
            
            print(line, end='')
            wordCnt += 1
            ipSet.add(ip)
            
print("\n")
print("----------------------------------------------")
print("검색 결과: ", wordCnt, "건")

# 입력한 word 존재하는 ip와 해당 ip에 발생한 건수 출력
for i in ipSet:
    print("발생 ip: ", i, " -> ", ipDic[i],"건")
  
