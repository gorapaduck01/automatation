import osimport shutil

download = os.path.expanduser("~/Downloads")

for file in os.listdir(download):

# 파일 끝 확장자 소문자로 변환하여 일치하는지 확인하여
# 확장자별로 폴더 생성
if file.lower().endswith((".pdf", ".xlsx", "txt", ".doc", ".ppt", ".docx", ".xls", ".pptx")):folder = "문서"

elif file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
    folder = "이미지"

elif file.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
    folder = "동영상"

elif file.lower().endswith((".mp3", ".wav", ".flac")):
    folder = "음악"

elif file.lower().endswith((".zip", ".rar", ".7z", ".tar", ".gz")):
    folder = "압축 파일"

elif file.lower().endswith((".exe", ".msi")):
    folder = "실행 파일"

else:
    continue

# shutil.move의 첫번째 매개변수에서 두번째 매개변수로 경로 이동 하라는 의미
# exist_ok=True 를 해야 기존에 있는 폴더여도 오류 발생 없이 이동 가능
# join을 해서 묶을 수 있는 이유는 파일 명은 단순히 폴더명을 붙여 분류할 뿐이기 때문
os.makedirs(os.path.join(download, folder),exist_ok=True)
shutil.move(
    os.path.join(download, file),
    os.path.join(download, folder, file)
)

# 오류 발생시 확인할 로그
print("내가 지정한 폴더:", download)print("폴더가 존재하나?:", os.path.exists(download))print("폴더 내용:", os.listdir(download))
