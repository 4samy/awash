"""added reward points

Revision ID: 8038177a47cc
Revises: 64284dae8d6e
Create Date: 2021-04-28 09:03:34.004511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8038177a47cc'
down_revision = '64284dae8d6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=True),
    sa.Column('password', sa.LargeBinary(length=60), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('car_description', sa.Text(), nullable=True),
    sa.Column('reward_points', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('password', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('car_description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    op.drop_table('drivers')
    # ### end Alembic commands ###