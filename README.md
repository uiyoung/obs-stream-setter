# obs-stream-setter

네이버 밴드 라이브 방송 시 제목을 자동으로 입력하고 스트림키를 발급받은 후 해당 값을 OBS에 자동으로 설정해주는 앱

- AHK를 사용한 밴드 라이브 방송 자동 제목입력, 스트림키 발급
- obs-websocket을 이용한 OBS 설정 변경

### Requirements

- Auto Hot Key
- OBS Studio > 28.0.0
  - [obs-websocket](https://github.com/obsproject/obs-websocket) : OBS Studio 28 버전 부터 기본 포함되어있으므로 따로 설치 할 필요 x
  - `Tools > obs-websocket Settings` 에서 Enable Websocket server 체크, Server Port, Server Password 세팅
  - (e.g. 4455 / 123456)
- Python3
- [obsws-python 라이브러리 설치](https://pypi.org/project/obsws-python/)
  - `pip install obsws-python`

## Usage

1. OBS를 실행한다.
2. BandStreamSetter.ahk를 실행한다.
3. 밴드 라이브방송 시작하기 창을 띄우고 F4키를 누른다.
4. 설정 값을 확인 후 y또는 n을 누른다.
5. 설정 값이 문제가 없다면 스트림이 시작된다.
