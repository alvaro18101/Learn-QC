from qiskit.visualization import array_to_latex
from qiskit.quantum_info import Statevector 
import numpy as np

Ket_3_qubits = Statevector([0, 1, 1, 0, 1, 0, 0, 0]/np.sqrt(3))
Ket_3_qubits.draw('Latex')

probs_3_qubits = Ket_3_qubits.probabilities()
print('probs: {}'.format(probs_3_qubits))

probs_Ket_3_qubits = Ket_3_qubits.probabilities_dict([1])
print('probs: {}'.format(probs_Ket_3_qubits))