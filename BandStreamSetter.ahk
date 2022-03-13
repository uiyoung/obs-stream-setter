SetKeyDelay, 50

F4::              

;refresh
;Send, {F5} 

;wait till page loaded
;pageLoaded := false
;while(pageLoaded = false)
;{
;	sleep 1000
;	ImageSearch, X, Y, 0, 0, A_ScreenWidth, A_ScreenHeight, *12 test2.png
;	if ErrorLevel = 0
;		pageLoaded := true
;}

;get date
FormatTime, today, , yyyy-MM-dd

;get time
if A_Hour between 7 and 9
	time = 1부
else if A_Hour between 10 and 12
	time = 2부
else 
	time = 오후 

;set title
InputBox, title, start band live, 방송 제목을 입력해 주세요., ,340, 140, , , , , %today% 주일%time%예배
if ErrorLevel
{
	MsgBox, cancelled 
	return
}

;Send, {TAB 2}
;Sleep 100

;Send, ^{A}
Send, %title%
Sleep 1000

;issue keys
Send, {TAB 4}
Sleep 1000
Send, {ENTER}
Sleep 1000

;copy stream url
Send, +{TAB 3}
Send, {ENTER}
sleep, 1000
Send, {ENTER}
stream_url := clipboard
sleep, 1000

;copy stream key
Send, {TAB 3}
Send, {ENTER}
sleep, 1000
Send, {ENTER}
stream_key := clipboard

Run python test.py %stream_url% %stream_key%

;delete existing configure file
;FileDelete, service.json

;create new configure file
;FileAppend,
;(
;{
;`t"settings": {
;`t`t"bwtest": false,
;`t`t"key": "%stream_key%",
;`t`t"server": "%stream_url%",
;`t`t"use_auth": false
;`t},
;`t"type": "rtmp_custom"
;}
;), service.json
;
;if ErrorLevel 
;	MsgBox, FileAppend error
;
;;reload obs
;Run, reload.bat
