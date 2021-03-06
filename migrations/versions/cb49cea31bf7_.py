"""empty message

Revision ID: cb49cea31bf7
Revises: 
Create Date: 2021-06-19 20:14:54.325321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb49cea31bf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('clients_id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.Text(), nullable=True),
    sa.Column('lastName', sa.Text(), nullable=True),
    sa.Column('GUemail', sa.String(length=64), nullable=True),
    sa.Column('GUstate', sa.Text(), nullable=True),
    sa.Column('GUzipcode', sa.Text(), nullable=True),
    sa.Column('GUpassword', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('clients_id')
    )
    op.create_index(op.f('ix_clients_GUemail'), 'clients', ['GUemail'], unique=True)
    op.create_table('food_pantries',
    sa.Column('foodpantries_id', sa.Integer(), nullable=False),
    sa.Column('foodPantryName', sa.Text(), nullable=True),
    sa.Column('FPemail', sa.String(length=64), nullable=True),
    sa.Column('FPstreet', sa.Text(), nullable=True),
    sa.Column('FPcity', sa.Text(), nullable=True),
    sa.Column('FPphone', sa.Text(), nullable=True),
    sa.Column('FPwebsite', sa.Text(), nullable=True),
    sa.Column('timings', sa.Text(), nullable=True),
    sa.Column('infoBring', sa.Text(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('FPpassword', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('foodpantries_id')
    )
    op.create_index(op.f('ix_food_pantries_FPemail'), 'food_pantries', ['FPemail'], unique=True)
    op.create_table('states',
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('states', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('state_id')
    )
    op.create_table('zipcodes',
    sa.Column('zipcode_id', sa.Integer(), nullable=False),
    sa.Column('zipcode', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('zipcode_id')
    )
    op.create_table('serves',
    sa.Column('foodpantries_id', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['foodpantries_id'], ['food_pantries.foodpantries_id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['states.state_id'], )
    )
    op.create_table('zserves',
    sa.Column('foodpantries_id', sa.Integer(), nullable=True),
    sa.Column('zipcode_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['foodpantries_id'], ['food_pantries.foodpantries_id'], ),
    sa.ForeignKeyConstraint(['zipcode_id'], ['zipcodes.zipcode_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zserves')
    op.drop_table('serves')
    op.drop_table('zipcodes')
    op.drop_table('states')
    op.drop_index(op.f('ix_food_pantries_FPemail'), table_name='food_pantries')
    op.drop_table('food_pantries')
    op.drop_index(op.f('ix_clients_GUemail'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###
