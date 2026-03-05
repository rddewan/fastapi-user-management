"""merge head

Revision ID: 52a9d9b20349
Revises: a0ef8b6a2dfe, bb4cfdae4f6a
Create Date: 2026-03-04 07:50:13.555952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52a9d9b20349'
down_revision: Union[str, Sequence[str], None] = ('a0ef8b6a2dfe', 'bb4cfdae4f6a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
