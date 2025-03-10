import flet as ft


def main(page: ft.Page):

    songs = [
        "/Users/julesarrioja/PycharmProjects/PythonBBC/Milo j - M.A.I (Letra).mp3",
        "/Users/julesarrioja/PycharmProjects/PythonBBC/KHEA - CómoleDigo.mp3",
        "/Users/julesarrioja/PycharmProjects/PythonBBC/Mora - QUE HABILIDAD (letraLyrics).mp3",
        "/Users/julesarrioja/PycharmProjects/PythonBBC/Jhayco - Tokyo (Audio).mp3",
        "/Users/julesarrioja/PycharmProjects/PythonBBC/Trueno - FEEL ME__ (Video Oficial).mp3"
    ]

    state = {"current_index": 0, "is_paused": False}
    audio_player = ft.Audio(src=songs[state["current_index"]])
    page.overlay.append(audio_player)


    def play_audio(e):
        if state["is_paused"]:
            audio_player.resume()
        else:
            audio_player.play()
        state["is_paused"] = False


    def pause_audio(e):
        audio_player.pause()
        state["is_paused"] = True


    def next_song(e):
        if songs[state["current_index"]:]:
            state["current_index"] += 1
            audio_player.src = songs[state["current_index"]]
            page.update()
            audio_player.play()
            state["is_paused"] = False


    def prev_song(e):
        if state["current_index"] > 0:
            state["current_index"] -= 1
            audio_player.src = songs[state["current_index"]]
            page.update()
            audio_player.play()
            state["is_paused"] = False


    prev_button = ft.ElevatedButton(text="Previous", on_click=prev_song)
    play_button = ft.ElevatedButton(text="Play", on_click=play_audio)
    pause_button = ft.ElevatedButton(text="Pause", on_click=pause_audio)
    next_button = ft.ElevatedButton(text="Next", on_click=next_song)


    page.add(prev_button, play_button, pause_button, next_button)


ft.app(target=main)
#Par de videos de youtube, se me olvido como programar
#Ponga cosas mas faciles pa la proxima pls