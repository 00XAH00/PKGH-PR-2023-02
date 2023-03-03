"""add unique for product name

Revision ID: b635dcb1dafb
Revises: 22430bb6af03
Create Date: 2023-02-27 16:45:32.897796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b635dcb1dafb'
down_revision = '22430bb6af03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'goods', ['name'])
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint(None, 'goods', type_='unique')
    # ### end Alembic commands ###