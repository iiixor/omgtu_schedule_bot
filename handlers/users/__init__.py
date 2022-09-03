from .command_start import dp
from .command_menu import dp
from .command_info import dp
from .command_support import dp
from .personal_cabinet import dp
from .support_button import dp
from .raspisanie import dp
from .prepod_info import dp
from .subscribe import dp
from .unknown_msg import dp


# тут так скажем подключаем все хэндлеры, которые мы прописали в этой дир-и
# важно задать порядок выполнения, потому что хэндлеры всегда выполняются
# сверху-вниз
__all__ = ["dp"]
