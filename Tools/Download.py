import pyrogram 
from translation import Translation
import time
from Tools.progress import progress_for_pyrogram
#Download the media

async def download(c, m):
   send = await c.send_message(chat_id=m.chat.id,
                          text=Translation.DOWNLOAD_START,
                          reply_to_message_id=m.message_id)


   download_location = Config.DOWNLOAD_LOCATION + "/"                                                               
   time = time.time()
   media_location = await c.download_media(
                          message=m.reply_to_message,
                          file_name=download_location,
                          progress=progress_for_pyrogram,
                          progress_args=(
                               "Download Status:",
                               send,
                               time
                          )
                    )
   if not media_location is None:
            await send.edit(Translation.DOWNLOAD_COMPLETE)
            logger.info(media_location)

            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(media_location))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = await take_screen_shot(
                    the_real_download_location,
                    os.path.dirname(the_real_download_location),
                    random.randint(
                        0,
                        duration - 1
                    )
                )
            logger.info(thumb_image_path)            metadata = extractMetadata(createParser(thumb_image_path))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
            Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
            img = Image.open(thumb_image_path)
            img.resize((90, height))
            img.save(thumb_image_path, "JPEG")
            c_time = time.time()