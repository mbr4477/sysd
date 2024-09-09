# pyright: reportUnusedExpression=false
import sysd.sysml.state_machine as stm
from sysd.core import FontBook
from sysd.dsl import (
    align_center,
    align_middle,
    end_sysd,
    hstack,
    stack,
    start_sysd,
)

FontBook.init()
FontBook.default().default_family = "Arial"

start_sysd("sm Test")
start = stm.initial_state()
state_opened = stm.state("Opened")
state_closed = stm.state("Closed")
state_locked = stm.state("Locked")
start.bounds.origin.x = 20
start.bounds.origin.y = 20
hstack(start, state_opened, state_closed, gutter=50.0)
align_middle(start, state_opened, state_closed)
stack(state_closed, state_locked, gutter=50.0)
align_center(state_closed, state_locked)

start - stm.Transition(1, 3) > state_opened
state_opened - stm.Transition(1, 3) > state_closed
state_closed - stm.Transition(2, 0) > state_locked
state_locked - stm.Transition(5, 6) > state_closed
state_closed - stm.Transition(7, 6) > state_opened
end_sysd()
