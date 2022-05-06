"""removendo a coluna api key

Revision ID: aac671abdf91
Revises: 10652f0a85e8
Create Date: 2022-04-21 18:27:22.609476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aac671abdf91'
down_revision = '10652f0a85e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'api_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('api_key', sa.VARCHAR(length=511), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
