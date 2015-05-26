from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
	gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
	gauth.Refresh()
else:
	gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

file1 = drive.CreateFile()
file1.SetContentFile('achat.txt')
file1.Upload()

file2 = drive.CreateFile()
file2.SetContentFile('depense.txt')
file2.Upload()

