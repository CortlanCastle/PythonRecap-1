import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")
# You have to install a library to make this work. # Create a virtual environment every new project and copy libraries into it
# step 1 - Create a virtual environment- (do in terminal down below) - PC's use "py" MAC use "python3"--- EX: py -3 -m venv myvenv (myvenv is the name)
# step 2 - Activate your venv. .\myvenv\Scripts\activate
# Step 3 - Install 3rd party library/modeule - pip3 install matplotlib (matplotlib is name of library)git confi