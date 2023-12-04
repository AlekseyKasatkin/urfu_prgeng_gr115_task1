import pyaudio
import wave
from pydub import AudioSegment

# Установка параметров записи
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILE = "output.mp3"

# Инициализация PyAudio
audio = pyaudio.PyAudio()

# Открытие потока для записи звука с микрофона
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Запись началась...")

# Создание списка для хранения фреймов звука
frames = []

# Запись звука во время указанной продолжительности
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Запись завершена.")

# Остановка потока записи
stream.stop_stream()
stream.close()
audio.terminate()

# Сохранение записанного звука в WAV файл
wave_file = wave.open("output.wav", "wb")
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()

# Конвертация WAV файла в MP3
sound = AudioSegment.from_wav("output.wav")
sound.export(OUTPUT_FILE, format="mp3")

print("Запись сохранена в файл:", OUTPUT_FILE)
