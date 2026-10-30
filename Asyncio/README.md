
## My understanding on asyncio

 - Synchronous : Runs one line at a time. If u call an API , the program waits until response comes back.
          example : U put water to boil. Once boiled , then chop vegetable.
 - async : Let u pause at waiting points and switch to other task, when response arrives it resumes.
          example : U put water to boil, then chop vegetable while waiting.


  # Building blocks

    - async : coroutine is a special type of function that can be paused or resumed
    - await : to await coroutine
    - asyncio.run - entry point

    - gather : Starts all task together and wait for all to finish .
          example : u order 3 pizza. Waiter waits till all 3 pizza is ready and then delivers u
    - create_ task : Dispatch each task independantly.
          example : u order 3 pizza . need not wait for all 3 . can eat as soon as one arrives
    
  
 - Reference video : https://www.bing.com/videos/riverview/relatedvideo?q=async+%2c+await+and+httpx+in+python&&mid=6D6E10D7E3E92FC6EAF36D6E10D7E3E92FC6EAF3&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCUdxvls7wrN6_FRvYe9F3RA&FORM=VRDGAR
 - reference GitHub :NA