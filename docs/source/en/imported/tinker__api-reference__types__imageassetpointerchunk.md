# tinker.types.ImageAssetPointerChunk

## *class* [**tinker.types.ImageAssetPointerChunk**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/image_asset_pointer_chunk.py\#L8)(*StrictBase*)[​](\#class-tinkertypesimageassetpointerchunkstrictbase)

**Fields:**

- **format**
  
  – Image format
- **location**
  
  – Path or URL to the image asset
- **expected_tokens**
  
  – Expected number of tokens this image represents. This is only advisory: the tinker backend will compute the number of tokens from the image, and we can fail requests quickly if the tokens does not match expected_tokens.
- **type**
