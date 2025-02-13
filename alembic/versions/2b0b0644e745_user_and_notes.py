"""User and Notes

Revision ID: 2b0b0644e745
Revises: d1dfe335984a
Create Date: 2025-02-13 13:02:26.577613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b0b0644e745'
down_revision: Union[str, None] = 'd1dfe335984a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
