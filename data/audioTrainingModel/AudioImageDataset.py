import torchaudio
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os

class AudioImageDataset(Dataset):
    def __init__(self, audio_dir, image_dir, transform=None):
        self.audio_dir = audio_dir
        self.image_dir = image_dir
        self.transform = transform
        self.audio_files = os.listdir(audio_dir)
        self.image_files = os.listdir(image_dir)

    def __len__(self):
        return len(self.audio_files)

    def __getitem__(self, idx):
        audio_path = os.path.join(self.audio_dir, self.audio_files[idx])
        image_path = os.path.join(self.image_dir, self.image_files[idx])

        waveform, sample_rate = torchaudio.load(audio_path)
        mel_spectrogram = torchaudio.transforms.MelSpectrogram()(waveform)

        image = Image.open(image_path).convert("RGB")
        if self.transform:
            image = self.transform(image)

        return mel_spectrogram, image

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

dataset = AudioImageDataset(audio_dir='path/to/audio', image_dir='path/to/images', transform=transform)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)