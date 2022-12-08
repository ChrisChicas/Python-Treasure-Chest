"""Initial migration

Revision ID: 31baf7e49dcc
Revises: 
Create Date: 2022-12-07 20:53:31.808455

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '31baf7e49dcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.Column('role', postgresql.ENUM('user', 'admin', name='user_roles'), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('chests',
    sa.Column('chest_id', sa.Integer(), nullable=False),
    sa.Column('chest_name', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('chest_id')
    )
    op.create_table('treasures',
    sa.Column('treasure_id', sa.Integer(), nullable=False),
    sa.Column('treasure_title', sa.String(length=100), nullable=False),
    sa.Column('treasure_details', sa.Text(), nullable=False),
    sa.Column('chest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chest_id'], ['chests.chest_id'], ),
    sa.PrimaryKeyConstraint('treasure_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('treasures')
    op.drop_table('chests')
    op.drop_table('users')
    # ### end Alembic commands ###