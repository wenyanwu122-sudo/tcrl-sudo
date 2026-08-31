# tinker.types.ImageChunk

## *class* [**tinker.types.ImageChunk**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/image_chunk.py\#L12)(*StrictBase*)[​](\#class-tinkertypesimagechunkstrictbase)

**Fields:**

- **data**
  
  – Image data as bytes
- **format**
  
  – Image format
- **expected_tokens**
  
  – Expected number of tokens this image represents. This is only advisory: the tinker backend will compute the number of tokens from the image, and we can fail requests quickly if the tokens does not match expected_tokens.
- **type**

### [**validate_data**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/image_chunk.py\#L29)(*value*)[​](\#validate_datavalue)

Deserialize base64 string to bytes if needed.

**Returns:** `bytes`

### [**serialize_data**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/image_chunk.py\#L36)(*value*)[​](\#serialize_datavalue)

Serialize bytes to base64 string for JSON.

**Returns:** `str`
