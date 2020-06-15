"""empty message

Revision ID: 4ff114342f66
Revises: e3876b5d695d
Create Date: 2020-06-09 16:21:12.683991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ff114342f66'
down_revision = 'e3876b5d695d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'permission')
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    op.add_column('roles', sa.Column('permission', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###