"""empty message

Revision ID: 039a20c0bae3
Revises: 8396ba1673bb
Create Date: 2020-06-08 10:55:22.361507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '039a20c0bae3'
down_revision = '8396ba1673bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permission', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permission')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
