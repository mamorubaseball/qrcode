import gspread
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

class Google_API():
    def __init__(self):
        # 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
        self.scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        # 認証情報設定
        # ダウンロードしたjsonフit()ァイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('molten-castle-350522-85dbb509eab0.json', self.scope)
        # OAuth2の資格情報を使用してGoogle APIにログインします。
        self.gc = gspread.authorize(self.credentials)

        # 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
        self.SPREADSHEET_KEY = '1CfY1wY7FN72neY8qh_3xhOi8_lxvjmr_AcalT79_jKE'
  
        self.meibo_sheet = self.gc.open_by_key(self.SPREADSHEET_KEY).worksheet('名簿')
        self.attend_sheeet = self.gc.open_by_key(self.SPREADSHEET_KEY).worksheet('出席者リスト')

    def add(self,user_id):
        if self.attend_sheeet.find(user_id):
            pass
        else:
            row_lists  = self.meibo_sheet.row_values(int(user_id)+1)
            name = row_lists[1]
            self.attend_sheeet.append_row([user_id,name])


        