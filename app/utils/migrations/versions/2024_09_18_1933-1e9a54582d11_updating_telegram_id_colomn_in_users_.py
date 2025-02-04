"""Updating telegram_id colomn in users table

Revision ID: 1e9a54582d11
Revises: a71b259b46ba
Create Date: 2024-09-18 19:33:27.763954

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1e9a54582d11"
down_revision: Union[str, None] = "a71b259b46ba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "telegram_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "telegram_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###
