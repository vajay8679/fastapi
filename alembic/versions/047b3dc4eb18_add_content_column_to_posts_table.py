"""add content column to posts table

Revision ID: 047b3dc4eb18
Revises: 93f19f84a922
Create Date: 2024-06-11 00:03:55.378560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '047b3dc4eb18'
down_revision: Union[str, None] = '93f19f84a922'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
