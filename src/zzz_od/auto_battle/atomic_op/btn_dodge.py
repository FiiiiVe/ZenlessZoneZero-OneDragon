from one_dragon.base.conditional_operation.atomic_op import AtomicOp
from zzz_od.context.battle_context import BattleEventEnum
from zzz_od.context.zzz_context import ZContext


class AtomicBtnDodge(AtomicOp):

    def __init__(self, ctx: ZContext):
        AtomicOp.__init__(self, op_name=BattleEventEnum.BTN_DODGE.value)
        self.ctx: ZContext = ctx

    def execute(self):
        self.ctx.battle.dodge()

    def stop(self) -> None:
        self.ctx.controller.release_dodge()