"""empty message

Revision ID: e1a88bcac1ba
Revises: b055f017428e
Create Date: 2022-04-11 10:53:06.611417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1a88bcac1ba'
down_revision = 'b055f017428e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musics', sa.Column('album_id', sa.Integer(), nullable=True))
    op.drop_constraint('musics_band_id_fkey', 'musics', type_='foreignkey')
    op.create_foreign_key(None, 'musics', 'albums', ['album_id'], ['album_id'])
    op.drop_column('musics', 'band_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('musics', sa.Column('band_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'musics', type_='foreignkey')
    op.create_foreign_key('musics_band_id_fkey', 'musics', 'bands', ['band_id'], ['band_id'])
    op.drop_column('musics', 'album_id')
    # ### end Alembic commands ###
