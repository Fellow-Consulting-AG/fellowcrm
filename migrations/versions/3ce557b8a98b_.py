"""empty message

Revision ID: 3ce557b8a98b
Revises: 
Create Date: 2021-05-10 17:33:47.201603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ce557b8a98b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('picklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('lang', sa.String(length=5), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('test_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_user_pkey')
    )
    op.drop_table('picklist')
    # ### end Alembic commands ###
