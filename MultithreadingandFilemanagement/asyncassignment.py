import asyncio
import aiofiles
import os
async def read_file(path):
     async with aiofiles.open(path,'r') as f:
         print("Reading File")
         content=await f.read()
     await asyncio.sleep(2)
     return content

async def write_file(fname,content):
    root="C:/Users/gokulakrishna.ravich/Downloads/DownloadedFiles"
    path=os.path.join(root,fname)
    async with aiofiles.open(path,'w') as f:
        print("Writing File")
        await f.write(content)
    await asyncio.sleep(1)
async def main():
    c1,c2=await asyncio.gather(
    read_file('C:/Users/gokulakrishna.ravich/IMPIGERTRAINING/athlete_events.csv'),
    read_file("C:/Users/gokulakrishna.ravich/IMPIGERTRAINING/car_price_dataset.csv")
    )
    await asyncio.gather(
        write_file("async1.txt",c1),
        write_file("async2.txt",c2)
    )
asyncio.run(main())