SetKeyDelay, 50

F4::       
WinGetActiveTitle, winTitle
WinMove, %winTitle%,, 1240, 0, 690, 1087
Sleep 100
MouseClick, left, 357, 470, 3

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

Send, %title%
Sleep 100

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

;run python script to set obs stream settings
Run python ObsStreamSetter.py %stream_url% %stream_key%