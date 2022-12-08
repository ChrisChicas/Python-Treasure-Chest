"""seed admin

Revision ID: 6fee7d8aba72
Revises: be978ffe2764
Create Date: 2022-12-07 21:21:25.635540

"""
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table
from alembic import op
from Project import _config
import sqlalchemy as sa
import bcrypt


# revision identifiers, used by Alembic.
revision = '6fee7d8aba72'
down_revision = 'be978ffe2764'
branch_labels = None
depends_on = None


def upgrade():
    users = table("users",
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=30), nullable=False),
        sa.Column('last_name', sa.String(length=30), nullable=False),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('password', sa.LargeBinary(), nullable=False),
        sa.Column('role', postgresql.ENUM('user', 'admin', name='user_roles', create_type=False), nullable=False),
    )

    op.bulk_insert(users,
    [
        {
            "first_name": "Snow",
            "last_name": "Bell",
            "username": "snowadmin",
            "password": bcrypt.hashpw(_config.admin_password.encode("utf-8"), bcrypt.gensalt(12)),
            "role": "admin"
        }
    ]
    )


def downgrade():
    pass
