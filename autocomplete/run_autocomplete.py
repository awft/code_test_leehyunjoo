from autocomplete import AutoComplete

if __name__ == "__main__":
    auto_complete = AutoComplete()
    sentence = """나는 네가 정말 싫었다.
                너를 다시 만나기 전까진…
                따분한 게 질색인 아이, 이시다 쇼야. 
                간디가 어떤 사람인지, 인류의 진화과정 이라든지, 알게뭐람. 
                어느 날 쇼야의 따분함을 앗아갈 전학생이 나타났다. 니시미야 쇼코. 그 아이는 귀가 들리지 않는다고 한다. 
                쇼야의 짓궂은 장난에도 늘, 생글생글 웃고만 있다. 짜증난다. 
                그의 괴롭힘에 쇼코는 결국 전학을 갔고, 이시다 쇼야는 외톨이가 되었다. 
                
                6년 후, 더 이상 이렇게 살아봐야 의미가 없음을 느낀 쇼야는 마지막으로 쇼코를 찾아간다. 
                처음으로 전해진 두 사람의 목소리. 두 사람의 만남이 교실을, 학교를, 
                그리고 쇼야의 인생, 쇼코의 인생을 바꾸기 시작한다.
                
                소년 그리고 소녀. 실타래처럼 뒤엉켜가는 청춘의 이야기."""

    print("검색어: ㅅㄴ / 검색결과: ", auto_complete.find_keyword(sentence=sentence, keyword="ㅅㄴ"))
    print("검색어: ㅁ / 검색결과: ", auto_complete.find_keyword(sentence=sentence, keyword="ㅁ"))
    print("검색어: 목소 / 검색결과: ", auto_complete.find_keyword(sentence=sentence, keyword="목소"))
    print("검색어: 굣 / 검색결과: ", auto_complete.find_keyword(sentence=sentence, keyword="굣"))




