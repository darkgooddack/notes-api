"""autoincrement

Revision ID: ababe6ab4101
Revises: 07785d226753
Create Date: 2025-02-16 14:31:36.413063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ababe6ab4101'
down_revision: Union[str, None] = '07785d226753'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
