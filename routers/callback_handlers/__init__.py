from aiogram import Router

from .norse_mythology_kb_callback_handler import router as kb_north_mythology_cb_router
from .runes_callback_handler import router as runes_kb_callback_handlers_router
from .worlds_callback_handler import router as worlds_kb_callback_handlers_router
from .stories_callback_handler import router as stories_cb_handlers_router
from .gods_callback_handler import router as gods_cb_handlers_router
from .symbolism_callback_handler import router as symbolism_kb_callback_handlers_router

router = Router(name=__name__)

router.include_routers(
    kb_north_mythology_cb_router,
    runes_kb_callback_handlers_router,
    worlds_kb_callback_handlers_router,
    stories_cb_handlers_router,
    gods_cb_handlers_router,
    symbolism_kb_callback_handlers_router
)
