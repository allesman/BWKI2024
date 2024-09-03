import torch.optim as optim
import torch.nn.functional as F

optimizer = optim.Adam(model.parameters(), lr=1e-4)
criterion = nn.MSELoss()

num_epochs = 10
for epoch in range(num_epochs):
    for mel_spectrogram, image in dataloader:
        optimizer.zero_grad()
        output = model(mel_spectrogram)
        loss = criterion(output, image)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")