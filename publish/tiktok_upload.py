#!/usr/bin/env python3
"""Upload a video to TikTok as a DRAFT (inbox). Usage: python3 publish/tiktok_upload.py video.mp4
The owner gets a notification in the TikTok app and publishes it with one tap."""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(HERE, "..", ".env")
API = "https://open.tiktokapis.com/v2"

def env():
    d = {}
    for l in open(ENV).read().splitlines():
        if "=" in l and not l.startswith("#"):
            k, v = l.split("=", 1); d[k] = v
    return d

def save_refresh(token):
    lines = open(ENV).read().splitlines()
    lines = [l for l in lines if not l.startswith("TIKTOK_REFRESH_TOKEN=")] + [f"TIKTOK_REFRESH_TOKEN={token}"]
    open(ENV, "w").write("\n".join(lines) + "\n")

def post(url, data, headers):
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} from {url}: {e.read().decode()[:500]}")

def access_token(e):
    tok = post(API + "/oauth/token/", urllib.parse.urlencode({
        "client_key": e["TIKTOK_CLIENT_KEY"], "client_secret": e["TIKTOK_CLIENT_SECRET"],
        "grant_type": "refresh_token", "refresh_token": e["TIKTOK_REFRESH_TOKEN"]}).encode(),
        {"Content-Type": "application/x-www-form-urlencoded"})
    if "access_token" not in tok:
        sys.exit(f"Token refresh failed (run publish/tiktok_setup.py again): {tok}")
    if tok.get("refresh_token"):
        save_refresh(tok["refresh_token"])
    return tok["access_token"]

def main(path):
    size = os.path.getsize(path)
    if size > 64 * 1024 * 1024:
        sys.exit("Video larger than 64 MB; compress it first.")
    at = access_token(env())
    h = {"Authorization": f"Bearer {at}", "Content-Type": "application/json; charset=UTF-8"}
    init = post(API + "/post/publish/inbox/video/init/", json.dumps({"source_info": {
        "source": "FILE_UPLOAD", "video_size": size, "chunk_size": size, "total_chunk_count": 1}}).encode(), h)
    if init.get("error", {}).get("code") not in (None, "ok"):
        sys.exit(f"Init failed: {init}")
    pid, up = init["data"]["publish_id"], init["data"]["upload_url"]
    req = urllib.request.Request(up, data=open(path, "rb").read(), method="PUT", headers={
        "Content-Type": "video/mp4", "Content-Length": str(size),
        "Content-Range": f"bytes 0-{size-1}/{size}"})
    urllib.request.urlopen(req)
    for _ in range(30):
        st = post(API + "/post/publish/status/fetch/", json.dumps({"publish_id": pid}).encode(), h)
        s = st.get("data", {}).get("status")
        if s in ("SEND_TO_USER_INBOX", "PUBLISH_COMPLETE"):
            print(f"OK: draft sent to TikTok inbox (publish_id {pid})"); return
        if s == "FAILED":
            sys.exit(f"Upload failed: {st}")
        time.sleep(5)
    print(f"Uploaded, status still processing (publish_id {pid}); check the TikTok app.")

if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
