import importlib
import traceback

import modular
import modules.logging
import modules.eval
import modules.mapper

importlib.reload(modular)
importlib.reload(modules.logging)
importlib.reload(modules.eval)
importlib.reload(modules.mapper)

ALIASES = {
    'sc': 'score'
}

TRIGGERS = {
    r'^You are thirsty\.$': 'drink waterskin'
}


class Kotl(modular.ModularClient):
    def __init__(self, mud, name):

        self.name = name
        self.logfname = '{}.log'.format(name)
        self.mapfname = '{}.map'.format(name)

        self.modules = {}
        mods = {
            'eval': (modules.eval.Eval, []),
            'logging': (modules.logging.Logging, [self.logfname]),
            # 'mapper': (modules.mapper.Mapper, [True, self.mapfname, True]),
        }

        for modname, module in mods.items():
            try:
                constructor, args = module
                args = [mud] + args
                self.modules[modname] = constructor(*args)
            except Exception:
                traceback.print_exc()

        super().__init__(mud)

        self.aliases.update(ALIASES)
        self.triggers.update(TRIGGERS)

    def getHostPort(self):
        return 'kotl.org', 2222


def getClass():
    return Kotl
