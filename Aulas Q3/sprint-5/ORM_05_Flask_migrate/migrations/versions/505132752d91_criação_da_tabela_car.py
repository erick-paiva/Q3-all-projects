"""Criação da tabela Car

Revision ID: 505132752d91
Revises: 
Create Date: 2022-04-05 16:20:15.581516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505132752d91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('carmaker', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
