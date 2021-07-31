# twwh2_krp
토탈 워: 워해머 2의 한글 번역을 본인이 원하는 대로 바꿔보세요! 현재 유닛명과 일부 단어를 지원합니다.

## 사용법
1. release에서 twwh2krp.exe를 다운로드 받거나, twwh2.py를 직접 실행하세요.
2. main.tsv 파일과 dict.tsv 파일을 준비해주세요. dict.tsv 파일은 [여기](https://docs.google.com/spreadsheets/d/1Jan_f9J5izT27GXfwrXK7huSx4dL1oAQaFUHU5ibe80/edit#gid=819329062, "구글 스프레드시트") 있는
구글 스프레드시트 파일의 사본을 생성하여 편집할 수도 있습니다.
(release에 있는 dict 파일은 현재 한국어 번역 명칭을 사용중입니다)
4. 같은 폴더에 main.tsv, dict.tsv라는 이름으로 파일이 존재하면 자동으로 변환을 수행합니다. 그렇지 않다면 직접 파일을 불러와주면 됩니다.
5. 완성된 exported.tsv 파일을 엑셀 등으로 엽니다.
6. rpfm으로 새로운 pack 파일을 만들어서, 해당 pack 파일 안에 text 폴더를 만든 후, text 폴더에 자신이원하는이름.loc 파일을 생성합니다.
7. 엑셀에서 1행을 제외한 모든 데이터를 복사합니다. 
8. rpfm의 loc 파일에서 Paste as New Row를 실행합니다. (Ctrl+Shift+V)
