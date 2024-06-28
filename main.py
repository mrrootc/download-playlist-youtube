# from pytube import Playlist
#
# pl = Playlist(input("Lien : "))
# path = input("Le chemin: ")
# print(f"le nombre de video est de {len(pl.videos)}")
# for i,v in enumerate(pl.videos,start=1):
#     stream = v.streams.get_highest_resolution()
#     print(f"Telechargment de la video {v.title} avec {stream.resolution}")
#     print(i,'download complete',stream.download(path,filename_prefix=f"{i}_"))


from pytube import Playlist
import os

def convert_to_mp3(filepath):
    base, ext = os.path.splitext(filepath)
    new_file = base + '.mp3'
    os.rename(filepath, new_file)
    return new_file

pl = Playlist(input("Lien : "))
path = input("Le chemin: ")
print(f"Le nombre de vidéos dans la playlist est de {len(pl.videos)}")

for i, v in enumerate(pl.videos, start=1):
    try:
        stream = v.streams.filter(only_audio=True).first()
        print(f"Téléchargement de la vidéo {v.title} en audio")
        downloaded_file = stream.download(path, filename_prefix=f"{i}_")
        mp3_file = convert_to_mp3(downloaded_file)
        print(f"{i} - Téléchargement terminé : {mp3_file}")
    except Exception as e:
        print(f"Erreur lors du traitement de la vidéo {v.title}: {e}")


