from libcpp cimport bool



cdef extern from "freeciv/common/game.h":
    struct civ_game:
        char *ruleset_summary
        pass
    void game_init(bool keep_ruleset_value)
    void game_reset()

def foo():
    return game_reset()
