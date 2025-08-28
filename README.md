# 🪨📄✂️ Rock-Paper-Scissors on Cartesi (Python DApp)

This is a decentralized **Rock-Paper-Scissors** game built using **Cartesi Rollups** and a **Python backend**.  
It demonstrates how classic games can be implemented as **trustless decentralized applications (dApps)** while leveraging the **Cartesi Machine** for off-chain computation.

---

## 🔎 What is Cartesi?

[Cartesi](https://cartesi.io/) is a **Layer-2 platform** that brings **Linux and mainstream software stacks** to blockchain.  
It allows developers to build **scalable dApps** using familiar tools (like Python, C++, TensorFlow, etc.) instead of being limited to smart contracts in Solidity.  

Key features:
- **Scalability** – Heavy computation happens off-chain inside the Cartesi Machine.  
- **Familiar Languages** – Build dApps using Python or other languages instead of Solidity.  
- **Decentralization** – Results are anchored on the blockchain, ensuring security and fairness.  

---

## 🎮 About the Game

- Two players commit their moves (Rock, Paper, or Scissors).  
- Each move is hashed and submitted to the Cartesi rollup (to prevent cheating).  
- Once both moves are revealed, the Python backend running inside Cartesi verifies the results.  
- The outcome is sent back and recorded on the blockchain, ensuring a **trustless and transparent** game.  

---

## ⚙️ Tech Stack

- **Backend**: Python (game logic + Cartesi rollups handler)  
- **Blockchain Layer**: Cartesi Rollups (anchored to Ethereum or compatible L2s)  
- **Frontend** *(optional)*: Can be extended with React/Streamlit or CLI commands  
- **Docker**: Used to package the Cartesi DApp environment  

---

## 🚀 How It Works

1. **Player Registration** → Players join a new game instance.  
2. **Move Commit** → Each player submits a hashed move (e.g., `hash("rock"+secret)`).  
3. **Move Reveal** → Players reveal their actual move + secret.  
4. **Validation in Python** → The backend verifies fairness and decides the winner.  
5. **Blockchain Anchoring** → The result is finalized and posted to the blockchain.  

---

# Refernce Git
https://github.com/Mugen-Builders

## 🛠️ Installation & Setup

### 1. Clone the Repository
```wsl 
git clone https://github.com/SurweeshSP/Stone-Paper-Scrissor-Cartesi.git
cd Stone-Paper-Scrissor-Cartesi

cartesi build
cartesi run

yarn start input send --payload '{"method":"create_challenge"}' from the frontEnd Consolge which is optional !!!
