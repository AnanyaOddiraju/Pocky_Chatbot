def chunk_text(
        text : str,
        chunk_size : int =1000,
        chunk_overlap: int =200,  #takes chunk_size - chunk_overlap to create chunks ex: text = abcdefghijklm size = 4, overlap = 2 , chunks = [abcd, cdef, efgh, ghij, ijkl, klm]
) -> list[str]:

     if not text.strip():
          return []
     chunks = []

     start = 0
     text_length = len(text)
     while start < text_length:
          end = min(start + chunk_size, text_length)
          chunk = text[start:end]
          if chunk.strip():
            chunks.append(chunk.strip())
          start += chunk_size - chunk_overlap
     return chunks

def chunk_document(
        document : dict,
        chunk_size : int =1000,
        chunk_overlap: int =200,  #takes chunk_size - chunk_overlap to create chunks ex: text = abcdefghijklm size = 4, overlap = 2 , chunks = [abcd, cdef, efgh, ghij, ijkl, klm]
) -> list[dict]:
     
     text = document["text"]
     if not text.strip():
               return [] 
         
     chunks = []
     start=0
     text_length = len(text)
     while start < text_length:
          end = min(start + chunk_size, text_length)
          chunk_text= text[start:end].strip()
          if chunk_text:
            chunks.append({"document" : document["source"], "text": chunk_text, "page": document["page"]})
          start += chunk_size - chunk_overlap
     return chunks