"""WTF

Revision ID: e200df7a34a2
Revises: ce722104fe34
Create Date: 2023-02-28 19:47:22.587722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e200df7a34a2'
down_revision = 'ce722104fe34'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('code', sa.String(length=15), nullable=False))
    op.create_unique_constraint(None, 'goods', ['code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'goods', type_='unique')
    op.drop_column('goods', 'code')
    # ### end Alembic commands ###
