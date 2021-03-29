# obs-stream-setter
밴드 라이브 방송 시 제목을 자동으로 입력하고 스트림키를 발급받은 후 해당 값을 OBS에 자동으로 설정해주는 앱
- AHK를 사용한 자동 제목입력, 스트림키 발급
- obs-websocket을 이용한 OBS 설정 변경


### Requirements
- Python3
- Auto Hot Key
- OBS
- [obs-websocket](https://github.com/Palakis/obs-websocket/releases)
  - installer version 설치
  - 설치 후 OBS를 켜고 port, password설정 (e.g. 4444/1234)


## Usage
1. BandStreamSetter.ahk를 실행한다.
2. OBS를 실행한다.
3. 밴드 라이브방송 시작하기 창을 띄우고 F4키를 누른다.
4. 설정 값을 확인후 y또는 n을 누른다.
5. 설정 값이 문제가 없다면 방송시작을 누른다.
