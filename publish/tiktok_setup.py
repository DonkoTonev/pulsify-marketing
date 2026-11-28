#!/usr/bin/env python3
"""One-time TikTok login. Asks for the app keys, prints a login link, saves tokens to ../.env.
Secrets are typed here in the terminal, never sent anywhere else."""
import getpass, json, os, secrets, sys, urllib.parse, urllib.request

ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
REDIRECT = "https://github.com/DonkoTonev/pulsify-marketing"

def set_env(updates):
    lines = open(ENV).read().splitlines() if os.path.exists(ENV) else []
    keep = [l for l in lines if l.split("=", 1)[0] not in updates]
    keep += [f"{k}={v}" for k, v in updates.items()]
    open(ENV, "w").write("\n".join(keep) + "\n")
    os.chmod(ENV, 0o600)

key = input("TikTok Client key: ").strip()
secret = input("TikTok Client secret (hidden): ").strip()
state = secrets.token_hex(8)
url = "https://www.tiktok.com/v2/auth/authorize/?" + urllib.parse.urlencode({
    "client_key": key, "scope": "user.info.basic,video.upload",
    "response_type": "code", "redirect_uri": REDIRECT, "state": state})
print("\n1) Open this link in a browser where you are logged in as @pulsify8 and press Authorize:\n")
print(url)
back = input("\n2) You will land on the GitHub page. Paste the FULL address from the browser bar here:\n> ").strip()
q = urllib.parse.parse_qs(urllib.parse.urlparse(back).query)
if q.get("state", [""])[0] != state or "code" not in q:
    sys.exit("No valid code in that address. Run the script again.")
data = urllib.parse.urlencode({"client_key": key, "client_secret": secret, "code": q["code"][0],
    "grant_type": "authorization_code", "redirect_uri": REDIRECT}).encode()
req = urllib.request.Request("https://open.tiktokapis.com/v2/oauth/token/", data=data,
    headers={"Content-Type": "application/x-www-form-urlencoded"})
tok = json.load(urllib.request.urlopen(req))
if "access_token" not in tok:
    sys.exit(f"TikTok refused: {tok}")
set_env({"TIKTOK_CLIENT_KEY": key, "TIKTOK_CLIENT_SECRET": secret,
         "TIKTOK_REFRESH_TOKEN": tok["refresh_token"], "TIKTOK_OPEN_ID": tok.get("open_id", "")})
print("\nOK: TikTok connected. Tokens saved in .env (refresh token valid about 1 year).")
