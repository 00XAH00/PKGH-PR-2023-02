"""add cart

Revision ID: 8ef90253a386
Revises: b47a379f2402
Create Date: 2023-02-15 01:31:26.428187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ef90253a386'
down_revision = 'b47a379f2402'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['goods.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_product_id'), 'cart', ['product_id'], unique=False)
    op.create_index(op.f('ix_cart_user_id'), 'cart', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cart_user_id'), table_name='cart')
    op.drop_index(op.f('ix_cart_product_id'), table_name='cart')
    op.drop_table('cart')
    # ### end Alembic commands ###