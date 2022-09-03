from .command_start import dp
from .command_menu import dp
from .command_info import dp
from .command_support import dp
from .personal_cabinet import dp
from .support_button import dp
from .raspisanie import dp
from .prepod_info import dp
from .subscribe import dp
#from .get_zodiacs import dp
#from .get_pifagor_square import dp
# from .get_zodiacs import dp
# from .get_skill import dp
# from .testing import dp
# from .info import dp
# from .portfolio import dp
# from .link import dp
# from .switch_language import dp
# from .review import dp
# from .price import dp
from .unknown_msg import dp


# тут так скажем подключаем все хэндлеры, которые мы прописали в этой дир-и
# важно задать порядок выполнения, потому что хэндлеры всегда выполняются
# сверху-вниз
__all__ = ["dp"]
