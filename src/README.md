### 로그인 시스템 만들기

---
### 1. 초기 사용자 목록 생성
- 프로그램 실행시 전체 사용자 목록 구조적으로 출력
  <img width="520" height="720" alt="image" src="https://github.com/user-attachments/assets/1dc22a47-fdaf-4b18-9ade-e535b61a0db6" />


### 2. 회원가입
- 입력된 생년월일이 유효한 날짜인지 확인
  <img width="520" height="84" alt="image" src="https://github.com/user-attachments/assets/ff593f04-90b3-479a-9663-834a2bc58c5d" />

- 중복된 아이디가 없는지 확인
  <img width="520" height="82" alt="image" src="https://github.com/user-attachments/assets/6354491a-59c2-44a7-8414-c0ab2227cec3" />

- 비밀번호 보안 조건(숫자와 특수문자 조합으로 8자리 이상)에 적합한지 확인
  <img width="520" height="80" alt="image" src="https://github.com/user-attachments/assets/5db23f9d-31a0-4ad8-99b9-6e9ceb271df2" />
  <img width="520" height="76" alt="image" src="https://github.com/user-attachments/assets/8fd1bdf1-a32d-4b49-a6cb-d3eb17319c19" />


### 3. 로그인
- 아이디, 비밀번호 일치 여부
  <img width="1046" height="148" alt="image" src="https://github.com/user-attachments/assets/5f326c4b-130f-4066-a543-bd0b06dc5b9d" />
  <img width="1008" height="112" alt="image" src="https://github.com/user-attachments/assets/9eb3c132-eee1-4fa1-8eda-06111fb53aa0" />

- 사용자 정보 수정 기능(viewer: 자기 자신만, admin, editor: 모든 사용자 정보 수정 가능)
  | viewer | editor&admin |
  |---|---|
  | <img width="884" height="978" alt="image" src="https://github.com/user-attachments/assets/4fd68836-4a05-4f1c-82bb-8c5c20e75f05" /> | <img width="1010" height="430" alt="image" src="https://github.com/user-attachments/assets/7048ea3a-b720-4fa7-afc5-9c159960bcd4" /> |

- 회원탈퇴 기능(viewer&editor: 자기 자신만, admin: 모든 사용자 탈퇴 가능)
  | viewer&editor | admin |
  |---|---|
  | <img width="982" height="652" alt="image" src="https://github.com/user-attachments/assets/cdb5ae93-1382-4813-ac5a-a3a0cecc02ff" /> | <img width="1164" height="648" alt="image" src="https://github.com/user-attachments/assets/86496543-4195-469a-ac27-5a80fc7b3510" /> |
