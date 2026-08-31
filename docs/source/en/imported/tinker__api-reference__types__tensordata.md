# tinker.types.TensorData

## *class* [**tinker.types.TensorData**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/tensor_data.py\#L25)(**)[​](\#class-tinkertypestensordata)

**Fields:**

- **dtype**
- **shape**
  
  – Optional.

The shape of the tensor (see PyTorch tensor.shape). The shape of a one-dimensional list of length N is `(N,)`. Can usually be inferred if not provided, and is generally inferred as a 1D tensor. - **sparse_crow_indices** – Optional CSR compressed row pointers. When set, this tensor is sparse CSR: - data contains only the non-zero values (flattened) - sparse_crow_indices contains the row pointers (length = nrows + 1) - sparse_col_indices contains the column indices (length = nnz) - shape is required and specifies the dense shape - **sparse_col_indices** – Optional CSR column indices. Must be set together with sparse_crow_indices.

### *property* [**data**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/tensor_data.py\#L82)[​](\#property-data)

Flattened tensor data as array of numbers.

**Returns:** `Union[List[int], List[float]]`

### [**from_torch_sparse**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/tensor_data.py\#L104)(*tensor*)[​](\#from_torch_sparsetensor)

Create a sparse CSR TensorData from a dense 2-D torch tensor.

Automatically detects sparsity and encodes as CSR when it saves space. Falls back to dense if the tensor is 1-D or mostly non-zero.

**Returns:** `TensorData`

### [**to_numpy**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/tensor_data.py\#L134)()[​](\#to_numpy)

Convert TensorData to numpy array.

**Returns:** `npt.NDArray[Any]`

### [**to_torch**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/tensor_data.py\#L140)()[​](\#to_torch)

Convert TensorData to torch tensor.

**Returns:** `torch.Tensor`
