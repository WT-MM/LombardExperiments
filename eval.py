import string
import torch
import librosa
from speechbrain.pretrained import EncoderDecoderASR
import glob
from jiwer import wer

sbmodel = EncoderDecoderASR.from_hparams(
             source="speechbrain/asr-crdnn-rnnlm-librispeech",savedir="pretrained_models/EncoderDecoderASR"
        )
def sb(file):
    data, rate = librosa.load(file, sr=16000)  
    data_tensor = torch.tensor(data)
    data_tensor = sbmodel.audio_normalizer(data_tensor, 16000)
    batch = data_tensor.unsqueeze(0)
    rel_length = torch.tensor([1.0])
    predicted_words, predicted_tokens = sbmodel.transcribe_batch(
        batch, rel_length
    )
    return predicted_words[0]

results = {}

#Struct is text_environ_num.wav 
for wave_file in glob.glob("testData/audio/*.wav"):
    meta = wave_file.split("_")
    text = sb(wave_file)
    gt = ""
    with open(f"testData/text/{meta[0]}.txt") as f:
        gt = f.read()
    error = wer(gt, text)
    results[wave_file] = [error, text]
    pass

with open("results.csv", "w") as f:    
    for (k, v) in results.items():
        f.write(k + "," + v[0] + "," + v[1] + "\n")