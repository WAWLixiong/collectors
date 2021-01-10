import requests, os, re, time, subprocess, sys
s = requests.session()
video_format = ""


def get_video_and_audio(avurl, vid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Range': 'bytes 0-xxxxxx',
        'Referer': avurl
    }
    res = s.get(avurl, headers=headers)
    res.encoding = 'utf-8'
    data = res.text
    pat = 'window.__playinfo__=(.*?)</script><script>window.__INITIAL_STATE'
    page_json = re.compile(pat).findall(data)[0]
    page_json = eval(page_json)
    videourl = page_json["data"]["dash"]["video"]
    audio = page_json["data"]["dash"]["audio"][0]["baseUrl"]
    video = {}
    for i in videourl:
        video_dic = eval('{"' + str(i["id"]) + '": "' + str(i["baseUrl"]) + '"}')
        video.update(video_dic)
    if vid:
        return vid, video[vid], audio
    else:
        print("80 == 1080P\n64 == 720p\n32 == 480P\n16 == 360P\n可选清晰度：")
        for i in video:
            print(i)
        vid = input("请选择清晰度：")
        if vid in ["80", "64", "32", "16"]:
            return vid, video[vid], audio
        else:
            print("选择错误")
            time.sleep(20)
            sys.exit(1)


def download(avurl,video, audio, title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Range': 'bytes 0-xxxxxx',
        'Referer': avurl
    }
    r = s.get(video, stream=True, headers=headers)
    count = 0
    count_tmp = 0
    time1 = time.time()
    file = open(title + "temp.mp4", "wb")
    length = float(r.headers['content-length'])
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            file.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 1:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1
                count_tmp = count
                if 0 <= speed < (1024):
                    print("\r" + title + '   进度: ' + '{:.2f}'.format(p) + '%' + '    下载速度: ' + '{:.2f}'.format(
                        speed) + 'KB/S', end="")
                else:
                    print("\r" + title + '   进度: ' + '{:.2f}'.format(p) + '%' + '    下载速度: ' + '{:.2f}'.format(
                        speed / 1024) + 'MB/S', end="")
                time1 = time.time()
    file.close()
    r = s.get(audio, headers=headers)
    file = open(title + "temp.aac", "wb")
    file.write(r.content)
    file.close()


def mix(title):
    try:
        temp_path = sys._MEIPASS + "\\"
    except Exception as err:
        temp_path = ""
    path = temp_path + "ffmpeg.exe -i " + title + "temp.mp4 -i " + title + "temp.aac -vcodec copy -acodec copy " + os.getcwd() + "\\" + title + ".mp4"
    subprocess.call(path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.remove(title + "temp.mp4")
    os.remove(title + "temp.aac")


def down(avurl, title):
    global video_format
    video_format, video_url, audio_url = get_video_and_audio(avurl, video_format)
    download(avurl, video_url, audio_url, title)
    mix(title)
    print("\n" + title + "\n下载成功\n")


def main():
    url = input("视频地址：")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Range': 'bytes 0-xxxxxx',
        'Referer': url
    }
    r = s.get(url, headers=headers)
    r.encoding = 'utf-8'
    data = r.text
    patt = '"page":(\d*?),"from".*?"part":"(.*?)",'
    pat = 'name="keywords" content="(.*?),'
    pages = re.compile(patt, re.S).findall(data)
    tit = re.compile(pat).findall(data)[0]
    tit = re.sub(r'[\\/:：;*?"<>| ]', '', tit)
    if "视频选集" not in data:
        down(url, tit)
    else:
        choese = input("此页面存在多个视频\n全部下载输入 1 \n单一下载输入 2\n请输入：")
        if int(choese) == 1:
            print("视频列表：")
            for i in pages:
                print(i[1])
            for e in pages:
                page = e[0]
                tit = re.sub(r'[\\/:：;*?"<>| ]', '', e[1])
                down_url = url + "?p=" + str(page)
                down(down_url, tit)
        else:
            down(url, tit)
    input("\n视频已保存在程序目录，按回车可退出。")


if __name__ == '__main__':
    main()
