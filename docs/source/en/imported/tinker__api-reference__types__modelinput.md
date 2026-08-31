# tinker.types.ModelInput

## *class* [**tinker.types.ModelInput**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L8)(*StrictBase*)[​](\#class-tinkertypesmodelinputstrictbase)

**Fields:**

- **chunks**
  
  – Sequence of input chunks (formerly TokenSequence)

### [**from_ints**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L13)(*tokens*)[​](\#from_intstokens)

Create a ModelInput from a list of ints (tokens).

**Returns:** `'ModelInput'`

### [**to_ints**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L19)()[​](\#to_ints)

Convert the ModelInput to a list of ints (tokens) Throws exception if there are any non-token chunks

**Returns:** `List[int]`

### *property* [**length**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L31)[​](\#property-length)

Return the total context length used by this ModelInput.

**Returns:** `int`

### [**empty**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L38)()[​](\#empty)

Create an empty ModelInput.

**Returns:** `'ModelInput'`

### [**append**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L44)(*chunk*)[​](\#appendchunk)

Add a new chunk, return a new ModelInput.

**Returns:** `'ModelInput'`

### [**append_int**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/model_input.py\#L50)(*token*)[​](\#append_inttoken)

Add a new token, return a new ModelInput.

**Returns:** `'ModelInput'`
