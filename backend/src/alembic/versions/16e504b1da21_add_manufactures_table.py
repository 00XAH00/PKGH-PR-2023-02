"""add manufactures table

Revision ID: 16e504b1da21
Revises: 417f13102588
Create Date: 2023-02-28 17:23:29.800977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16e504b1da21'
down_revision = '417f13102588'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manufactures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manufactures')
    # ### end Alembic commands ###