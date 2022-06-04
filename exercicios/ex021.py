# abrir e reproduzir um arquivo .mp3

import vlc

p = vlc.MediaPlayer(str(input('Cole o caminho para a música: ')))
p.play()
