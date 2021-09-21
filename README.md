# Synology_SharedLink_Migration
Migrate Synology Shared Link : for DSM5.2, DSM6.0, DSM6.2
<br/>
시놀로지 NAS의 "공유 링크"기능을 통해 생성된 링크가 깨지지 않도록 유지하며 다른 웹서버나 다른 버전의 DSM으로 마이그레이션 하는 것을 도와줍니다.
<br/><br/><br/><br/>


* 현재 개발이 진행중입니다. 
* 현재 진행 상황은, 링크ID 지정자와 파일의 경로를 매칭해주는 Sqlite 데이터베이스 파일의 위치를 찾았고 DB Browser for SQLite프로그램으로 DB를 읽어 csv 추출에 성공했습니다.
* 파이썬을 이용하여 CSV 또는 데이터베이스 파일을 파싱, 이후 각각의 공유 링크에 대한 html파일을 생성하는 것이 최종 목표입니다.
* 어느 정도 정리가 되는대로 이곳에 릴리즈 후 사용 방법을 업데이트 하겠습니다.
* 이 프로그램은 IM-Holic서버 유지/보수용으로 작성되었습니다.
