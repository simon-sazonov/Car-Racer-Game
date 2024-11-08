🚗 Car Racer Game
Welcome to our Car Racer game! This project was developed as a final assignment for Computation III, aimed at demonstrating skills in object-oriented programming and game development using Pygame. Below you’ll find details on game features, installation instructions, and more.

📌 Project Overview
This project builds upon a basic car racing game developed during practical classes, with the addition of creative enhancements and customizations. Players can enjoy both single and multiplayer modes, with dynamic gameplay enhanced by various power-ups and an improved user interface. The game structure follows an object-oriented approach and is designed to be modular and extendable.

Notable Features
Single-Player Mode: Engage in a solo racing experience.
Multiplayer Mode: Race against a friend on the same screen!
Custom Shop: Players can select cars in single-player mode based on score credits, while in multiplayer mode, each player can independently choose their car.
Power-Ups: The game includes four unique power-ups that enhance the gameplay:
Invincibility: Temporary immunity to obstacles.
Slow Motion: Reduces the speed of incoming traffic, giving players more reaction time.
Size Reduction: Temporarily shrinks the car, making it easier to navigate.
Shooting Ability: Grants players the ability to shoot obstacles on the track.
Enhanced UI: The game interface has been customized for a smooth and engaging experience.
Instructions Panel: Includes game rules, power-up explanations, and control instructions.
Controls
Single Player / Player 1: WASD keys (with W and S adjusting car speed).
Player 2 (Multiplayer Mode): Refer to the in-game Instructions Menu for details.
🎮 Installation
Prerequisites
Ensure you have the following Python packages installed to run the game:

bash
Копировать код
pip install setuptools pip opencv-python pygame numpy wheel
Launch Instructions
Clone this repository:
bash
Копировать код
git clone https://github.com/yourusername/your-repo-name.git
Navigate to the project directory:
bash
Копировать код
cd your-repo-name
Run the game:
bash
Копировать код
python main.py
Note: This project includes audio files for an immersive experience, especially when selecting cars in the shop. Some audio clips are humorous but may be a bit loud for headphone users.

📂 Project Structure
main.py: The main script to launch the game.
assets/: Contains images, sounds, and other game assets.
src/: All core game classes, including PowerUps, Car, UI components, and game logic.
uml/: UML Class Diagram (open with SAP’s PowerDesigner software).
📜 Requirements
Please refer to requirements.txt for all dependencies, ensuring compatibility across setups.

🛠️ How to Customize
Power-Ups: Modify or add additional power-ups by extending the PowerUp abstract class in src/powerups/.
UI Improvements: Customize the UI by editing files in src/ui/.
🧑‍💻 Authors
Guilherme Pereira (20221856)
Rodrigo Azevedo Gonçalves (20222044)
Semen Sazonov (20221689)
📜 License
This project is licensed under the MIT License.

⚠️ Important Notes
UML Diagram: Use SAP PowerDesigner to view the UML class diagram, providing an overview of the game’s object-oriented structure.
GitHub Repository: We used GitHub for version control and collaboration throughout the development process.
Thank you for checking out our Car Racer game! We hope you enjoy playing it as much as we enjoyed creating it.
