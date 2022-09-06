from .command_start import dp
from .command_menu import dp
from .command_info import dp
from .command_support import dp
from .personal_cabinet import dp
from .support_button import dp
from .schedule import dp
from .teacher_info import dp
from .unviversity_map import dp
from .subscribe import dp
from .unknown_msg import dp


# тут так скажем подключаем все хэндлеры, которые мы прописали в этой дир-и
# важно задать порядок выполнения, потому что хэндлеры всегда выполняются
# сверху-вниз
__all__ = ["dp"]
