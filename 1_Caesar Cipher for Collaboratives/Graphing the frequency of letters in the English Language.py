import matplotlib.pyplot as plt

# Function to add centered value labels
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')  # Aligning text at center



letters = ["E","T","A","O","I","N","S","R","H","D",
           "L","U","C","M","F","Y","W","G","B","V",
           "K","X","Q","J","Z"]

frequencies = [12.02,9.10,8.12,7.68,7.31,6.95,6.28,6.02,5.92,4.32,
               3.98,2.88,2.71,2.61,2.30,2.11,2.09,2.03,1.49,1.11,
               0.69,0.17,0.11,0.10,0.07]

plt.bar(letters, frequencies)

# Adding value labels
add_labels(letters, frequencies)

plt.title("Letter Frequency in English")
plt.xlabel("Letters")
plt.ylabel("Frequency (%)")

plt.show()