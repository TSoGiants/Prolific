"""empty message

Revision ID: fb80f39acb62
Revises: 5716bb9fc7d8
Create Date: 2021-01-02 21:45:46.054577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb80f39acb62'
down_revision = '5716bb9fc7d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clients', sa.Column('GUpassword', sa.Text(), nullable=True))
    op.add_column('food_pantries', sa.Column('FPpassword', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('food_pantries', 'FPpassword')
    op.drop_column('clients', 'GUpassword')
    # ### end Alembic commands ###