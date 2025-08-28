import json
from enum import Enum

# 역할정의 (Role)
class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


# 초기 사용자 목록 생성
users = {
    # admin 계정
    "admin": {
        "name": "admin",
        "birth": "2000-01-01",
        "pwd": "password123!",
        "role": Role.ADMIN.value
    },
    # editor 계정
    "surim": {
        "name": "yeomsurim",
        "birth": "2000-06-27",
        "pwd": "password123!",
        "role": Role.EDITOR.value
    },
    # viewer 계정
    "user1": {
        "name": "user1",
        "birth": "1999-06-09",
        "pwd": "password123!",
        "role": Role.VIEWER.value
    }
}

# 프로그램 실행시 전체 사용자 목록 구조적으로 출력
print("============ 초기 사용자 ============")
print(json.dumps(users, indent=2))

mode = input("회원가입(1), 로그인(2): ")

# 회원가입
if mode == "1":
    id = input("Enter your ID: ")
    if id in users: # 아이디 중복 검사
        print("아이디 중복입니다.")
        exit()
    name = input("Enter your name: ")
    birth = input("Enter your birth(0000-00-00): ")
    # 생년월일 유효 검사
    birth_list = list(map(int, birth.split("-")))   # 리스트로 숫자 저장 [2000, 06, 27]
    if birth_list[0] > 2025:    # 연도 유효 검사
        print("날짜를 잘못 입력하셨습니다.")
        exit()
    if 0 == birth_list[1] or 13 <= birth_list[1]:     # 달 유효 검사
        print("날짜를 잘못 입력하셨습니다.")
        exit()
    if 0 == birth_list[2] or 32 <= birth_list[2]:
        print("날짜를 잘못 입력하셨습니다.")
        exit()
    pwd = input("Enter your password: ")
    # 비밀번호 유효 검사 (특수문자를 포함하여 8자리 이상)
    if len(pwd) < 8:
        print("비밀번호 길이가 짧습니다.")
        exit()
    if pwd.isalnum() == True:
        print("비밀번호에 특수문자를 포함해주세요.")
        exit()

    # 사용자 추가
    users = {
        id: {
            "name": name,
            "birth": birth,
            "pwd": pwd,
            "role": Role.VIEWER.value
        }
    }
    print(f"아이디 {id}님의 정보가 추가 되었습니다.")
    print(json.dumps(users[id], indent=2))

# 로그인
elif mode == "2":
    login_id = input("ID를 입력해주세요: ")
    login_pwd = input("비밀번호를 입력해주세요: ")
    if login_id not in users:
        print("사용자를 찾을 수 없습니다.")
        exit()
    if login_pwd != users[login_id]["pwd"]:
        print("비밀번호가 틀렸습니다.")
        exit()
    print(f"{users[login_id]["name"]}님 로그인 성공!")
    while True:
        login_mode = input("사용자 정보 수정(1), 회원 탈퇴(2): ")
        # 사용자 정보 수정
        if login_mode == "1":
            if users[login_id]["role"] == Role.VIEWER.value:    # 자신 정보만 수정 가능
                modi = input("수정할 항목을 작성해주세요 (name, birth, pwd): ")
                modi_content = input("수정할 내용을 작성해주세요: ")
                if modi == 'pwd':
                    while True:
                        if len(modi_content) < 8:
                            print("비밀번호 길이가 짧습니다.")
                            modi_content = input("비밀번호를 다시 작성해주세요: ")
                        if modi_content.isalnum() == True:
                            print("비밀번호에 특수문자를 포함해주세요.")
                            modi_content = input("비밀번호를 다시 작성해주세요: ")
                        break
                # 정보 교체
                users[login_id][modi] = modi_content
                print("사용자 정보 수정 완료")
                print(json.dumps(users[login_id], indent=2))
            else:
                modi_user = input("수정할 유저 아이디를 입력해주세요: ")
                modi = input("수정할 항목을 작성해주세요 (name, birth, pwd): ")
                modi_content = input("수정할 내용을 작성해주세요: ")
                if modi == 'pwd':
                    while True:
                        if len(modi_content) < 8:
                            print("비밀번호 길이가 짧습니다.")
                            modi_content = input("비밀번호를 다시 작성해주세요: ")
                        if modi_content.isalnum() == True:
                            print("비밀번호에 특수문자를 포함해주세요.")
                            modi_content = input("비밀번호를 다시 작성해주세요: ")
                            break
                # 정보 교체
                users[modi_user][modi] = modi_content
                print(f"{modi_user} 사용자 정보 수정 완료")
                print(json.dumps(users[modi_user], indent=2))
        # 회원탈퇴
        elif login_mode == "2":
            if users[login_id]["role"] == Role.ADMIN.value: # 모든 계정 삭제 가능
                del_user = input("탈퇴시킬 회원 아이디를 입력하세요: ")
                del users[del_user]
                print(f"{del_user} 사용자가 탈퇴되었습니다.")
                print(json.dumps(users, indent=2))
            else:
                aws = input("정말 탈퇴하시겠습니까(y/n)? ")
                if aws == "y":
                    del users[login_id]
                    print(f"{login_id} 사용자가 탈퇴되었습니다.")
                    print(json.dumps(users, indent=2))
                    exit() # 종료
                else:
                    print("회원탈퇴 중지")
        # 종료
        else:
            print("시스템을 종료합니다.")
            exit()
else:
    print("잘못된 입력입니다.")
    exit()