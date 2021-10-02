import re

# word, data = "blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
word, data = "Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
def solution(word,page):
    answer = 0
    pages = dict()
    for p in page:
        parsePage(pages, p, word)
    for p in pages.values():
        for a in p.get("a"):
            if pages.get(a):
                pages[a]["total_score"] += p["link_score"]
    max_v = 0
    for idx, dic in enumerate(pages.values()):
        if dic["total_score"] > max_v:
            max_v = dic["total_score"]
            answer = idx
    return answer

def matchWord(word, targetWord):
    answer = 0
    if len(word) < len(targetWord):
        return answer
    for i in range(len(word)-len(targetWord)+1):
        if word[i:i+len(targetWord)].lower() == targetWord.lower():
            prev = ord(word[i-1].lower()) if i != 0 else 0
            nxt = ord(word[i+len(targetWord)].lower()) if i != len(word)-len(targetWord) else 0
            # if i == 0 and 97 <= nxt <= 122:
            #     continue
            # elif i == len(word)-len(targetWord)-1 and 97 <= prev <= 122:
            #     continue
            if 97 <= prev <= 122 or 97 <= nxt <= 122:
                continue
            answer += 1
    return answer

def parsePage(pages, html, word):
    html = html.replace("\n", " ")
    html = html.replace(">", " ")
    html = html.split(" ")
    url, data = None, dict()
    data["total_score"], data["def_score"], data["a"], data["link_score"] = 0, 0, list(), 0
    for idx, w in enumerate(html):
        data["def_score"] += matchWord(w, word)
        if "<a" in w and "href" == html[idx+1][:4]:
            attr = html[idx+1].split("\"")
            data["a"].append(attr[1])
            data["link_score"] += 1
        if w == "<meta":
            for nxt in range(idx+1, len(html)):
                if "content=" in html[nxt]:
                    attr = html[nxt].split("\"")
                    url = attr[1]
                    break
    data["link_score"] = 0 if len(data["a"]) == 0 else data["def_score"] / len(data["a"])
    data["total_score"] = data["def_score"]
    pages[url] = data
    return pages


print(solution(word, data))
print(ord("a"), ord("z"))