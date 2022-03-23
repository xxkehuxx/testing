from yandex_music import Client

client = Client('token').init()
client.users_likes_tracks()[0].fetch_track().download('example.mp3')