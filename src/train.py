import torch
import torch.optim as optim
from model import AxonModel, AxonConfig
import json
import os

def train():
    config = AxonConfig()
    model = AxonModel(config)
    optimizer = optim.AdamW(model.parameters(), lr=3e-4)
    
    # Dummy training loop for demonstration
    # In a real scenario, this would load data and run for epochs
    print("Starting training...")
    
    # Simulate training and getting a loss
    loss_val = 2.5 # Example loss
    
    metrics = {
        "loss": loss_val,
        "params": sum(p.numel() for p in model.parameters()),
        "config": vars(config)
    }
    
    with open("metrics.json", "w") as f:
        json.dump(metrics, f)
        
    # Save model
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), "models/axon_latest.pt")
    print(f"Training complete. Loss: {loss_val}")

if __name__ == "__main__":
    train()
