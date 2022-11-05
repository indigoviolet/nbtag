from .tag_pre_save_hook import TagPreSaveHook


def _jupyter_server_extension_paths():
    return [{"module": "nbtag"}]


def _load_jupyter_server_extension(serverapp):
    serverapp.contents_manager.register_pre_save_hook(TagPreSaveHook())


load_jupyter_server_extension = _load_jupyter_server_extension
